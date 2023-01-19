# -* coding: utf-8 *-
from PySide6.QtCore import Qt, QPoint, Slot, Signal
from PySide6.QtGui import QIcon, QMouseEvent, QPixmap, QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSizeGrip, QDialog, QDialogButtonBox, QComboBox
import sys
from Design.qt_py import ui_main_window, ui_book_card, ui_ex_search_window, ui_book_window
import webbrowser
import pandas as pd
from math import ceil

GLOBAL_STATE = 0
GLOBAL_STATE_2 = 0


def get_values_of_combobox(combobox: QComboBox):
    """ Метод для получения всех значений QComboBox """
    return (combobox.itemText(i) for i in range(combobox.count()))


class MainWindow(QMainWindow, ui_main_window.Ui_main_window):
    """ Класс главного окна """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Инициализация дизайна
        self.setWindowFlag(Qt.FramelessWindowHint)  # Удаление встроенного title bar
        self.setAttribute(Qt.WA_TranslucentBackground)  # Делаем фон окна прозрачным
        # Привязка функций к кнопкам и событиям
        self.max_btn.clicked.connect(self.maximize_restore)
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.ex_search_params_btn.clicked.connect(self.open_ex_search)
        self.title_bar.mouseMoveEvent = self.move_window
        self.search_btn.clicked.connect(self.common_search)
        self.ex_search_btn.clicked.connect(self.ex_search)
        self.pagination_next_btn.clicked.connect(lambda: self.move_pagination('right'))
        self.pagination_prev_btn.clicked.connect(lambda: self.move_pagination('left'))
        self.sort_btn.clicked.connect(self.sort_loaded_rows)
        # Создание дополнительных переменных
        self.resize_btn = QSizeGrip(self.size_grip)
        self.ex_search_dialog = ExtendSearchDialog()
        self.book_window = None
        self.dragPos = None
        self.ex_search_params = None
        self.ex_search_was_input = None
        self.can_ex_search = False
        self.rows_was_load = False
        self.full_screen = 0
        self.pagination_cursor = 0
        self.rows_on_page = 30
        self.loaded_rows = []
        # Применение дополнительных действий
        self.resize_btn.setStyleSheet("QSizeGrip {width: 10px; height:10px; background-color: rgba(254,211,44,0)}")
        self.error_label.setText('')
        self.pagination_label.setText('0/0')
        self.load_sort_keys()

    def load_sort_keys(self):
        """ Метод загрузки ключей сортировки в QComboBox """
        keys = ['', 'Году издания', 'Алфавиту', 'Номеру УДК', 'Номеру ББК']
        self.sort_params.addItems(keys)

    def sort_loaded_rows(self):
        """ Метод сортировки загруженных в программу строк (книг) по заданному ключу """
        sort_key = self.sort_params.currentText()
        # Если книги еще не были загружены прерываем процесс и сообщаем об ошибке пользователю
        if not self.rows_was_load:
            self.error_label.setText('Сначала необходимо найти книги')
            return
        if sort_key == '':
            self.error_label.setText('Параметр сортировки не задан')
            return
        # Производим сортировку в зависимости от значения ключа
        if sort_key == 'Году издания':
            self.loaded_rows = sorted(self.loaded_rows, key=lambda x: max([int(i) for i in x[2].split(',')]))
        if sort_key == 'Алфавиту':
            self.loaded_rows = sorted(self.loaded_rows, key=lambda x: x[0])
        if sort_key == 'Номеру УДК':
            self.loaded_rows = sorted(self.loaded_rows, key=lambda x: x[10].split(',')[0])
        if sort_key == 'Номеру ББК':
            self.loaded_rows = sorted(self.loaded_rows, key=lambda x: x[9].split(',')[0])
        # Если указана сортировка по убыванию, "переворачиваем сортированный список"
        if self.checkBox.isChecked():
            self.loaded_rows = self.loaded_rows[::-1]
        # Загружаем сортированный список книг в UI
        self.error_label.setText(f'Все {len(self.loaded_rows)} книг были сортированы по {sort_key}')
        self.pagination_cursor = 1
        self.add_book_cards()

    def move_pagination(self, direction: str):
        """ Метод 'передвижения' по панели пагинации """
        pages_count = ceil(len(self.loaded_rows) / self.rows_on_page) + 1  #
        # Если нужно переместиться вперед
        if direction == 'right':
            # Если находимся не на последней странице
            if self.pagination_cursor != pages_count - 1:
                self.pagination_cursor = (self.pagination_cursor + 1) % pages_count
                self.add_book_cards()
        # Если нужно переместиться назад
        elif direction == 'left':
            # Если находимся не на первой странице
            if self.pagination_cursor != 1:
                self.pagination_cursor = (self.pagination_cursor - 1) % pages_count
                self.add_book_cards()

    def clear_scroll(self):
        """ Метод очистки QScrollArea от виджетов загруженных книг """
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

    def add_book_cards(self):
        """ Метод загрузки карточек найденных книг в виджет QScrollArea """
        self.clear_scroll()  # Очищаем QScrollArea перед загрузкой
        headings = ['title', 'publishing', 'year', 'pages', 'book_type', 'lvl_education', 'author', 'discipline',
                    'isbn', 'bbk', 'ydk', 'bibl_record', 'annotation', 'link']
        # Создаем DataFrame со строками тех книг, которые находятся на текущей странице пагинации
        db = pd.DataFrame(
            self.loaded_rows[self.rows_on_page*(self.pagination_cursor - 1):self.rows_on_page * self.pagination_cursor],
            columns=headings)
        # Сообщаем пользователю, на какой странице пагинации он находится
        self.pagination_label.setText(f'{self.pagination_cursor} из {ceil(len(self.loaded_rows) / self.rows_on_page)}')
        # Загружаем карточки книг
        for row in range(db.shape[0]):
            book_card = BookCard(db.loc[row])  # Создаем экземпляр класса
            # Связываем карточку с главным окном, чтобы потом получать от нее сигнал
            book_card.open_book_window.connect(self.open_book_window)
            self.scroll_layout.addWidget(book_card)

    def common_search(self):
        """ Метод осуществления обычного поиска (по названию книги) """
        # Проверяем, заполнена ли строка поиска и сообщаем пользователю, если это не так
        if self.search_input.text().strip() != '':
            search_text = self.search_input.text()  #
            # Получаем информацию из базы данных
            db = pd.read_csv("Data_bases/test.csv", sep='|', dtype={'pages': 'str'})
            db = db.to_numpy()
            # Если в названии книги есть исковая подстрока, то загружаем книгу
            self.loaded_rows = [row for row in db if search_text.lower() in row[13].lower()
                                or search_text.lower() in row[0].lower()]
            # Сообщаем пользователю, что по его запросу было найдено n книг
            self.error_label.setText(f'Было найдено {len(self.loaded_rows)} книг')
            self.pagination_cursor = 1 if ceil(len(self.loaded_rows) / self.rows_on_page) else 0
            self.rows_was_load = True  # Книги были загружены
            self.add_book_cards()
        else:
            self.error_label.setText('Строка поиска пуста')

    @Slot(pd.Series)
    # Принимаем сигнал от карточки книги
    def open_book_window(self, data: pd.Series):
        """ Метод для открытия окна определенной книги с подробной информацией """
        # Если окно уже открыто, закрываем его и создаем новое
        if self.book_window is None:
            self.book_window = BookWindow(data)
        else:
            self.book_window.close()
            self.book_window = BookWindow(data)
        # Открываем окно
        self.book_window.show()

    def open_ex_search(self):
        """ Метод открытия диалогового окна ввода данных для расширенного поиска """
        self.setEnabled(False)  # Отключаем взаимодействие с главным окном
        resut = self.ex_search_dialog.exec()  # Запускаем диалоговое окно
        # Проверяем, была ли нажата кнопка "Задать"
        if resut:
            # Получаем значения всех полей и информацию о том, было ли заполнено поле
            inputs = self.ex_search_dialog.get_input_info()
            self.ex_search_was_input = self.ex_search_dialog.get_was_input()
            # Если хоть одно поле было заполнено, то разрешаем произвести поиск
            if any(self.ex_search_was_input):
                self.ex_search_params = inputs
                self.ex_search_status.setText('Параметры расширенного поиска заданы')
                self.ex_search_inputs.setText(f'Было заполнено: {sum(self.ex_search_was_input)} полей')
                self.can_ex_search = True
            else:
                self.ex_search_status.setText('Параметры расширенного поиска не заданы')
                self.ex_search_inputs.setText(f'Было заполнено: 0 полей')
                self.can_ex_search = False
        self.setEnabled(True)  # Включаем взаимодействие с главным окном

    def ex_search(self):
        """ Метод осуществления расширенного поиска (по множеству параметров) """
        # Если расширенный поиск разрешен
        if self.can_ex_search:
            # Получаем информацию из базы данных
            db = pd.read_csv("Data_bases/test.csv", sep='|', dtype={'pages': 'str'})
            db = db.to_numpy()
            was_input = self.ex_search_was_input
            inputs = self.ex_search_params
            loaded_rows = []  # Строки, которые пройдут отбор по всем заданным критериям
            # Проверяем каждую книгу в БД на соответствие заданным параметрам
            for row in db:
                was_found = 0  # Количество совпадений
                # Поиск искомой строки в названии или в аннотации книги
                if was_input[0]:
                    if was_input[1]:
                        if inputs[0] in row[0].lower():
                            was_found += 1
                    if was_input[2]:
                        if inputs[0] in row[12].lower():
                            was_found += 1
                    if was_found:
                        was_found += 1
                # Поиск года издания книги
                if was_input[3]:
                    if str(inputs[3]) in str(row[2]):
                        was_found += 1
                #  Поиск издательства
                if was_input[4]:
                    if inputs[4] == row[1]:
                        was_found += 1
                # Поиск автора
                if was_input[5]:
                    if inputs[5] in str(row[6]):
                        was_found += 1
                # Поиск isbn
                if was_input[6]:
                    if inputs[6] == row[8]:
                        was_found += 1
                # Поиск УДК
                if was_input[7]:
                    if inputs[7] in row[10]:
                        was_found += 1
                # Поиск ББК
                if was_input[8]:
                    if inputs[8] in row[9]:
                        was_found += 1
                # Поиск вида издания
                if was_input[9]:
                    if inputs[9] == row[4]:
                        was_found += 1
                # Поиск дисциплины
                if was_input[10]:
                    if inputs[10] in str(row[7]):
                        was_found += 1
                # Если кол-во совпадений равно кол-ву заполненных полей, книга подходит
                if was_found == sum(was_input):
                    loaded_rows.append(row)
            # Загружаем найденные книги в QScrollArea
            self.loaded_rows = loaded_rows
            self.error_label.setText(f'Было найдено {len(self.loaded_rows)} книг')
            self.pagination_cursor = 1 if ceil(len(self.loaded_rows) / self.rows_on_page) else 0
            self.rows_was_load = True
            self.add_book_cards()

    def mousePressEvent(self, event: QMouseEvent):
        """ Метод определения положения мыши после нажатия ее кнопок """
        p = event.globalPosition()
        mouse_global_pos = p.toPoint()
        self.dragPos = mouse_global_pos

    def maximize_restore(self):
        """ Метод перехода окна в полноэкранный режим и обратно """
        status = self.full_screen  # Состояние окна
        if status == 0:
            self.full_screen = 1
            self.max_btn.setIcon(QIcon('Design/For_QT/minimize-2.svg'))
            self.showMaximized()
            self.main_body.setStyleSheet('#main_body {border-radius: 0%;} #title_bar {border-radius: 0%;}')
        else:
            self.full_screen = 0
            self.showNormal()
            self.max_btn.setIcon(QIcon('Design/For_QT/maximize-2.svg'))
            self.main_body.setStyleSheet('#main_body {border-radius: 10%;} '
                                         '#title_bar {border-top-left-radius: 10%; border-top-right-radius: 10%}')

    def move_window(self, event: QMouseEvent):
        """ Метод перемещения окна с помощью мыши """
        # Если зажата левая кнопка мыши
        if event.buttons() == Qt.LeftButton:
            # Определяем координаты курсора относительно глобальной системы координат
            p = event.globalPosition()
            mouse_global_pos = p.toPoint()
            # Если окно открыто в полноэкранном режиме, уменьшаем его до нормальных размеров
            if self.full_screen == 1:
                self.maximize_restore()
                self.move(QPoint(mouse_global_pos.x() - self.width() // 2, mouse_global_pos.y()))
            self.move(self.pos() + mouse_global_pos - self.dragPos)
            self.dragPos = mouse_global_pos
            event.accept()

    def closeEvent(self, event: QCloseEvent):
        """ Метод закрытия окна """
        # Если окно закрывается, все дочерние окна - тоже
        if self.book_window is not None:
            self.book_window.close()
        event.accept()


class BookCard(QWidget, ui_book_card.Ui_book_card):
    """ Класс карточки с краткой информацией о книге """
    # Создаем сигнал, который будем посылать главному окну
    open_book_window = Signal(pd.Series)

    def __init__(self, data: pd.Series):
        super(BookCard, self).__init__()
        self.setupUi(self)
        self.resize(self.minimumSize())
        self.open_here_btn.clicked.connect(self.open_btn_press)
        self.open_library_btn.clicked.connect(self.open_browser)
        self.data = data
        self.load_data()

    def open_browser(self):
        """ Метод открытия страницы книги в онлайн библиотеке """
        webbrowser.open(self.data['link'])

    @Slot(pd.Series)
    def open_btn_press(self):
        """ Метод открытия окна с подробной информацией о книге """
        # Отправляем сигнал о том, что нужно открыть окно и передаем данные книги
        self.open_book_window.emit(self.data)

    def load_data(self):
        """ Метод загрузки краткой информации о книге при инициализации """
        self.heading_label.setText(str(self.data['title']))
        self.year_label.setText(str(self.data['year']))
        self.type_label.setText(str(self.data['book_type']))
        self.pages_label.setText(str(self.data['pages']))
        self.authors_label.setText(str(self.data['author']))
        image = QPixmap(f'Design/images/{self.data["isbn"]}.jpg')
        self.image.setPixmap(image.scaledToHeight(self.image_container.height() - 10))


class ExtendSearchDialog(QDialog, ui_ex_search_window.Ui_ex_search_window):
    """ Класс диалогового окна ввода данных для расширенного поиска """
    def __init__(self):
        # Инициализация UI
        super(ExtendSearchDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Привязка функций и к кнопкам и событиям
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.title_bar.mouseMoveEvent = self.move_window
        self.buttons.button(QDialogButtonBox.StandardButton.Reset).clicked.connect(self.reset_fields)
        self.string_input.textChanged.connect(self.check_errors)
        self.in_headings.stateChanged.connect(self.check_errors)
        self.in_annotation.stateChanged.connect(self.check_errors)
        self.year_input.textChanged.connect(self.check_errors)
        self.load_info()
        comboboxes = [self.publishings_combobox, self.author_combobox, self.isbn_combobox,
                      self.udk_combobox, self.bbk_combobox, self.type_combobox, self.discipline_combobox]
        for box in comboboxes:
            box.currentTextChanged.connect(self.check_errors)
            box.setMaxCount(box.count())
        self.discipline_combobox.currentTextChanged.connect(self.check_errors)
        # Дополнительные переменные и действия
        self.dragPos = None
        self.can_set = True
        self.buttons.button(QDialogButtonBox.StandardButton.Ok).setText('Задать')
        self.buttons.button(QDialogButtonBox.StandardButton.Reset).setText('Очистить')
        self.error_label.setText('')

    def reset_fields(self):
        """ Метод для сброса значений всех полей """
        self.string_input.setText('')
        self.in_annotation.setChecked(False)
        self.in_headings.setChecked(False)
        self.year_input.setText('')
        self.publishings_combobox.setCurrentText('')
        self.author_combobox.setCurrentText('')
        self.isbn_combobox.setCurrentText('')
        self.udk_combobox.setCurrentText('')
        self.bbk_combobox.setCurrentText('')
        self.type_combobox.setCurrentText('')
        self.discipline_combobox.setCurrentText('')

    def load_info(self):
        """ Метод загрузки вариантов запросов в комбо-боксы """
        db = pd.read_csv("Data_bases/summary_table.csv", sep='|')
        publishings = [i for i in db['publishing'] if str(i) != 'nan']
        book_types = [i for i in db['book_type'] if str(i) != 'nan']
        bbks = [i for i in db['bbk'] if str(i) != 'nan']
        udks = [i for i in db['udk'] if str(i) != 'nan']
        disciplines = [i for i in db['discipline'] if str(i) != 'nan']
        authors = [i for i in db['author'] if str(i) != 'nan']
        isbns = [i for i in db['isbn'] if str(i) != 'nan']
        self.publishings_combobox.addItem('')
        self.type_combobox.addItem('')
        self.udk_combobox.addItem('')
        self.bbk_combobox.addItem('')
        self.discipline_combobox.addItem('')
        self.author_combobox.addItem('')
        self.isbn_combobox.addItem('')
        self.publishings_combobox.addItems(publishings)
        self.type_combobox.addItems(book_types)
        self.udk_combobox.addItems(udks)
        self.bbk_combobox.addItems(bbks)
        self.discipline_combobox.addItems(disciplines)
        self.author_combobox.addItems(authors)
        self.isbn_combobox.addItems(isbns)

    def move_window(self, event: QMouseEvent):
        """ Метод перемещения окна с помощью мыши """
        if event.buttons() == Qt.LeftButton:
            p = event.globalPosition()
            mouse_global_pos = p.toPoint()
            self.move(self.pos() + mouse_global_pos - self.dragPos)
            self.dragPos = mouse_global_pos
            event.accept()

    def mousePressEvent(self, event: QMouseEvent):
        """ Метод закрытия окна """
        p = event.globalPosition()
        mouse_global_pos = p.toPoint()
        self.dragPos = mouse_global_pos

    def get_input_info(self):
        """ Метод получения значений всех полей ввода """
        text = ' '.join(self.string_input.text().strip().split()).lower()
        in_headers = self.in_headings.isChecked()
        in_annotation = self.in_annotation.isChecked()
        year = ' '.join(self.year_input.text().strip().split()).lower()
        publishing = ' '.join(self.publishings_combobox.currentText().strip().split())
        author = ' '.join(self.author_combobox.currentText().strip().split())
        isbn = ' '.join(self.isbn_combobox.currentText().strip().split())
        udk = ' '.join(self.udk_combobox.currentText().strip().split())
        bbk = ' '.join(self.bbk_combobox.currentText().strip().split())
        book_type = ' '.join(self.type_combobox.currentText().strip().split())
        discipline = ' '.join(self.discipline_combobox.currentText().strip().split())
        return text, in_headers, in_annotation, year, publishing, author, isbn, udk, bbk, book_type, discipline

    def get_was_input(self):
        """ Метод получений о том, заполнены поля или нет """
        data = self.get_input_info()  # Получаем значения полей
        was_input = [bool(i) for i in data]  # Проверяем, заполнены ли они
        # Если поле искомой строки пусто или не задана область поиска строки
        if (was_input[0] and (not was_input[1] and not was_input[2])) or\
                ((not was_input[0]) and (was_input[1] or was_input[2])):
            was_input[0] = was_input[1] = was_input[2] = False
        return was_input

    def check_errors(self):
        """ Метод проверки правильности заполнения полей """
        # Получаем значения полей
        text, in_headers, in_annotation, year, publishing,\
            author, isbn, udk, bbk, book_type, discipline = self.get_input_info()
        self.can_set = True  # Возможность задать параметры
        message = ''  # Сообщение, которое будет передаваться пользователю
        # Если хоть одно поле будет заполнено неправильно, то пользователь не сможет задать параметры
        if text and (not in_headers and not in_annotation):
            message = 'Не задана область поиска'
            self.can_set = False
        if (not text) and (in_annotation or in_headers):
            message = 'Не введена искомая строка'
            self.can_set = False
        if (not year.isdigit()) and year != '':
            message = 'Год издания должен состоять только из цифр'
            self.can_set = False
        if publishing not in get_values_of_combobox(self.publishings_combobox):
            message = 'Такого издательства нет'
            self.can_set = False
        if author not in get_values_of_combobox(self.author_combobox):
            message = 'Такого автора нет'
            self.can_set = False
        if isbn not in get_values_of_combobox(self.isbn_combobox):
            message = 'Такого номера ISBN нет'
            self.can_set = False
        if udk not in get_values_of_combobox(self.udk_combobox):
            message = 'Такого номера УДК нет'
            self.can_set = False
        if bbk not in get_values_of_combobox(self.bbk_combobox):
            message = 'Такого номера ББК нет'
            self.can_set = False
        if book_type not in get_values_of_combobox(self.type_combobox):
            message = 'Такого вида издательства нет'
            self.can_set = False
        if discipline not in get_values_of_combobox(self.discipline_combobox):
            message = 'Такой дисциплины нет'
            self.can_set = False
        self.error_label.setText(message)
        self.change_style_ok_btn(self.can_set)

    def change_style_ok_btn(self, flag):
        """ Метод для изменения стиля кнопки 'задать' в зависимости от правильности заполнения полей """
        # Создаем правила QSS
        if flag:
            style = 'QPushButton ' \
                    '{background: rgba(254,211,44,255); ' \
                    'border-radius: 5px; ' \
                    'padding: 0 10px 0 10px; ' \
                    'height: 40px; ' \
                    'color: black;}'
        else:
            style = 'QPushButton ' \
                    '{background: rgba(25, 27, 30, 1); ' \
                    'border-radius: 5px; ' \
                    'padding: 0 10px 0 10px; ' \
                    'height: 40px; ' \
                    'color: white;}'
        # Применяем к элементу созданные правила
        self.buttons.button(QDialogButtonBox.StandardButton.Ok).setStyleSheet(style)
        # Включаем/отключаем взаимодействие с элементом
        self.buttons.button(QDialogButtonBox.StandardButton.Ok).setEnabled(self.can_set)


class BookWindow(QWidget, ui_book_window.Ui_book_window):
    """ Класс окна с подробной информацией о книге """
    def __init__(self, data: pd.Series):
        # Инициализируем дизайн
        super(BookWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Привязываем функции к кнопкам и событиям
        self.max_btn.clicked.connect(self.maximize_restore)
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.title_bar.mouseMoveEvent = self.move_window
        self.open_library_btn.clicked.connect(self.open_browser)
        # Дополнительные переменные и действия
        self.resize_btn = QSizeGrip(self.size_grip)
        self.resize_btn.setStyleSheet("QSizeGrip {width: 10px; height:10px; background-color: rgba(254,211,44,0)}")
        self.ex_search_dialog = None
        self.dragPos = None
        self.full_screen = 0
        self.spawn_coords = QPoint(self.width() // 2, self.height() // 30)
        self.move(self.spawn_coords)
        self.data = data
        self.load_data()

    def open_browser(self):
        webbrowser.open(self.data['link'])

    def load_data(self):
        """ Метод загрузки информации о книге при инициализации """
        self.label.setPixmap(QPixmap(f'Design/images/{self.data["isbn"]}.jpg'))
        self.book_title.setText(self.data['title'])
        self.publishings_label.setText(self.data['publishing'])
        self.year_label.setText(str(self.data['year']))
        self.pages_label.setText(str(self.data['pages']))
        self.type_label.setText(self.data['book_type'])
        self.education_lvl_label.setText(str(self.data['lvl_education']))
        self.discipline_label.setText(self.data['discipline'])
        self.authors_label.setText(self.data['author'])
        self.isbn_text.setText(self.data['isbn'])
        self.bibliographic_record_text.setText(self.data['bibl_record'])
        self.annotation_text.setText(self.data['annotation'])
        text_bbk = ''
        text_udk = ''
        for bbk in self.data['bbk'].split('/'):
            text_bbk += f'{bbk.split(",")[0]}: {bbk.split(",")[1]}\n'
        for udk in self.data['ydk'].split('/'):
            text_udk += f'{udk.split(",")[0]}: {udk.split(",")[1]}\n'
        self.bbk_text.setText(text_bbk)
        self.udk_text.setText(text_udk)

    def move_window(self, event: QMouseEvent):
        """ Метод перемещения окна с помощью мыши """
        if event.buttons() == Qt.LeftButton:
            p = event.globalPosition()
            mouse_global_pos = p.toPoint()
            if self.full_screen == 1:
                self.maximize_restore()
                self.move(QPoint(mouse_global_pos.x() - self.width() // 2, mouse_global_pos.y()))
            self.move(self.pos() + mouse_global_pos - self.dragPos)
            self.dragPos = mouse_global_pos
            event.accept()

    def mousePressEvent(self, event: QMouseEvent):
        """ Метод определения положения мыши после нажатия ее кнопок """
        p = event.globalPosition()
        mouse_global_pos = p.toPoint()
        self.dragPos = mouse_global_pos

    def maximize_restore(self):
        """ Метод перехода окна в полноэкранный режим и обратно """
        status = self.full_screen
        if status == 0:
            self.full_screen = 1
            self.max_btn.setIcon(QIcon('Design/For_QT/minimize-2.svg'))
            self.showMaximized()
            self.main_body.setStyleSheet('#main_body {border-radius: 0%;} #title_bar {border-radius: 0%;}')

        else:
            self.full_screen = 0
            self.max_btn.setIcon(QIcon('Design/For_QT/maximize-2.svg'))
            self.showNormal()
            self.move(self.spawn_coords)
            self.move(self.spawn_coords)
            self.main_body.setStyleSheet('#main_body {border-radius: 10%;} '
                                         '#title_bar {border-top-left-radius: 10%; border-top-right-radius: 10%}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
