# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_card.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)
import resources_rc


class Ui_book_card(object):
    def setupUi(self, book_card):
        if not book_card.objectName():
            book_card.setObjectName(u"book_card")
        book_card.resize(990, 268)
        book_card.setMinimumSize(QSize(989, 241))
        book_card.setMaximumSize(QSize(16777215, 300))
        book_card.setStyleSheet(u"/* General */\n"
                                "* {\n"
                                "	margin: 0;\n"
                                "	padding: 0;\n"
                                "	font-size: 18px;\n"
                                "	outline: none;\n"
                                "}\n"
                                "\n"
                                "QFrame {\n"
                                "	border: none;\n"
                                "}\n"
                                "\n"
                                "#main_body {\n"
                                "	border-radius: 10%;\n"
                                "	background-color: rgb(32, 36, 42);\n"
                                "}\n"
                                "\n"
                                "#image_container {\n"
                                "	width: 5em;\n"
                                "	height: 5em;\n"
                                "	background-color: rgb(76,79,86);\n"
                                "	border-radius: 10%;\n"
                                "}\n"
                                "\n"
                                "/* Qlabel style */\n"
                                "QLabel {\n"
                                "	color: white;\n"
                                "}\n"
                                "\n"
                                "#heading_label {\n"
                                "	font-size: 22px;\n"
                                "	font-weight: 500;\n"
                                "}\n"
                                "\n"
                                "/* Buttons style */\n"
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
                                "}")
        self.verticalLayout = QVBoxLayout(book_card)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QWidget(book_card)
        self.main_body.setObjectName(u"main_body")
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_container = QWidget(self.main_body)
        self.image_container.setObjectName(u"image_container")
        self.image_container.setMinimumSize(QSize(250, 250))
        self.image_container.setMaximumSize(QSize(400, 400))
        self.verticalLayout_4 = QVBoxLayout(self.image_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.image_container)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(6546545, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout.addWidget(self.image_container, 0, Qt.AlignLeft)

        self.description = QFrame(self.main_body)
        self.description.setObjectName(u"description")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy1)
        self.description.setFrameShape(QFrame.StyledPanel)
        self.description.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.description)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 5, 0, 10)
        self.frame_5 = QFrame(self.description)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.heading_label = QLabel(self.frame_5)
        self.heading_label.setObjectName(u"heading_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.heading_label.sizePolicy().hasHeightForWidth())
        self.heading_label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setBold(True)
        self.heading_label.setFont(font)
        self.heading_label.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.heading_label)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.description)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.description)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.description)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame = QFrame(self.description)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.description)

        self.buttons = QFrame(self.main_body)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.buttons)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_2 = QPushButton(self.buttons)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/For_QT/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.open_btn = QPushButton(self.buttons)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/For_QT/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_btn.setIcon(icon1)
        self.open_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.open_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout.addWidget(self.buttons, 0, Qt.AlignRight)

        self.verticalLayout.addWidget(self.main_body)

        self.retranslateUi(book_card)

        QMetaObject.connectSlotsByName(book_card)

    # setupUi

    def retranslateUi(self, book_card):
        book_card.setWindowTitle(QCoreApplication.translate("book_card", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("book_card", u"TextLabel", None))
        self.heading_label.setText(QCoreApplication.translate("book_card",
                                                              u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043e\u0447\u0435\u043d\u044c \u0434\u043d\u0438\u043d\u043d\u044b\u043c, \u043d\u043e \u044d\u0442\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0446\u0432\u0435\u0442\u043e\u0447\u043a\u0438",
                                                              None))
        self.label_5.setText(
            QCoreApplication.translate("book_card", u"\u0413\u043e\u0434 \u0438\u0437\u0434\u0430\u043d\u0438\u044f:",
                                       None))
        self.label_6.setText(QCoreApplication.translate("book_card", u"2021", None))
        self.label_9.setText(
            QCoreApplication.translate("book_card", u"\u0422\u0438\u043f \u0438\u0437\u0434\u0430\u043d\u0438\u044f:",
                                       None))
        self.label_10.setText(QCoreApplication.translate("book_card",
                                                         u"\u0443\u0447\u0435\u0431\u043d\u043e\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u0435",
                                                         None))
        self.label_7.setText(QCoreApplication.translate("book_card",
                                                        u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0440\u0430\u043d\u0438\u0446:",
                                                        None))
        self.label_8.setText(QCoreApplication.translate("book_card", u"223", None))
        self.label_4.setText(QCoreApplication.translate("book_card", u"\u0410\u0432\u0442\u043e\u0440\u044b:", None))
        self.label_3.setText(
            QCoreApplication.translate("book_card", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418. \u041e.",
                                       None))
        self.pushButton_2.setText(
            QCoreApplication.translate("book_card", u" \u041e\u0442\u0440\u044b\u0442\u044c", None))
        self.open_btn.setText(QCoreApplication.translate("book_card",
                                                         u"  \u0412 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0443",
                                                         None))
    # retranslateUi