# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex_search_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_ex_search_window(object):
    def setupUi(self, ex_search_window):
        if not ex_search_window.objectName():
            ex_search_window.setObjectName(u"ex_search_window")
        ex_search_window.resize(607, 622)
        ex_search_window.setMinimumSize(QSize(607, 622))
        ex_search_window.setMaximumSize(QSize(607, 622))
        ex_search_window.setStyleSheet(u"/* General */\n"
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
"#error_label {\n"
"	margin-top: 15px;\n"
"}\n"
"\n"
"#inputs_area {\n"
"	background-color: rgb(76,79,86);\n"
"	border-radius: 10%;\n"
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
"/* Buttons style */\n"
"QPushButton {\n"
"	backgro"
                        "und: rgba(254,211,44,255);\n"
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
"    border-top-right-radius: 10%;\n"
"    border-bottom-right-radius:"
                        " 10%;\n"
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
"	image: url(:/Icons/For_QT/check-square.svg);\n"
"}\n"
"\n"
"/* Scroll Area style */\n"
""
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
"Q"
                        "ScrollBar::handle:vertical:hover{	\n"
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
"QScrollBar::add-page:vertical, QScrollBar::sub-page:verti"
                        "cal {\n"
"	background: none;\n"
"}\n"
"\n"
"/* Dialog buttons style */\n"
"#buttons QPushButton {\n"
"	width: 100px;\n"
"}")
        self.verticalLayout = QVBoxLayout(ex_search_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QWidget(ex_search_window)
        self.main_body.setObjectName(u"main_body")
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

        self.close_btn = QPushButton(self.frame_7)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/For_QT/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.close_btn)


        self.horizontalLayout_6.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.title_bar, 0, Qt.AlignTop)

        self.content = QWidget(self.main_body)
        self.content.setObjectName(u"content")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 0)
        self.inputs_area = QWidget(self.content)
        self.inputs_area.setObjectName(u"inputs_area")
        self.verticalLayout_4 = QVBoxLayout(self.inputs_area)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.inputs_area)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.input = QFrame(self.frame)
        self.input.setObjectName(u"input")
        self.input.setFrameShape(QFrame.StyledPanel)
        self.input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.input)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.input)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.string_input = QLineEdit(self.input)
        self.string_input.setObjectName(u"string_input")
        self.string_input.setMinimumSize(QSize(435, 0))

        self.horizontalLayout.addWidget(self.string_input)


        self.verticalLayout_5.addWidget(self.input)

        self.input_1 = QFrame(self.frame)
        self.input_1.setObjectName(u"input_1")
        self.input_1.setFrameShape(QFrame.StyledPanel)
        self.input_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.input_1)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.in_headings = QCheckBox(self.input_1)
        self.in_headings.setObjectName(u"in_headings")

        self.horizontalLayout_10.addWidget(self.in_headings, 0, Qt.AlignLeft)

        self.in_annotation = QCheckBox(self.input_1)
        self.in_annotation.setObjectName(u"in_annotation")

        self.horizontalLayout_10.addWidget(self.in_annotation, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.input_1)


        self.verticalLayout_4.addWidget(self.frame)

        self.input_2 = QFrame(self.inputs_area)
        self.input_2.setObjectName(u"input_2")
        self.input_2.setFrameShape(QFrame.StyledPanel)
        self.input_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.input_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.input_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.publishings_combobox = QComboBox(self.input_2)
        self.publishings_combobox.setObjectName(u"publishings_combobox")
        self.publishings_combobox.setMinimumSize(QSize(435, 0))

        self.horizontalLayout_2.addWidget(self.publishings_combobox)


        self.verticalLayout_4.addWidget(self.input_2)

        self.input_3 = QFrame(self.inputs_area)
        self.input_3.setObjectName(u"input_3")
        self.input_3.setFrameShape(QFrame.StyledPanel)
        self.input_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.input_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.input_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.author_input = QLineEdit(self.input_3)
        self.author_input.setObjectName(u"author_input")
        self.author_input.setMinimumSize(QSize(435, 0))

        self.horizontalLayout_3.addWidget(self.author_input)


        self.verticalLayout_4.addWidget(self.input_3)

        self.input_4 = QFrame(self.inputs_area)
        self.input_4.setObjectName(u"input_4")
        self.input_4.setFrameShape(QFrame.StyledPanel)
        self.input_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.input_4)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.input_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.year_input = QLineEdit(self.input_4)
        self.year_input.setObjectName(u"year_input")
        self.year_input.setMinimumSize(QSize(435, 0))

        self.horizontalLayout_4.addWidget(self.year_input)


        self.verticalLayout_4.addWidget(self.input_4)

        self.input_5 = QFrame(self.inputs_area)
        self.input_5.setObjectName(u"input_5")
        self.input_5.setFrameShape(QFrame.StyledPanel)
        self.input_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.input_5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.input_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.isbn_input = QLineEdit(self.input_5)
        self.isbn_input.setObjectName(u"isbn_input")
        self.isbn_input.setMinimumSize(QSize(435, 0))

        self.horizontalLayout_5.addWidget(self.isbn_input)


        self.verticalLayout_4.addWidget(self.input_5)

        self.input_6 = QFrame(self.inputs_area)
        self.input_6.setObjectName(u"input_6")
        self.input_6.setFrameShape(QFrame.StyledPanel)
        self.input_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.input_6)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.input_6)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.udk_combobox = QComboBox(self.input_6)
        self.udk_combobox.setObjectName(u"udk_combobox")
        self.udk_combobox.setMinimumSize(QSize(435, 0))

        self.horizontalLayout_8.addWidget(self.udk_combobox)


        self.verticalLayout_4.addWidget(self.input_6)

        self.input_7 = QFrame(self.inputs_area)
        self.input_7.setObjectName(u"input_7")
        self.input_7.setFrameShape(QFrame.StyledPanel)
        self.input_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.input_7)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.input_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.bbk_combobox = QComboBox(self.input_7)
        self.bbk_combobox.setObjectName(u"bbk_combobox")
        self.bbk_combobox.setMinimumSize(QSize(435, 0))

        self.horizontalLayout_9.addWidget(self.bbk_combobox)


        self.verticalLayout_4.addWidget(self.input_7)

        self.input_8 = QFrame(self.inputs_area)
        self.input_8.setObjectName(u"input_8")
        self.input_8.setFrameShape(QFrame.StyledPanel)
        self.input_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.input_8)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.input_8)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.type_combobox = QComboBox(self.input_8)
        self.type_combobox.setObjectName(u"type_combobox")
        self.type_combobox.setMinimumSize(QSize(435, 0))

        self.horizontalLayout_11.addWidget(self.type_combobox)


        self.verticalLayout_4.addWidget(self.input_8)

        self.buttons = QDialogButtonBox(self.inputs_area)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttons.setCenterButtons(True)

        self.verticalLayout_4.addWidget(self.buttons)


        self.verticalLayout_3.addWidget(self.inputs_area)


        self.verticalLayout_2.addWidget(self.content)

        self.size_grip = QFrame(self.main_body)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.size_grip, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.main_body)


        self.retranslateUi(ex_search_window)
        self.buttons.accepted.connect(ex_search_window.accept)
        self.buttons.rejected.connect(ex_search_window.reject)

        QMetaObject.connectSlotsByName(ex_search_window)
    # setupUi

    def retranslateUi(self, ex_search_window):
        ex_search_window.setWindowTitle(QCoreApplication.translate("ex_search_window", u"Dialog", None))
        self.icon.setText("")
        self.window_title.setText(QCoreApplication.translate("ex_search_window", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.min_btn.setText("")
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("ex_search_window", u"\u0418\u0441\u043a\u043e\u043c\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430:", None))
        self.in_headings.setText(QCoreApplication.translate("ex_search_window", u"\u0418\u0441\u043a\u0430\u0442\u044c \u0432 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0438", None))
        self.in_annotation.setText(QCoreApplication.translate("ex_search_window", u"\u0418\u0441\u043a\u0430\u0442\u044c \u0432 \u0430\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("ex_search_window", u"\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e:", None))
        self.label_3.setText(QCoreApplication.translate("ex_search_window", u"\u0410\u0432\u0442\u043e\u0440\u044b:", None))
        self.author_input.setText("")
        self.label_4.setText(QCoreApplication.translate("ex_search_window", u"\u0413\u043e\u0434 \u0438\u0437\u0434\u0430\u043d\u0438\u044f: ", None))
        self.year_input.setText("")
        self.label_5.setText(QCoreApplication.translate("ex_search_window", u"\u041d\u043e\u043c\u0435\u0440 ISBN:", None))
        self.isbn_input.setText("")
        self.label_6.setText(QCoreApplication.translate("ex_search_window", u"\u041d\u043e\u043c\u0435\u0440 \u0423\u0414\u041a:", None))
        self.label_7.setText(QCoreApplication.translate("ex_search_window", u"\u041d\u043e\u043c\u0435\u0440 \u0411\u0411\u041a:", None))
        self.label_8.setText(QCoreApplication.translate("ex_search_window", u"\u0412\u0438\u0434 \u043f\u043e\u0441\u043e\u0431\u0438\u044f:", None))
    # retranslateUi

