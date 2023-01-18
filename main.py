# -* coding: utf-8 *-
from PySide6.QtCore import Qt, QPoint, Slot, Signal
from PySide6.QtGui import QIcon, QMouseEvent, QPixmap, QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSizeGrip, QDialog, QDialogButtonBox
import sys
from Design.qt_py import ui_main_window, ui_book_card, ui_ex_search_window, ui_book_window
import webbrowser
import pandas as pd

GLOBAL_STATE = 0
GLOBAL_STATE_2 = 0


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

        # Создание дополнительных переменных
        self.resize_btn = QSizeGrip(self.size_grip)
        self.resize_btn.setStyleSheet("QSizeGrip {width: 10px; height:10px; background-color: rgba(254,211,44,0)}")
        self.ex_search_dialog = ExtendSearchDialog()
        self.book_window = None
        self.dragPos = None
        self.ex_search_params = None
        self.ex_search_was_input = None
        self.can_ex_search = False
        self.full_screen = 0
        self.error_label.setText('')

    def clear_scroll(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

    def add_book_cards(self, headings, data):
        self.clear_scroll()
        db = pd.DataFrame(data, columns=headings)
        print(db.shape[0])
        for row in range(db.shape[0]):
            book_card = BookCard(db.loc[row])
            book_card.open_book_window.connect(self.open_book_window)
            self.scroll_layout.addWidget(book_card)

    def common_search(self):
        if self.search_input.text().strip() != '':
            search_text = self.search_input.text()
            db = pd.read_csv("Data_bases/test.csv", sep='|', dtype={'pages': 'str'})
            headings = list(db.columns)
            db = db.to_numpy()
            db = [row for row in db if search_text.lower() in row[13].lower()
                  or search_text.lower() in row[0].lower()]
            self.add_book_cards(headings, db)

    @Slot(pd.Series)
    def open_book_window(self, data: pd.Series):
        widget = self.sender()
        if self.book_window is None:
            self.book_window = BookWindow(data)
        else:
            self.book_window.close()
            self.book_window = BookWindow(data)
        self.book_window.show()

    def move_window(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            p = event.globalPosition()
            mouse_global_pos = p.toPoint()
            if self.full_screen == 1:
                self.maximize_restore()
                self.move(QPoint(mouse_global_pos.x() - self.width() // 2, mouse_global_pos.y()))
            self.move(self.pos() + mouse_global_pos - self.dragPos)
            self.dragPos = mouse_global_pos
            event.accept()

    def open_ex_search(self):
        self.setEnabled(False)
        resut = self.ex_search_dialog.exec()
        if resut:
            inputs = self.ex_search_dialog.get_input_info()
            self.ex_search_was_input = self.ex_search_dialog.get_was_input()
            if self.ex_search_was_input:
                self.ex_search_params = inputs
                self.ex_search_status.setText('Параметры расширенного поиска заданы')
                self.ex_search_inputs.setText(f'Было заполнено: {sum(self.ex_search_was_input)} полей')
                self.can_ex_search = True
            else:
                self.ex_search_status.setText('Параметры расширенного поиска не заданы')
                self.can_ex_search = False
        self.setEnabled(True)

    def ex_search(self):
        if self.can_ex_search:
            db = pd.read_csv("Data_bases/test.csv", sep='|', dtype={'pages': 'str'})
            headings = list(db.columns)
            db = db.to_numpy()
            was_input = self.ex_search_was_input
            inputs = self.ex_search_params
            if sum(was_input) == 0:
                print('Ничего не введено')
                return
            print(was_input)
            print(inputs)
            loaded_rows = []
            for row in db:
                was_found = []
                if was_input[0]:
                    if was_input[1]:
                        if inputs[0] in row[0].lower():
                            was_found.append(True)
                    if was_input[2]:
                        if inputs[0] in row[12].lower():
                            was_found.append(True)
                    if was_input[0]:
                        was_found.append(True)
                if was_input[3]:
                    if inputs[3] == row[1]:
                        was_found.append(True)
                if was_input[4]:
                    if inputs[4] in str(row[6]):
                        was_found.append(True)
                if was_input[5]:
                    if str(inputs[5]) in str(row[2]):
                        was_found.append(True)
                if was_input[6]:
                    if inputs[6] == row[8]:
                        was_found.append(True)
                if was_input[7]:
                    if inputs[7] in row[10]:
                        was_found.append(True)
                if was_input[8]:
                    if inputs[8] in row[9]:
                        was_found.append(True)
                if was_input[9]:
                    if inputs[9] == row[4]:
                        was_found.append(True)
                if was_input[10]:
                    if inputs[10] in str(row[7]):
                        was_found.append(True)
                if sum(was_found) == sum(was_input):
                    loaded_rows.append(row)
            self.add_book_cards(headings, loaded_rows)

    def mousePressEvent(self, event: QMouseEvent):
        p = event.globalPosition()
        mouse_global_pos = p.toPoint()
        self.dragPos = mouse_global_pos

    def maximize_restore(self):
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
            self.main_body.setStyleSheet('#main_body {border-radius: 10%;} '
                                              '#title_bar {border-top-left-radius: 10%; border-top-right-radius: 10%}')

    def closeEvent(self, event: QCloseEvent):
        if self.book_window is not None:
            self.book_window.close()
        event.accept()


class BookCard(QWidget, ui_book_card.Ui_book_card):
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
        webbrowser.open(self.data['link'])

    @Slot(pd.Series)
    def open_btn_press(self):
        self.open_book_window.emit(self.data)

    def load_data(self):
        self.heading_label.setText(str(self.data['title']))
        self.year_label.setText(str(self.data['year']))
        self.type_label.setText(str(self.data['book_type']))
        self.pages_label.setText(str(self.data['pages']))
        self.authors_label.setText(str(self.data['author']))
        image = QPixmap(f'Design/images/{self.data["isbn"]}.jpg')
        self.image.setPixmap(image.scaledToHeight(self.image_container.height() - 10))


class ExtendSearchDialog(QDialog, ui_ex_search_window.Ui_ex_search_window):
    def __init__(self):
        super(ExtendSearchDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.title_bar.mouseMoveEvent = self.move_window
        self.buttons.button(QDialogButtonBox.StandardButton.Reset).clicked.connect(self.reset_fields)
        self.dragPos = None
        self.buttons.button(QDialogButtonBox.StandardButton.Ok).setText('Задать')
        self.buttons.button(QDialogButtonBox.StandardButton.Reset).setText('Очистить')
        self.load_info()

    def reset_fields(self):
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
        if event.buttons() == Qt.LeftButton:
            p = event.globalPosition()
            mouse_global_pos = p.toPoint()
            self.move(self.pos() + mouse_global_pos - self.dragPos)
            self.dragPos = mouse_global_pos
            event.accept()

    def mousePressEvent(self, event: QMouseEvent):
        p = event.globalPosition()
        mouse_global_pos = p.toPoint()
        self.dragPos = mouse_global_pos

    def get_input_info(self):
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
        return text, in_headers, in_annotation, publishing, author, year, isbn, udk, bbk, book_type, discipline

    def get_was_input(self):
        data = self.get_input_info()
        was_input = [bool(i) for i in data]
        return was_input


class BookWindow(QWidget, ui_book_window.Ui_book_window):
    def __init__(self, data: pd.Series):
        super(BookWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.max_btn.clicked.connect(self.maximize_restore)
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.title_bar.mouseMoveEvent = self.move_window
        self.open_library_btn.clicked.connect(self.open_browser)
        self.resize_btn = QSizeGrip(self.size_grip)
        self.resize_btn.setStyleSheet("QSizeGrip {width: 10px; height:10px; background-color: rgba(254,211,44,0)}")
        self.ex_search_dialog = None
        self.dragPos = None
        self.full_screen = 0
        self.resize(800, 655)
        self.spawn_coords = QPoint(self.width() // 2, self.height() // 30)
        self.move(self.spawn_coords)
        self.data = data
        self.load_data()

    def open_browser(self):
        webbrowser.open(self.data['link'])

    def load_data(self):
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
        p = event.globalPosition()
        mouse_global_pos = p.toPoint()
        self.dragPos = mouse_global_pos

    def maximize_restore(self):
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
