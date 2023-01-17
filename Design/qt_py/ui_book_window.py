# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_book_window(object):
    def setupUi(self, book_window):
        if not book_window.objectName():
            book_window.setObjectName(u"book_window")
        book_window.resize(716, 653)
        book_window.setStyleSheet(u"/* General */\n"
"* {\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	font-size: 16px;\n"
"	outline: none;\n"
"	font-family: \"Arial\";\n"
"}\n"
"\n"
"QFrame {\n"
"	border: none;\n"
"}\n"
"\n"
"#main_body {\n"
"	background-color: rgba(32,36,42,255);\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"#book_info {\n"
"	background-color: rgb(76,79,86);\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"#error_label {\n"
"	margin-top: 15px;\n"
"}\n"
"\n"
"/* Tabs style */\n"
"QTabWidget QLabel {\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"	background: transparent;\n"
"	border: none;\n"
"	overflow: hidden;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background-color: rgb(100,100,116);\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"	width: 200px;\n"
"	height: 35px;\n"
"	padding: 0px 10px;\n"
"	margin: 0 5px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgba(254,211,44,255);\n"
"	color: black;\n"
"}\n"
"\n"
"#tab_background, #tab_backg"
                        "round_2, #tab_background_3 {\n"
"	background-color: rgb(76,79,86);\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"/* Qlabel style */\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"\n"
"#book_title {\n"
"	font-size: 20px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"/* Buttons style */\n"
"QPushButton {\n"
"	background: rgba(254,211,44,255);\n"
"	border-radius: 5px;\n"
"	padding: 0 10px 0 10px;\n"
"	height: 40px;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgba(204,161, 44,255);\n"
"	color: white;\n"
"}\n"
"\n"
"/* Text input style */\n"
"QLineEdit {\n"
"	border-radius: 10%;\n"
"	background-color: rgba(32,36,42,255);\n"
"	color: white;\n"
"	padding-left: 10px;\n"
"	height: 40px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgba(254,211,44,255);\n"
"}\n"
"\n"
"/* ComboBox style */\n"
"QComboBox {\n"
"	border-radius: 10%;\n"
"	background-color: rgba(32,36,42,255);\n"
"	color: white;\n"
"	padding-left: 10px;\n"
"	height: 40px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    border-bottom-left-radius: 0p"
                        "x;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 40px;\n"
"	background-color: rgba(254,211,44,255);\n"
"    border-top-right-radius: 10%;\n"
"    border-bottom-right-radius: 10%;\n"
"}\n"
"\n"
"QComboBox::drop-down:on {\n"
"	border-bottom-left-radius: 0%;\n"
"	border-bottom-right-radius: 0%;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Icons/For_QT/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    image: url(:/Icons/For_QT/chevron-up.svg);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	/* Style of the drop-down list */\n"
"	padding: 10px 5px;\n"
"	color: white;\n"
"    selection-color: black;\n"
"    selection-background-color: rgba(254,211,44,255);\n"
"	font-size: 10pt;\n"
"    box-shadow: transparent;\n"
"	background-color: rgba(32,36,42,255);\n"
"	border-bottom-left-radius: 10%;\n"
"	border-bottom-right-radius: 10%;\n"
"}\n"
"\n"
"/* CheckBox style "
                        "*/\n"
"QCheckBox {\n"
"	color: white;\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/Icons/For_QT/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	\n"
"	image: url(:/Icons/For_QT/check-square.svg);\n"
"}\n"
"\n"
"/* Scroll Area style */\n"
"#scroll_widget {\n"
"	background-color: transparent;\n"
"	overflow: hidden;\n"
"}\n"
"\n"
"QScrollArea, #scroll_area_container {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#scroll_area_content {\n"
"	background-color: rgb(76,79,86);\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"/* TitleBar style */\n"
"#title_bar {\n"
"	background-color: rgb(76,79,86);\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"}\n"
"\n"
"#window_title {\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"#title_bar QPushButton {\n"
"	height: 25px;\n"
"}\n"
"\n"
"#icon {\n"
"	min-width: 25px;\n"
"	min-height: 25px;\n"
"	background: rgba(254,211,44,255);\n"
"	border-radius: 5%;\n"
"}\n"
"\n"
"/* ScrollBar style */\n"
"/* VERTICAL SCR"
                        "OLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: 1px solid rgba(254,211,44,255);\n"
"	background-color: rgba(32,36,42,255);\n"
"    width: 20px;\n"
"	border-radius: 5%;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(76,79,86);\n"
"	min-height: 20px;\n"
"	margin: 20px 0 20px 0;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background: rgba(204,161, 44,255);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgba(254,211,44,255);\n"
"	height: 21px;\n"
"	border-top-left-radius: 3%;\n"
"	border-top-right-radius: 3%;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background: rgba(204,161, 44,255);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: rgba(254,211,44,255);\n"
"	height: 21px;\n"
"	border-bottom-left-radius: 3%;\n"
"	border-bottom-right-radius: 3%;"
                        "\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background: rgba(204,161, 44,255);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	overflow: hidden;\n"
"}\n"
"\n"
"#bbk_text, #udk_text, #isbn_text {\n"
"	max-height: 60px;\n"
"}\n"
"\n"
"#annotation_text {\n"
"	font-size: 14px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(book_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QWidget(book_window)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"/* General */\n"
"* {\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	font-size: 16px;\n"
"	outline: none;\n"
"	font-family: \"Arial\";\n"
"}\n"
"\n"
"QFrame {\n"
"	border: none;\n"
"}\n"
"\n"
"#main_body {\n"
"	background-color: rgba(32,36,42,255);\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"#book_info {\n"
"	background-color: rgb(76,79,86);\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"#error_label {\n"
"	margin-top: 15px;\n"
"}\n"
"\n"
"/* Tabs style */\n"
"QTabWidget QLabel {\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"	background: transparent;\n"
"	border: none;\n"
"	overflow: hidden;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background-color: rgb(100,100,116);\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"	width: 200px;\n"
"	height: 35px;\n"
"	padding: 0px 10px;\n"
"	margin: 0 5px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgba(254,211,44,255);\n"
"	color: black;\n"
"}\n"
"\n"
"#tab_background, #tab_backg"
                        "round_2, #tab_background_3 {\n"
"	background-color: rgb(76,79,86);\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"/* Qlabel style */\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"\n"
"#book_title {\n"
"	font-size: 20px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"/* Buttons style */\n"
"QPushButton {\n"
"	background: rgba(254,211,44,255);\n"
"	border-radius: 5px;\n"
"	padding: 0 10px 0 10px;\n"
"	height: 40px;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgba(204,161, 44,255);\n"
"	color: white;\n"
"}\n"
"\n"
"/* Text input style */\n"
"QLineEdit {\n"
"	border-radius: 10%;\n"
"	background-color: rgba(32,36,42,255);\n"
"	color: white;\n"
"	padding-left: 10px;\n"
"	height: 40px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgba(254,211,44,255);\n"
"}\n"
"\n"
"/* ComboBox style */\n"
"QComboBox {\n"
"	border-radius: 10%;\n"
"	background-color: rgba(32,36,42,255);\n"
"	color: white;\n"
"	padding-left: 10px;\n"
"	height: 40px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    border-bottom-left-radius: 0p"
                        "x;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 40px;\n"
"	background-color: rgba(254,211,44,255);\n"
"    border-top-right-radius: 10%;\n"
"    border-bottom-right-radius: 10%;\n"
"}\n"
"\n"
"QComboBox::drop-down:on {\n"
"	border-bottom-left-radius: 0%;\n"
"	border-bottom-right-radius: 0%;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Icons/For_QT/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    image: url(:/Icons/For_QT/chevron-up.svg);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	/* Style of the drop-down list */\n"
"	padding: 10px 5px;\n"
"	color: white;\n"
"    selection-color: black;\n"
"    selection-background-color: rgba(254,211,44,255);\n"
"	font-size: 10pt;\n"
"    box-shadow: transparent;\n"
"	background-color: rgba(32,36,42,255);\n"
"	border-bottom-left-radius: 10%;\n"
"	border-bottom-right-radius: 10%;\n"
"}\n"
"\n"
"/* CheckBox style "
                        "*/\n"
"QCheckBox {\n"
"	color: white;\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/Icons/For_QT/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	\n"
"	image: url(:/Icons/For_QT/check-square.svg);\n"
"}\n"
"\n"
"/* Scroll Area style */\n"
"#scroll_widget {\n"
"	background-color: transparent;\n"
"	overflow: hidden;\n"
"}\n"
"\n"
"QScrollArea, #scroll_area_container {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#scroll_area_content {\n"
"	background-color: rgb(76,79,86);\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"/* TitleBar style */\n"
"#title_bar {\n"
"	background-color: rgb(76,79,86);\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"}\n"
"\n"
"#window_title {\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"#title_bar QPushButton {\n"
"	height: 25px;\n"
"}\n"
"\n"
"#icon {\n"
"	min-width: 25px;\n"
"	min-height: 25px;\n"
"	background: rgba(254,211,44,255);\n"
"	border-radius: 5%;\n"
"}\n"
"\n"
"/* ScrollBar style */\n"
"/* VERTICAL SCR"
                        "OLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: 1px solid rgba(254,211,44,255);\n"
"	background-color: rgba(32,36,42,255);\n"
"    width: 20px;\n"
"	border-radius: 5%;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(76,79,86);\n"
"	min-height: 20px;\n"
"	margin: 20px 0 20px 0;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background: rgba(204,161, 44,255);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgba(254,211,44,255);\n"
"	height: 21px;\n"
"	border-top-left-radius: 3%;\n"
"	border-top-right-radius: 3%;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background: rgba(204,161, 44,255);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: rgba(254,211,44,255);\n"
"	height: 21px;\n"
"	border-bottom-left-radius: 3%;\n"
"	border-bottom-right-radius: 3%;"
                        "\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background: rgba(204,161, 44,255);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#bbk_text, #udk_text, #isbn_text {\n"
"	max-height: 60px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.main_body)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QWidget(self.main_body)
        self.title_bar.setObjectName(u"title_bar")
        self.horizontalLayout_6 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_5 = QFrame(self.title_bar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.icon = QLabel(self.frame_5)
        self.icon.setObjectName(u"icon")
        self.icon.setPixmap(QPixmap(u":/Icons/For_QT/book.svg"))
        self.icon.setScaledContents(False)
        self.icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.icon)


        self.horizontalLayout_6.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.title_bar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.window_title = QLabel(self.frame_6)
        self.window_title.setObjectName(u"window_title")
        self.window_title.setMinimumSize(QSize(200, 0))

        self.verticalLayout_14.addWidget(self.window_title, 0, Qt.AlignLeft)


        self.horizontalLayout_6.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame_7 = QFrame(self.title_bar)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.min_btn = QPushButton(self.frame_7)
        self.min_btn.setObjectName(u"min_btn")
        self.min_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/For_QT/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon1)
        self.min_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.min_btn)

        self.max_btn = QPushButton(self.frame_7)
        self.max_btn.setObjectName(u"max_btn")
        self.max_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/For_QT/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.max_btn.setIcon(icon2)
        self.max_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.max_btn)

        self.close_btn = QPushButton(self.frame_7)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/For_QT/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.close_btn)


        self.horizontalLayout_6.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.title_bar)

        self.content = QWidget(self.main_body)
        self.content.setObjectName(u"content")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 0)
        self.book_info = QWidget(self.content)
        self.book_info.setObjectName(u"book_info")
        self.verticalLayout_4 = QVBoxLayout(self.book_info)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.heading = QFrame(self.book_info)
        self.heading.setObjectName(u"heading")
        self.heading.setFrameShape(QFrame.StyledPanel)
        self.heading.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.heading)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.image_container = QFrame(self.heading)
        self.image_container.setObjectName(u"image_container")
        self.image_container.setFrameShape(QFrame.StyledPanel)
        self.image_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.image_container)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.image_container)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)


        self.horizontalLayout.addWidget(self.image_container)

        self.small_description = QFrame(self.heading)
        self.small_description.setObjectName(u"small_description")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.small_description.sizePolicy().hasHeightForWidth())
        self.small_description.setSizePolicy(sizePolicy2)
        self.small_description.setFrameShape(QFrame.StyledPanel)
        self.small_description.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.small_description)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.book_title = QLabel(self.small_description)
        self.book_title.setObjectName(u"book_title")
        self.book_title.setFrameShape(QFrame.Box)
        self.book_title.setFrameShadow(QFrame.Plain)
        self.book_title.setLineWidth(1)
        self.book_title.setWordWrap(True)
        self.book_title.setOpenExternalLinks(False)

        self.verticalLayout_8.addWidget(self.book_title)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.row = QFrame(self.small_description)
        self.row.setObjectName(u"row")
        sizePolicy2.setHeightForWidth(self.row.sizePolicy().hasHeightForWidth())
        self.row.setSizePolicy(sizePolicy2)
        self.row.setFrameShape(QFrame.StyledPanel)
        self.row.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.row)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.row)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Arial"])
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.publishings_label = QLabel(self.row)
        self.publishings_label.setObjectName(u"publishings_label")
        sizePolicy2.setHeightForWidth(self.publishings_label.sizePolicy().hasHeightForWidth())
        self.publishings_label.setSizePolicy(sizePolicy2)
        self.publishings_label.setLineWidth(1)
        self.publishings_label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.publishings_label, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.row)

        self.row_3 = QFrame(self.small_description)
        self.row_3.setObjectName(u"row_3")
        sizePolicy2.setHeightForWidth(self.row_3.sizePolicy().hasHeightForWidth())
        self.row_3.setSizePolicy(sizePolicy2)
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.row_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.row_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.year_label = QLabel(self.row_3)
        self.year_label.setObjectName(u"year_label")
        sizePolicy2.setHeightForWidth(self.year_label.sizePolicy().hasHeightForWidth())
        self.year_label.setSizePolicy(sizePolicy2)
        self.year_label.setLineWidth(1)
        self.year_label.setScaledContents(False)
        self.year_label.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.year_label, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.row_3)

        self.row_6 = QFrame(self.small_description)
        self.row_6.setObjectName(u"row_6")
        sizePolicy2.setHeightForWidth(self.row_6.sizePolicy().hasHeightForWidth())
        self.row_6.setSizePolicy(sizePolicy2)
        self.row_6.setFrameShape(QFrame.StyledPanel)
        self.row_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.row_6)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.row_6)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.pages_label = QLabel(self.row_6)
        self.pages_label.setObjectName(u"pages_label")
        sizePolicy2.setHeightForWidth(self.pages_label.sizePolicy().hasHeightForWidth())
        self.pages_label.setSizePolicy(sizePolicy2)
        self.pages_label.setLineWidth(1)
        self.pages_label.setScaledContents(False)
        self.pages_label.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.pages_label, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.row_6)

        self.row_4 = QFrame(self.small_description)
        self.row_4.setObjectName(u"row_4")
        sizePolicy2.setHeightForWidth(self.row_4.sizePolicy().hasHeightForWidth())
        self.row_4.setSizePolicy(sizePolicy2)
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.row_4)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.row_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.type_label = QLabel(self.row_4)
        self.type_label.setObjectName(u"type_label")
        sizePolicy2.setHeightForWidth(self.type_label.sizePolicy().hasHeightForWidth())
        self.type_label.setSizePolicy(sizePolicy2)
        self.type_label.setLineWidth(1)
        self.type_label.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.type_label, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.row_4)

        self.row_5 = QFrame(self.small_description)
        self.row_5.setObjectName(u"row_5")
        sizePolicy2.setHeightForWidth(self.row_5.sizePolicy().hasHeightForWidth())
        self.row_5.setSizePolicy(sizePolicy2)
        self.row_5.setFrameShape(QFrame.StyledPanel)
        self.row_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.row_5)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.row_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.education_lvl_label = QLabel(self.row_5)
        self.education_lvl_label.setObjectName(u"education_lvl_label")
        sizePolicy2.setHeightForWidth(self.education_lvl_label.sizePolicy().hasHeightForWidth())
        self.education_lvl_label.setSizePolicy(sizePolicy2)
        self.education_lvl_label.setLineWidth(1)
        self.education_lvl_label.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.education_lvl_label, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.row_5)

        self.row_2 = QFrame(self.small_description)
        self.row_2.setObjectName(u"row_2")
        sizePolicy2.setHeightForWidth(self.row_2.sizePolicy().hasHeightForWidth())
        self.row_2.setSizePolicy(sizePolicy2)
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.row_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.row_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.authors_label = QLabel(self.row_2)
        self.authors_label.setObjectName(u"authors_label")
        sizePolicy2.setHeightForWidth(self.authors_label.sizePolicy().hasHeightForWidth())
        self.authors_label.setSizePolicy(sizePolicy2)
        self.authors_label.setLineWidth(1)
        self.authors_label.setScaledContents(False)
        self.authors_label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.authors_label, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.row_2)


        self.horizontalLayout.addWidget(self.small_description)

        self.buttons = QFrame(self.heading)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(150, 0))
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.buttons)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.open_library_btn = QPushButton(self.buttons)
        self.open_library_btn.setObjectName(u"open_library_btn")
        self.open_library_btn.setMinimumSize(QSize(0, 50))
        self.open_library_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/For_QT/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_library_btn.setIcon(icon4)
        self.open_library_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.open_library_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.buttons, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.heading)


        self.verticalLayout_3.addWidget(self.book_info, 0, Qt.AlignTop)

        self.big_description = QTabWidget(self.content)
        self.big_description.setObjectName(u"big_description")
        self.big_description.setTabPosition(QTabWidget.North)
        self.big_description.setTabShape(QTabWidget.Rounded)
        self.big_description.setDocumentMode(False)
        self.bibliographic_record = QWidget()
        self.bibliographic_record.setObjectName(u"bibliographic_record")
        self.verticalLayout_7 = QVBoxLayout(self.bibliographic_record)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.tab_background = QWidget(self.bibliographic_record)
        self.tab_background.setObjectName(u"tab_background")
        self.verticalLayout_11 = QVBoxLayout(self.tab_background)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.bibliographic_record_text = QTextBrowser(self.tab_background)
        self.bibliographic_record_text.setObjectName(u"bibliographic_record_text")
        self.bibliographic_record_text.setFont(font)

        self.verticalLayout_11.addWidget(self.bibliographic_record_text)


        self.verticalLayout_7.addWidget(self.tab_background)

        self.big_description.addTab(self.bibliographic_record, "")
        self.annotation = QWidget()
        self.annotation.setObjectName(u"annotation")
        self.verticalLayout_6 = QVBoxLayout(self.annotation)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.tab_background_2 = QWidget(self.annotation)
        self.tab_background_2.setObjectName(u"tab_background_2")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_background_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.annotation_text = QTextBrowser(self.tab_background_2)
        self.annotation_text.setObjectName(u"annotation_text")
        self.annotation_text.setFont(font)
        self.annotation_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.annotation_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.annotation_text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.annotation_text.setOverwriteMode(False)

        self.horizontalLayout_10.addWidget(self.annotation_text)


        self.verticalLayout_6.addWidget(self.tab_background_2)

        self.big_description.addTab(self.annotation, "")
        self.classifiers = QWidget()
        self.classifiers.setObjectName(u"classifiers")
        self.verticalLayout_5 = QVBoxLayout(self.classifiers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.tab_background_3 = QWidget(self.classifiers)
        self.tab_background_3.setObjectName(u"tab_background_3")
        self.verticalLayout_18 = QVBoxLayout(self.tab_background_3)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 20, 10, 10)
        self.row_7 = QFrame(self.tab_background_3)
        self.row_7.setObjectName(u"row_7")
        sizePolicy2.setHeightForWidth(self.row_7.sizePolicy().hasHeightForWidth())
        self.row_7.setSizePolicy(sizePolicy2)
        self.row_7.setFrameShape(QFrame.StyledPanel)
        self.row_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.row_7)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.row_7)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11.setMargin(0)

        self.verticalLayout_15.addWidget(self.label_11)

        self.bbk_text = QTextBrowser(self.row_7)
        self.bbk_text.setObjectName(u"bbk_text")
        self.bbk_text.setMinimumSize(QSize(0, 0))
        self.bbk_text.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_15.addWidget(self.bbk_text)


        self.verticalLayout_18.addWidget(self.row_7, 0, Qt.AlignTop)

        self.row_8 = QFrame(self.tab_background_3)
        self.row_8.setObjectName(u"row_8")
        sizePolicy2.setHeightForWidth(self.row_8.sizePolicy().hasHeightForWidth())
        self.row_8.setSizePolicy(sizePolicy2)
        self.row_8.setFrameShape(QFrame.StyledPanel)
        self.row_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_8)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.row_8)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13.setMargin(0)

        self.verticalLayout_16.addWidget(self.label_13)

        self.udk_text = QTextBrowser(self.row_8)
        self.udk_text.setObjectName(u"udk_text")
        self.udk_text.setMinimumSize(QSize(0, 0))
        self.udk_text.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_16.addWidget(self.udk_text)


        self.verticalLayout_18.addWidget(self.row_8, 0, Qt.AlignTop)

        self.row_9 = QFrame(self.tab_background_3)
        self.row_9.setObjectName(u"row_9")
        sizePolicy2.setHeightForWidth(self.row_9.sizePolicy().hasHeightForWidth())
        self.row_9.setSizePolicy(sizePolicy2)
        self.row_9.setFrameShape(QFrame.StyledPanel)
        self.row_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.row_9)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.row_9)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_15.setMargin(0)

        self.verticalLayout_17.addWidget(self.label_15)

        self.isbn_text = QTextBrowser(self.row_9)
        self.isbn_text.setObjectName(u"isbn_text")
        self.isbn_text.setMinimumSize(QSize(0, 0))
        self.isbn_text.setMaximumSize(QSize(16777215, 60))
        self.isbn_text.setAcceptRichText(True)

        self.verticalLayout_17.addWidget(self.isbn_text)


        self.verticalLayout_18.addWidget(self.row_9, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.tab_background_3)

        self.big_description.addTab(self.classifiers, "")

        self.verticalLayout_3.addWidget(self.big_description)


        self.verticalLayout_2.addWidget(self.content)

        self.size_grip = QFrame(self.main_body)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.size_grip, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.main_body)


        self.retranslateUi(book_window)

        self.big_description.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(book_window)
    # setupUi

    def retranslateUi(self, book_window):
        book_window.setWindowTitle(QCoreApplication.translate("book_window", u"Form", None))
        self.icon.setText("")
        self.window_title.setText(QCoreApplication.translate("book_window", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438", None))
        self.min_btn.setText("")
        self.max_btn.setText("")
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("book_window", u"TextLabel", None))
        self.book_title.setText(QCoreApplication.translate("book_window", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043e\u0447\u0435\u043d\u044c \u0434\u043b\u0438\u043d\u043d\u044b\u043c, \u043d\u043e \u044d\u0442\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0446\u0432\u0435\u0442\u043e\u0447\u043a\u0438", None))
        self.label_9.setText(QCoreApplication.translate("book_window", u"\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e:", None))
        self.publishings_label.setText(QCoreApplication.translate("book_window", u"\u041e\u0447\u0435\u043d\u044c \u0434\u043b\u0438\u043d\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u043a\u043e\u0433\u043e-\u0442\u043e \u0438\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("book_window", u"\u0413\u043e\u0434 \u0438\u0437\u0434\u0430\u043d\u0438\u044f:", None))
        self.year_label.setText(QCoreApplication.translate("book_window", u"2004", None))
        self.label_6.setText(QCoreApplication.translate("book_window", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446:", None))
        self.pages_label.setText(QCoreApplication.translate("book_window", u"457", None))
        self.label_4.setText(QCoreApplication.translate("book_window", u"\u0412\u0438\u0434 \u0438\u0437\u0434\u0430\u043d\u0438\u044f:", None))
        self.type_label.setText(QCoreApplication.translate("book_window", u"\u0423\u0447\u0435\u0431\u043d\u043e\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("book_window", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.education_lvl_label.setText(QCoreApplication.translate("book_window", u"\u0411\u0430\u043a\u0430\u043b\u0430\u0432\u0440", None))
        self.label_2.setText(QCoreApplication.translate("book_window", u"\u0410\u0432\u0442\u043e\u0440\u044b:", None))
        self.authors_label.setText(QCoreApplication.translate("book_window", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418. \u041e., \u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418. \u041e., \u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418. \u041e., \u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418. \u041e., \u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418. \u041e.", None))
        self.open_library_btn.setText(QCoreApplication.translate("book_window", u" \u0412 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0443", None))
        self.bibliographic_record_text.setHtml(QCoreApplication.translate("book_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">\u0411\u043e\u043d\u0434\u0430\u0440\u0435\u0432\u0430, \u041e. \u0410. \u0425\u0443\u0434\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u043a\u0435\u0440\u0430\u043c\u0438\u043a\u0430 / \u041e. \u0410. \u0411\u043e\u043d\u0434\u0430\u0440\u0435\u0432\u0430. - \u041c\u043e\u0441\u043a\u0432\u0430 : \u0414\u0438\u0440\u0435\u043a\u0442-\u041c\u0435\u0434\u0438\u0430, 2019. - 51 \u0441. - ISBN 978-5-4475-9919-5. - \u0422\u0435\u043a\u0441\u0442 : \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u0439. "
                        "- URL: https://znanium.com/catalog/product/1964094 (\u0434\u0430\u0442\u0430 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f: 13.01.2023). \u2013 \u0420\u0435\u0436\u0438\u043c \u0434\u043e\u0441\u0442\u0443\u043f\u0430: \u043f\u043e \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0435.</span></p></body></html>", None))
        self.big_description.setTabText(self.big_description.indexOf(self.bibliographic_record), QCoreApplication.translate("book_window", u"\u0411\u0438\u0431\u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.annotation_text.setHtml(QCoreApplication.translate("book_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:14px; font-weight:296; color:#ffffff; background-color:transparent;\">\u0423\u0447\u0435\u0431\u043d\u043e-\u043c\u0435\u0442\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u0435 \u00ab\u0425\u0443\u0434\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u043a\u0435\u0440\u0430\u043c\u0438\u043a\u0430\u00bb \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u043e \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438"
                        "\u0438 \u0441 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u0439 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043c\u043e\u0434\u0443\u043b\u044f \u00ab\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u043e-\u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c\u00bb, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0447\u0430\u0441\u0442\u044c\u044e \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0439 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 \u0424\u0413\u041e\u0421 \u0421\u041f"
                        "\u041e \u043f\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 54.02.02 \u00ab\u0414\u0435\u043a\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u043e-\u043f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u043e\u0435 \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u043e \u0438 \u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0435 \u043f\u0440\u043e\u043c\u044b\u0441\u043b\u044b\u00bb (\u043f\u043e \u0432\u0438\u0434\u0430\u043c). \u0412 \u043f\u043e\u0441\u043e\u0431\u0438\u0438 \u0443\u0434\u0435\u043b\u0435\u043d\u043e \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c \u044d\u0442\u0430\u043f\u0430\u043c \u0440\u0430\u0431\u043e\u0442\u044b: \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0435 \u0433\u043b\u0438\u043d\u044b, \u0442\u0435\u0445\u043d\u0438\u043a\u0430\u043c \u043b\u0435\u043f\u043a\u0438, \u0432\u0438\u0434\u0430\u043c \u0438 \u0441\u043f\u043e\u0441\u043e\u0431\u0430\u043c \u043d\u0430\u043d\u0435\u0441\u0435\u043d\u0438\u044f"
                        " \u0434\u0435\u043a\u043e\u0440\u0430, \u043e\u0431\u0436\u0438\u0433\u0443 \u0438\u0437\u0434\u0435\u043b\u0438\u0439, \u0430 \u0442\u0430\u043a\u0436\u0435 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u044b \u0442\u0435\u043c\u044b \u0438\u0442\u043e\u0433\u043e\u0432\u044b\u0445 \u0437\u0430\u0434\u0430\u043d\u0438\u0439 \u0438 \u0437\u0430\u0434\u0430\u043d\u0438\u044f \u043a \u043d\u0438\u043c. \u0422\u0430\u043a\u0436\u0435 \u0432 \u043f\u043e\u0441\u043e\u0431\u0438\u0438 \u0434\u0430\u044e\u0442\u0441\u044f \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0433\u043b\u0438\u043d\u0435, \u043c\u0435\u0442\u043e\u0434\u0430\u0445 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u0438 \u0444\u043e\u0440\u043c\u043e\u0432\u0430\u043d\u0438\u044f \u0433\u043b\u0438\u043d\u044f\u043d\u044b\u0445 \u043c\u0430\u0441\u0441, \u0441\u0443\u0448\u043a\u0435, \u043e\u0431\u0436\u0438\u0433\u0435 \u0438 \u0432\u0438\u0434\u0430\u0445 \u0434\u0435\u043a\u043e\u0440\u0438\u0440\u043e\u0432"
                        "\u0430\u043d\u0438\u044f. \u0420\u0430\u0441\u0441\u043c\u0430\u0442\u0440\u0438\u0432\u0430\u044e\u0442\u0441\u044f \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0432\u0438\u0434\u044b \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f, \u043f\u0440\u0438\u0432\u0435\u0434\u0435\u043d\u044b \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e\u0431 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u0445 \u0432\u0438\u0434\u0430\u0445 \u043a\u0435\u0440\u0430\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432 \u0438 \u0442\u0435\u0445\u043d\u0438\u043a, \u0441 \u043e\u0441\u043d\u043e\u0432\u0430\u043c\u0438 \u0444\u0438\u0437\u0438\u043a\u043e-\u0445\u0438\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0435\u0432\u0440\u0430\u0449\u0435\u043d\u0438\u0439, \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u044f\u0449\u0438\u0445 \u0441 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430\u043c\u0438 \u0432 \u043f\u0440"
                        "\u043e\u0446\u0435\u0441\u0441\u0435 \u043e\u0431\u0436\u0438\u0433\u0430, \u043f\u0440\u0438\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u043e-\u043e\u0446\u0435\u043d\u043e\u0447\u043d\u044b\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b \u043f\u043e \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0435. \u0423\u0447\u0435\u0431\u043d\u043e-\u043c\u0435\u0442\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u0435 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043e \u0434\u043b\u044f \u0440\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0434\u0438\u0441- \u0446\u0438\u043f\u043b\u0438\u043d\u044b \u00ab\u0425\u0443\u0434\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u043a\u0435\u0440\u0430\u043c\u0438\u043a\u0430\u00bb \u0432 \u043a\u043e\u043b\u043b\u0435\u0434\u0436\u0430\u0445 \u043a"
                        "\u0443\u043b\u044c\u0442\u0443\u0440\u044b \u0438 \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u0430. \u041e\u043d\u043e \u0442\u0430\u043a\u0436\u0435 \u043c\u043e\u0436\u0435\u0442 \u043f\u043e\u043c\u043e\u0447\u044c \u043e\u0431\u0443\u0447\u0430\u044e\u0449\u0438\u043c\u0441\u044f \u043f\u043e\u043b\u043d\u0435\u0435 \u0440\u0430\u0441\u043a\u0440\u044b\u0442\u044c \u0441\u0432\u043e\u0438 \u0442\u0432\u043e\u0440\u0447\u0435\u0441\u043a\u0438\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438. \u041f\u043e\u0441\u043e\u0431\u0438\u0435 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u043e\u043b\u0435\u0437\u043d\u043e \u0434\u043b\u044f \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0438 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432 \u043a\u043e\u043b\u043b\u0435\u0434\u0436\u0435\u0439 \u043a\u0443\u043b\u044c\u0442\u0443\u0440\u044b \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u00ab"
                        "\u0414\u0435\u043a\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u043e-\u043f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u043e\u0435 \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u043e \u0438 \u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0435 \u043f\u0440\u043e\u043c\u044b\u0441\u043b\u044b\u00bb \u0438 \u043f\u0435\u0434\u0430\u0433\u043e\u0433\u0430\u043c \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u0434\u0435\u0442\u0435\u0439 \u0438 \u0432\u0437\u0440\u043e\u0441\u043b\u044b\u0445. \u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0447\u0430\u0442\u0430\u0435\u0442\u0441\u044f \u0432 \u0430\u0432\u0442\u043e\u0440\u0441\u043a\u043e\u0439 \u0440\u0435\u0434\u0430\u043a\u0446\u0438\u0438.</span></p></body></html>", None))
        self.big_description.setTabText(self.big_description.indexOf(self.annotation), QCoreApplication.translate("book_window", u"\u0410\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("book_window", u"\u041d\u043e\u043c\u0435\u0440 \u0411\u0411\u041a:", None))
        self.bbk_text.setHtml(QCoreApplication.translate("book_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">\u041e\u0447\u0435\u043d\u044c \u0434\u043b\u0438\u043d\u043d\u044b\u0439 \u0438 \u043d\u0435\u043f\u043e\u043d\u044f\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0411\u0411\u041a</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("book_window", u"\u041d\u043e\u043c\u0435\u0440 \u0423\u0414\u041a:", None))
        self.udk_text.setHtml(QCoreApplication.translate("book_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">\u041e\u0447\u0435\u043d\u044c \u0434\u043b\u0438\u043d\u043d\u044b\u0439 \u0438 \u043d\u0435\u043f\u043e\u043d\u044f\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0423\u0414\u041a</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("book_window", u"\u041d\u043e\u043c\u0435\u0440 ISBN:", None))
        self.isbn_text.setHtml(QCoreApplication.translate("book_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">\u041e\u0447\u0435\u043d\u044c \u0434\u043b\u0438\u043d\u043d\u044b\u0439 \u0438 \u043d\u0435\u043f\u043e\u043d\u044f\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 ISBN</span></p></body></html>", None))
        self.big_description.setTabText(self.big_description.indexOf(self.classifiers), QCoreApplication.translate("book_window", u"\u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b", None))
    # retranslateUi

