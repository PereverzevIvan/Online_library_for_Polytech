# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
                               QTabWidget, QVBoxLayout, QWidget)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1175, 720)
        MainWindow.setStyleSheet(u"/* General */\n"
                                 "* {\n"
                                 "	margin: 0;\n"
                                 "	padding: 0;\n"
                                 "	font-size: 18px;\n"
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
                                 "	border_radius: 10%;\n"
                                 "}\n"
                                 "\n"
                                 "#search_background, #ex_search_background, #sort_background {\n"
                                 "	background-color: rgb(76,79,86);\n"
                                 "	border-radius: 10%;\n"
                                 "}\n"
                                 "\n"
                                 "#error_label {\n"
                                 "	margin-top: 15px;\n"
                                 "}\n"
                                 "\n"
                                 "/* Tabs style */\n"
                                 "QTabWidget::pane {\n"
                                 "	background: transparent;\n"
                                 "	border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar {\n"
                                 "	qproperty-drawBase: 0;\n"
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
                                 "/* Qlabel style */\n"
                                 "QLabel {\n"
                                 "	color: white;\n"
                                 "}\n"
                                 "\n"
                                 "/* "
                                 "Buttons style */\n"
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
                                 "    border-bottom-left-radius: 0px;\n"
                                 "    border-bottom-right-radius: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down {\n"
                                 "    subcontrol-origin: padding;\n"
                                 "    subcontrol-position: top right;\n"
                                 "    width: 40px;\n"
                                 "	background-color: rgba(254,211,44,255);\n"
                                 "    border-top-right-r"
                                 "adius: 10%;\n"
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
                                 "/* CheckBox style */\n"
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
                                 "	image: url(:/Icons/For_QT/check-square"
                                 ".svg);\n"
                                 "}\n"
                                 "\n"
                                 "/* Scroll Area style */\n"
                                 "#scroll_widget {\n"
                                 "	background-color: transparent;\n"
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
                                 "/* VERTICAL SCROLLBAR */\n"
                                 " QScrollBar:vertical {\n"
                                 "	border: none;\n"
                                 "	background-color: rgba(32,36,42,255);\n"
                                 "    width: 20px;\n"
                                 "	border-radius: 0px;\n"
                                 " }\n"
                                 "\n"
                                 "/*  HANDLE BAR VERTICAL */\n"
                                 "QScrollBar::handle:vertical {	\n"
                                 "	background-color: rgb(76,79,86);\n"
                                 "	min-height: 20px;\n"
                                 "	margin: 20px 0 20px 0;\n"
                                 "}\n"
                                 "QScrollBar::handle:v"
                                 "ertical:hover{	\n"
                                 "	background: rgba(204,161, 44,255);\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN TOP - SCROLLBAR */\n"
                                 "QScrollBar::sub-line:vertical {\n"
                                 "	border: none;\n"
                                 "	background: rgba(254,211,44,255);\n"
                                 "	height: 20px;\n"
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
                                 "	height: 20px;\n"
                                 "	border-bottom-left-radius: 3%;\n"
                                 "	border-bottom-right-radius: 3%;\n"
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
                                 "	backgrou"
                                 "nd: none;\n"
                                 "}")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setMinimumSize(QSize(1083, 663))
        self.central_widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QWidget(self.central_widget)
        self.main_body.setObjectName(u"main_body")
        self.verticalLayout_2 = QVBoxLayout(self.main_body)
        self.verticalLayout_2.setSpacing(10)
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

        self.verticalLayout_2.addWidget(self.title_bar, 0, Qt.AlignTop)

        self.widget = QWidget(self.main_body)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_15 = QVBoxLayout(self.widget)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.instrumental_menu = QWidget(self.widget)
        self.instrumental_menu.setObjectName(u"instrumental_menu")
        self.verticalLayout_3 = QVBoxLayout(self.instrumental_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tab_menu = QTabWidget(self.instrumental_menu)
        self.tab_menu.setObjectName(u"tab_menu")
        self.search_tab = QWidget()
        self.search_tab.setObjectName(u"search_tab")
        self.verticalLayout_4 = QVBoxLayout(self.search_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.search_background = QWidget(self.search_tab)
        self.search_background.setObjectName(u"search_background")
        self.verticalLayout_9 = QVBoxLayout(self.search_background)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 0, 10, 10)
        self.frame = QFrame(self.search_background)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.search_input = QLineEdit(self.frame)
        self.search_input.setObjectName(u"search_input")

        self.horizontalLayout.addWidget(self.search_input)

        self.verticalLayout_9.addWidget(self.frame)

        self.search_btn = QPushButton(self.search_background)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/For_QT/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon4)
        self.search_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.search_btn, 0, Qt.AlignRight)

        self.verticalLayout_4.addWidget(self.search_background)

        self.tab_menu.addTab(self.search_tab, "")
        self.ex_search_tab = QWidget()
        self.ex_search_tab.setObjectName(u"ex_search_tab")
        self.verticalLayout_7 = QVBoxLayout(self.ex_search_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.ex_search_background = QWidget(self.ex_search_tab)
        self.ex_search_background.setObjectName(u"ex_search_background")
        self.verticalLayout_10 = QVBoxLayout(self.ex_search_background)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.frame_2 = QFrame(self.ex_search_background)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ex_search_status = QLabel(self.frame_2)
        self.ex_search_status.setObjectName(u"ex_search_status")

        self.horizontalLayout_3.addWidget(self.ex_search_status)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.ex_search_inputs = QLabel(self.frame_2)
        self.ex_search_inputs.setObjectName(u"ex_search_inputs")

        self.horizontalLayout_4.addWidget(self.ex_search_inputs)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalLayout_10.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.ex_search_background)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ex_search_params_btn = QPushButton(self.frame_3)
        self.ex_search_params_btn.setObjectName(u"ex_search_params_btn")
        self.ex_search_params_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/For_QT/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ex_search_params_btn.setIcon(icon5)
        self.ex_search_params_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.ex_search_params_btn)

        self.ex_search_btn = QPushButton(self.frame_3)
        self.ex_search_btn.setObjectName(u"ex_search_btn")
        self.ex_search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ex_search_btn.setIcon(icon4)
        self.ex_search_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.ex_search_btn)

        self.verticalLayout_10.addWidget(self.frame_3, 0, Qt.AlignRight)

        self.verticalLayout_7.addWidget(self.ex_search_background)

        self.tab_menu.addTab(self.ex_search_tab, "")
        self.sort_tab = QWidget()
        self.sort_tab.setObjectName(u"sort_tab")
        self.verticalLayout_8 = QVBoxLayout(self.sort_tab)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 0)
        self.sort_background = QWidget(self.sort_tab)
        self.sort_background.setObjectName(u"sort_background")
        self.verticalLayout_11 = QVBoxLayout(self.sort_background)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.frame_4 = QFrame(self.sort_background)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.sort_params = QComboBox(self.frame_4)
        self.sort_params.addItem("")
        self.sort_params.addItem("")
        self.sort_params.addItem("")
        self.sort_params.addItem("")
        self.sort_params.addItem("")
        self.sort_params.addItem("")
        self.sort_params.addItem("")
        self.sort_params.addItem("")
        self.sort_params.setObjectName(u"sort_params")
        self.sort_params.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.sort_params)

        self.verticalLayout_11.addWidget(self.frame_4)

        self.checkBox = QCheckBox(self.sort_background)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox.setIconSize(QSize(25, 25))
        self.checkBox.setChecked(False)

        self.verticalLayout_11.addWidget(self.checkBox, 0, Qt.AlignLeft)

        self.sort_btn = QPushButton(self.sort_background)
        self.sort_btn.setObjectName(u"sort_btn")
        self.sort_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/For_QT/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sort_btn.setIcon(icon6)
        self.sort_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.sort_btn, 0, Qt.AlignRight)

        self.verticalLayout_8.addWidget(self.sort_background)

        self.tab_menu.addTab(self.sort_tab, "")

        self.verticalLayout_3.addWidget(self.tab_menu)

        self.verticalLayout_15.addWidget(self.instrumental_menu, 0, Qt.AlignTop)

        self.error_label = QLabel(self.widget)
        self.error_label.setObjectName(u"error_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy3)
        self.error_label.setLineWidth(1)
        self.error_label.setWordWrap(True)
        self.error_label.setMargin(0)
        self.error_label.setIndent(-1)

        self.verticalLayout_15.addWidget(self.error_label, 0, Qt.AlignBottom)

        self.scroll_widget = QWidget(self.widget)
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.verticalLayout_12 = QVBoxLayout(self.scroll_widget)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 10, 0)
        self.scroll_area = QScrollArea(self.scroll_widget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_container = QWidget()
        self.scroll_area_container.setObjectName(u"scroll_area_container")
        self.scroll_area_container.setGeometry(QRect(0, 0, 1145, 424))
        self.verticalLayout_5 = QVBoxLayout(self.scroll_area_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.scroll_area_content = QWidget(self.scroll_area_container)
        self.scroll_area_content.setObjectName(u"scroll_area_content")
        self.verticalLayout_16 = QVBoxLayout(self.scroll_area_content)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_16.addLayout(self.scroll_layout)

        self.verticalLayout_5.addWidget(self.scroll_area_content)

        self.scroll_area.setWidget(self.scroll_area_container)

        self.verticalLayout_12.addWidget(self.scroll_area)

        self.verticalLayout_15.addWidget(self.scroll_widget)

        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        self.tab_menu.setCurrentIndex(0)
        self.sort_params.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.window_title.setText(
            QCoreApplication.translate("MainWindow", u"\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430",
                                       None))
        self.min_btn.setText("")
        self.max_btn.setText("")
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438:",
                                                      None))
        self.search_input.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                        u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438",
                                                                        None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u" \u041d\u0430\u0439\u0442\u0438", None))
        self.tab_menu.setTabText(self.tab_menu.indexOf(self.search_tab),
                                 QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.ex_search_status.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0441\u043a\u0430 \u043d\u0435 \u0437\u0430\u0434\u0430\u043d\u044b",
                                                                 None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043e \u043f\u043e\u043b\u0435\u0439:",
                                                        None))
        self.ex_search_inputs.setText(
            QCoreApplication.translate("MainWindow", u"0 \u043f\u043e\u043b\u0435\u0439", None))
        self.ex_search_params_btn.setText(QCoreApplication.translate("MainWindow",
                                                                     u"  \u0417\u0430\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b",
                                                                     None))
        self.ex_search_btn.setText(QCoreApplication.translate("MainWindow", u" \u041d\u0430\u0439\u0442\u0438", None))
        self.tab_menu.setTabText(self.tab_menu.indexOf(self.ex_search_tab), QCoreApplication.translate("MainWindow",
                                                                                                       u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a",
                                                                                                       None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e:",
                                                        None))
        self.sort_params.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                   u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438",
                                                                   None))
        self.sort_params.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.sort_params.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.sort_params.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.sort_params.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.sort_params.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.sort_params.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.sort_params.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))

        self.sort_params.setCurrentText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438",
                                                                   None))
        self.sort_params.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                       u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043a\u0438",
                                                                       None))
        self.checkBox.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e",
                                       None))
        self.sort_btn.setText(QCoreApplication.translate("MainWindow",
                                                         u" \u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                                         None))
        self.tab_menu.setTabText(self.tab_menu.indexOf(self.sort_tab), QCoreApplication.translate("MainWindow",
                                                                                                  u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430",
                                                                                                  None))
        self.error_label.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u0417\u0434\u0435\u0441\u044c \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431 \u043e\u0448\u0438\u0431\u043a\u0435",
                                                            None))
    # retranslateUi
