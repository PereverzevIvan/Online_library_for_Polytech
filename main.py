# -* coding: utf-8 *-
import numpy
from PySide6.QtCore import Qt, QPoint, Slot, Signal
from PySide6.QtGui import QIcon, QMouseEvent, QPixmap, QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSizeGrip, QDialog, QDialogButtonBox
import sys
from Design.qt_py import ui_main_window, ui_book_card, ui_ex_search_window, ui_book_window
import webbrowser
import pandas as pd
import numpy

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

        # Создание дополнительных переменных
        self.resize_btn = QSizeGrip(self.size_grip)
        self.resize_btn.setStyleSheet("QSizeGrip {width: 10px; height:10px; background-color: rgba(254,211,44,0)}")
        self.ex_search_dialog = ExtendSearchDialog()
        self.book_window = None
        self.dragPos = None
        self.ex_search_params = None
        self.can_ex_search = False
        self.full_screen = 0
        self.error_label.setText('')

    def clear_scroll(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)

    def add_book_cards(self, headings, data):
        self.clear_scroll()
        db = pd.DataFrame(data, columns=headings)
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
            inputs = self.ex_search_dialog.get_info()
            corr_id = sum([i != '' for i in inputs[:-2]])
            if corr_id:
                self.ex_search_params = inputs
                self.ex_search_status.setText('Параметры расширенного поиска заданы')
                self.ex_search_inputs.setText(f'Было заполнено: {corr_id} полей')
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
            loaded_rows = []
            in_head, in_annotation = [False for _ in range(2)]
            for i in db:
                if self.ex_search_params[0]:
                    if self.ex_search_params[-2]:
                        if self.ex_search_params[0].lower() in i[0]:
                            in_head = True
                        if self.ex_search_params[0].lower() in i[0]:
                            in_annotation = True
            self.add_book_cards(headings, db)

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
        self.heading_label.setText(self.data['title'])
        self.year_label.setText(str(self.data['year']))
        self.type_label.setText(self.data['book_type'])
        self.pages_label.setText(str(self.data['pages']))
        self.authors_label.setText(self.data['author'])
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
        self.dragPos = None
        self.buttons.button(QDialogButtonBox.StandardButton.Ok).setText('Задать')
        self.buttons.button(QDialogButtonBox.StandardButton.Cancel).setText('Отмена')
        self.load_info()

    def load_info(self):
        db = pd.read_csv("Data_bases/test.csv", sep='|', dtype={'pages': 'str'})
        publishings = sorted(set(db['publishing']))
        book_types = list(set(db['book_type']))
        self.publishings_combobox.addItem('Выберите издательство')
        self.type_combobox.addItem('Выберите вид издательства')
        self.udk_combobox.addItem('Выберите номер УДК')
        self.bbk_combobox.addItem('Выберите номер ББК')
        for i in publishings:
            if str(i) != 'nan':
                self.publishings_combobox.addItem(i)
        for i in book_types:
            if str(i) != 'nan':
                self.type_combobox.addItem(i)

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

    def get_info(self):
        text = self.string_input.text()
        in_headers = self.in_headings.isChecked()
        in_annotation = self.in_annotation.isChecked()
        publishing = self.publishings_combobox.currentText()
        author = self.author_input.text()
        year = self.year_input.text()
        isbn = self.isbn_input.text()
        udk = self.udk_combobox.currentText()
        bbk = self.bbk_combobox.currentText()
        book_type = self.type_combobox.currentText()
        return text, publishing, author, year, isbn, udk, bbk, book_type, in_headers, in_annotation


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
        self.education_lvl_label.setText(self.data['lvl_education'])
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
