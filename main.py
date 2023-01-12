from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from Design.qt_py import ui_main_window, ui_book_card


class MainWindow(QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Библиотека')
        self.close_btn.clicked.connect(self.close)
        self.max_btn.clicked.connect(self.showMaximized)
        self.min_btn.clicked.connect(self.showMinimized)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.error_label.setText('')
        for i in range(10):
            self.scroll_layout.addWidget(BookCard())


class BookCard(QWidget, ui_book_card.Ui_book_card):
    def __init__(self):
        super(BookCard, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
