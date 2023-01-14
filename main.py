# -* coding: utf-8 *-
from PySide6.QtCore import Qt, QPoint, Slot, Signal
from PySide6.QtGui import QIcon, QMouseEvent, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSizeGrip, QDialog, QDialogButtonBox
import sys
from Design.qt_py import ui_main_window, ui_book_card, ui_ex_search_window, ui_book_window
import webbrowser
import csv

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

        # Создание дополнительных переменных
        self.resize_btn = QSizeGrip(self.size_grip)
        self.resize_btn.setStyleSheet("QSizeGrip {width: 10px; height:10px; background-color: rgba(254,211,44,0)}")
        self.ex_search_dialog = None
        self.book_window = None
        self.dragPos = None
        self.full_screen = 0
        self.error_label.setText('')

        self.add_book_cards()

    def add_book_cards(self):
        file = open('data_base.csv', mode='r', encoding='utf-8')
        reader = csv.reader(file, delimiter='\t')
        data = [i for i in reader]

        for i in range(10):
            book_card = BookCard()
            book_card.open_book_window.connect(self.open_book_window)
            self.scroll_layout.addWidget(book_card)

    @Slot(list)
    def open_book_window(self, data: list):
        widget = self.sender()
        if self.book_window is None:
            self.book_window = BookWindow()
        else:
            self.book_window.close()
            self.book_window = self.book_window = BookWindow()
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
        self.ex_search_dialog = ExtendSearchDialog()
        self.setEnabled(False)
        resut = self.ex_search_dialog.exec()
        self.setEnabled(True)

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


class BookCard(QWidget, ui_book_card.Ui_book_card):
    open_book_window = Signal(list)

    def __init__(self):
        super(BookCard, self).__init__()
        self.setupUi(self)
        self.resize(self.minimumSize())
        image = QPixmap('Design/images/img.jpg')
        self.image.setPixmap(image.scaledToHeight(self.image_container.height() - 10))
        self.open_here_btn.clicked.connect(self.open_btn_press)

    @Slot(list)
    def open_btn_press(self):
        self.open_book_window.emit(['Это номер ISBN!'])


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


class BookWindow(QWidget, ui_book_window.Ui_book_window):
    def __init__(self):
        super(BookWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.max_btn.clicked.connect(self.maximize_restore)
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.title_bar.mouseMoveEvent = self.move_window
        self.resize_btn = QSizeGrip(self.size_grip)
        self.resize_btn.setStyleSheet("QSizeGrip {width: 10px; height:10px; background-color: rgba(254,211,44,0)}")
        self.ex_search_dialog = None
        self.dragPos = None
        self.full_screen = 0
        self.spawn_coords = QPoint(self.width() // 2, 50)
        self.move(self.spawn_coords)
        self.resize(720, 655)
        self.label.setPixmap(QPixmap('Design/images/img.jpg'))

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
