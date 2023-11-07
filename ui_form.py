# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Game(object):
    def setupUi(self, Game):
        if not Game.objectName():
            Game.setObjectName(u"Game")
        Game.resize(816, 544)
        self.label = QLabel(Game)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 50, 231, 111))
        self.widget = QWidget(Game)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 330, 801, 51))
        font = QFont()
        font.setPointSize(13)
        self.widget.setFont(font)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_W = QPushButton(self.widget)
        self.pushButton_W.setObjectName(u"pushButton_W")
        self.pushButton_W.setMinimumSize(QSize(45, 40))
        self.pushButton_W.setMaximumSize(QSize(45, 40))
        self.pushButton_W.setFont(font)

        self.gridLayout.addWidget(self.pushButton_W, 0, 2, 1, 1)

        self.pushButton_Y = QPushButton(self.widget)
        self.pushButton_Y.setObjectName(u"pushButton_Y")
        self.pushButton_Y.setMinimumSize(QSize(45, 40))
        self.pushButton_Y.setMaximumSize(QSize(45, 40))
        self.pushButton_Y.setFont(font)

        self.gridLayout.addWidget(self.pushButton_Y, 0, 6, 1, 1)

        self.pushButton_P = QPushButton(self.widget)
        self.pushButton_P.setObjectName(u"pushButton_P")
        self.pushButton_P.setMinimumSize(QSize(45, 40))
        self.pushButton_P.setMaximumSize(QSize(45, 40))
        self.pushButton_P.setFont(font)

        self.gridLayout.addWidget(self.pushButton_P, 0, 10, 1, 1)

        self.pushButton_E = QPushButton(self.widget)
        self.pushButton_E.setObjectName(u"pushButton_E")
        self.pushButton_E.setMinimumSize(QSize(45, 40))
        self.pushButton_E.setMaximumSize(QSize(45, 40))
        self.pushButton_E.setFont(font)

        self.gridLayout.addWidget(self.pushButton_E, 0, 3, 1, 1)

        self.pushButton_TAB = QPushButton(self.widget)
        self.pushButton_TAB.setObjectName(u"pushButton_TAB")
        self.pushButton_TAB.setMinimumSize(QSize(60, 40))
        self.pushButton_TAB.setMaximumSize(QSize(60, 40))

        self.gridLayout.addWidget(self.pushButton_TAB, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(45, 40))
        self.pushButton_7.setMaximumSize(QSize(45, 40))
        self.pushButton_7.setFont(font)

        self.gridLayout.addWidget(self.pushButton_7, 0, 7, 1, 1)

        self.pushButton_T = QPushButton(self.widget)
        self.pushButton_T.setObjectName(u"pushButton_T")
        self.pushButton_T.setMinimumSize(QSize(45, 40))
        self.pushButton_T.setMaximumSize(QSize(45, 40))
        self.pushButton_T.setFont(font)

        self.gridLayout.addWidget(self.pushButton_T, 0, 5, 1, 1)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(45, 40))
        self.pushButton_9.setMaximumSize(QSize(45, 40))
        self.pushButton_9.setFont(font)

        self.gridLayout.addWidget(self.pushButton_9, 0, 9, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(45, 40))
        self.pushButton_8.setMaximumSize(QSize(45, 40))
        self.pushButton_8.setFont(font)

        self.gridLayout.addWidget(self.pushButton_8, 0, 8, 1, 1)

        self.pushButton_Q = QPushButton(self.widget)
        self.pushButton_Q.setObjectName(u"pushButton_Q")
        self.pushButton_Q.setMinimumSize(QSize(45, 40))
        self.pushButton_Q.setMaximumSize(QSize(45, 40))
        self.pushButton_Q.setFont(font)

        self.gridLayout.addWidget(self.pushButton_Q, 0, 1, 1, 1)

        self.pushButton_41 = QPushButton(self.widget)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(45, 40))
        self.pushButton_41.setMaximumSize(QSize(45, 40))
        self.pushButton_41.setFont(font)

        self.gridLayout.addWidget(self.pushButton_41, 0, 11, 1, 1)

        self.pushButton_42 = QPushButton(self.widget)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(45, 40))
        self.pushButton_42.setMaximumSize(QSize(45, 40))
        self.pushButton_42.setFont(font)

        self.gridLayout.addWidget(self.pushButton_42, 0, 12, 1, 1)

        self.pushButton_R = QPushButton(self.widget)
        self.pushButton_R.setObjectName(u"pushButton_R")
        self.pushButton_R.setMinimumSize(QSize(45, 40))
        self.pushButton_R.setMaximumSize(QSize(45, 40))
        self.pushButton_R.setFont(font)

        self.gridLayout.addWidget(self.pushButton_R, 0, 4, 1, 1)

        self.pushButton_Enther = QPushButton(self.widget)
        self.pushButton_Enther.setObjectName(u"pushButton_Enther")
        self.pushButton_Enther.setMinimumSize(QSize(100, 40))
        self.pushButton_Enther.setMaximumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.pushButton_Enther, 0, 13, 1, 1)

        self.widget_2 = QWidget(Game)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 380, 741, 51))
        self.widget_2.setFont(font)
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_37 = QPushButton(self.widget_2)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(45, 40))
        self.pushButton_37.setMaximumSize(QSize(45, 40))
        self.pushButton_37.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_37, 0, 10, 1, 1)

        self.pushButton_32 = QPushButton(self.widget_2)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(45, 40))
        self.pushButton_32.setMaximumSize(QSize(45, 40))
        self.pushButton_32.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_32, 0, 7, 1, 1)

        self.pushButton_36 = QPushButton(self.widget_2)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(45, 40))
        self.pushButton_36.setMaximumSize(QSize(45, 40))
        self.pushButton_36.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_36, 0, 6, 1, 1)

        self.pushButton_38 = QPushButton(self.widget_2)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(45, 40))
        self.pushButton_38.setMaximumSize(QSize(45, 40))
        self.pushButton_38.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_38, 0, 9, 1, 1)

        self.pushButton_31 = QPushButton(self.widget_2)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(45, 40))
        self.pushButton_31.setMaximumSize(QSize(45, 40))
        self.pushButton_31.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_31, 0, 2, 1, 1)

        self.pushButton_33 = QPushButton(self.widget_2)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(45, 40))
        self.pushButton_33.setMaximumSize(QSize(45, 40))
        self.pushButton_33.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_33, 0, 12, 1, 1)

        self.pushButton_44 = QPushButton(self.widget_2)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(45, 40))
        self.pushButton_44.setMaximumSize(QSize(45, 40))
        self.pushButton_44.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_44, 0, 13, 1, 1)

        self.pushButton_43 = QPushButton(self.widget_2)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMinimumSize(QSize(45, 40))
        self.pushButton_43.setMaximumSize(QSize(45, 40))
        self.pushButton_43.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_43, 0, 3, 1, 1)

        self.pushButton_40 = QPushButton(self.widget_2)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(45, 40))
        self.pushButton_40.setMaximumSize(QSize(45, 40))
        self.pushButton_40.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_40, 0, 5, 1, 1)

        self.pushButton_35 = QPushButton(self.widget_2)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(45, 40))
        self.pushButton_35.setMaximumSize(QSize(45, 40))
        self.pushButton_35.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_35, 0, 8, 1, 1)

        self.pushButton_39 = QPushButton(self.widget_2)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(45, 40))
        self.pushButton_39.setMaximumSize(QSize(45, 40))
        self.pushButton_39.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_39, 0, 1, 1, 1)

        self.pushButton_F = QPushButton(self.widget_2)
        self.pushButton_F.setObjectName(u"pushButton_F")
        self.pushButton_F.setMinimumSize(QSize(45, 40))
        self.pushButton_F.setMaximumSize(QSize(45, 40))
        self.pushButton_F.setFont(font)

        self.gridLayout_4.addWidget(self.pushButton_F, 0, 4, 1, 1)

        self.pushButton_CapsLock = QPushButton(self.widget_2)
        self.pushButton_CapsLock.setObjectName(u"pushButton_CapsLock")
        self.pushButton_CapsLock.setMinimumSize(QSize(90, 40))
        self.pushButton_CapsLock.setMaximumSize(QSize(90, 40))

        self.gridLayout_4.addWidget(self.pushButton_CapsLock, 0, 0, 1, 1)

        self.widget_3 = QWidget(Game)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 430, 801, 51))
        self.widget_3.setFont(font)
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_52 = QPushButton(self.widget_3)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setMinimumSize(QSize(45, 40))
        self.pushButton_52.setMaximumSize(QSize(45, 40))
        self.pushButton_52.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_52, 0, 5, 1, 1)

        self.pushButton_55 = QPushButton(self.widget_3)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setMinimumSize(QSize(45, 40))
        self.pushButton_55.setMaximumSize(QSize(45, 40))
        self.pushButton_55.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_55, 0, 4, 1, 1)

        self.pushButton_51 = QPushButton(self.widget_3)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMinimumSize(QSize(45, 40))
        self.pushButton_51.setMaximumSize(QSize(45, 40))
        self.pushButton_51.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_51, 0, 3, 1, 1)

        self.pushButton_46 = QPushButton(self.widget_3)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMinimumSize(QSize(45, 40))
        self.pushButton_46.setMaximumSize(QSize(45, 40))
        self.pushButton_46.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_46, 0, 6, 1, 1)

        self.pushButton_45 = QPushButton(self.widget_3)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(45, 40))
        self.pushButton_45.setMaximumSize(QSize(45, 40))
        self.pushButton_45.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_45, 0, 7, 1, 1)

        self.pushButton_50 = QPushButton(self.widget_3)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(45, 40))
        self.pushButton_50.setMaximumSize(QSize(45, 40))
        self.pushButton_50.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_50, 0, 10, 1, 1)

        self.pushButton_54 = QPushButton(self.widget_3)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setMinimumSize(QSize(45, 40))
        self.pushButton_54.setMaximumSize(QSize(45, 40))
        self.pushButton_54.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_54, 0, 1, 1, 1)

        self.pushButton_53 = QPushButton(self.widget_3)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(45, 40))
        self.pushButton_53.setMaximumSize(QSize(45, 40))
        self.pushButton_53.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_53, 0, 8, 1, 1)

        self.pushButton_57 = QPushButton(self.widget_3)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setMinimumSize(QSize(120, 40))
        self.pushButton_57.setMaximumSize(QSize(120, 40))

        self.gridLayout_5.addWidget(self.pushButton_57, 0, 0, 1, 1)

        self.pushButton_47 = QPushButton(self.widget_3)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(45, 40))
        self.pushButton_47.setMaximumSize(QSize(45, 40))
        self.pushButton_47.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_47, 0, 9, 1, 1)

        self.pushButton_48 = QPushButton(self.widget_3)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(45, 40))
        self.pushButton_48.setMaximumSize(QSize(45, 40))
        self.pushButton_48.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton_48, 0, 2, 1, 1)

        self.pushButton_58 = QPushButton(self.widget_3)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setMinimumSize(QSize(120, 40))
        self.pushButton_58.setMaximumSize(QSize(120, 40))

        self.gridLayout_5.addWidget(self.pushButton_58, 0, 11, 1, 1)

        self.widget_4 = QWidget(Game)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 480, 801, 51))
        self.widget_4.setFont(font)
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_62 = QPushButton(self.widget_4)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setMinimumSize(QSize(45, 40))
        self.pushButton_62.setMaximumSize(QSize(45, 40))
        self.pushButton_62.setFont(font)

        self.gridLayout_6.addWidget(self.pushButton_62, 0, 5, 1, 1)

        self.pushButton_64 = QPushButton(self.widget_4)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setMinimumSize(QSize(45, 40))
        self.pushButton_64.setMaximumSize(QSize(45, 40))
        self.pushButton_64.setFont(font)

        self.gridLayout_6.addWidget(self.pushButton_64, 0, 1, 1, 1)

        self.pushButton_68 = QPushButton(self.widget_4)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setMinimumSize(QSize(120, 40))
        self.pushButton_68.setMaximumSize(QSize(120, 40))

        self.gridLayout_6.addWidget(self.pushButton_68, 0, 0, 1, 1)

        self.pushButton_67 = QPushButton(self.widget_4)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMinimumSize(QSize(45, 40))
        self.pushButton_67.setMaximumSize(QSize(45, 40))
        self.pushButton_67.setFont(font)

        self.gridLayout_6.addWidget(self.pushButton_67, 0, 2, 1, 1)

        self.pushButton_61 = QPushButton(self.widget_4)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setMinimumSize(QSize(400, 40))
        self.pushButton_61.setMaximumSize(QSize(300, 40))
        self.pushButton_61.setFont(font)

        self.gridLayout_6.addWidget(self.pushButton_61, 0, 3, 1, 1)

        self.pushButton_65 = QPushButton(self.widget_4)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setMinimumSize(QSize(45, 40))
        self.pushButton_65.setMaximumSize(QSize(45, 40))
        self.pushButton_65.setFont(font)

        self.gridLayout_6.addWidget(self.pushButton_65, 0, 6, 1, 1)

        self.pushButton_66 = QPushButton(self.widget_4)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setMinimumSize(QSize(45, 40))
        self.pushButton_66.setMaximumSize(QSize(45, 40))
        self.pushButton_66.setFont(font)

        self.gridLayout_6.addWidget(self.pushButton_66, 0, 7, 1, 1)


        self.retranslateUi(Game)

        QMetaObject.connectSlotsByName(Game)
    # setupUi

    def retranslateUi(self, Game):
        Game.setWindowTitle(QCoreApplication.translate("Game", u"Game", None))
        self.label.setText(QCoreApplication.translate("Game", u"TextLabel", None))
        self.pushButton_W.setText(QCoreApplication.translate("Game", u"W", None))
        self.pushButton_Y.setText(QCoreApplication.translate("Game", u"Y", None))
        self.pushButton_P.setText(QCoreApplication.translate("Game", u"P", None))
        self.pushButton_E.setText(QCoreApplication.translate("Game", u"E", None))
        self.pushButton_TAB.setText(QCoreApplication.translate("Game", u"Tab", None))
        self.pushButton_7.setText(QCoreApplication.translate("Game", u"U", None))
        self.pushButton_T.setText(QCoreApplication.translate("Game", u"T", None))
        self.pushButton_9.setText(QCoreApplication.translate("Game", u"O", None))
        self.pushButton_8.setText(QCoreApplication.translate("Game", u"I", None))
        self.pushButton_Q.setText(QCoreApplication.translate("Game", u"Q", None))
        self.pushButton_41.setText(QCoreApplication.translate("Game", u"[\n"
"{", None))
        self.pushButton_42.setText(QCoreApplication.translate("Game", u"]\n"
"}", None))
        self.pushButton_R.setText(QCoreApplication.translate("Game", u"R", None))
        self.pushButton_Enther.setText(QCoreApplication.translate("Game", u"Enter", None))
        self.pushButton_37.setText(QCoreApplication.translate("Game", u";\n"
":", None))
        self.pushButton_32.setText(QCoreApplication.translate("Game", u"J", None))
        self.pushButton_36.setText(QCoreApplication.translate("Game", u"H", None))
        self.pushButton_38.setText(QCoreApplication.translate("Game", u"L", None))
        self.pushButton_31.setText(QCoreApplication.translate("Game", u"S", None))
        self.pushButton_33.setText(QCoreApplication.translate("Game", u"'\n"
"\"", None))
        self.pushButton_44.setText(QCoreApplication.translate("Game", u"\\\n"
"|", None))
        self.pushButton_43.setText(QCoreApplication.translate("Game", u"D", None))
        self.pushButton_40.setText(QCoreApplication.translate("Game", u"G", None))
        self.pushButton_35.setText(QCoreApplication.translate("Game", u"K", None))
        self.pushButton_39.setText(QCoreApplication.translate("Game", u"A", None))
        self.pushButton_F.setText(QCoreApplication.translate("Game", u"F", None))
        self.pushButton_CapsLock.setText(QCoreApplication.translate("Game", u"Caps Lock", None))
        self.pushButton_52.setText(QCoreApplication.translate("Game", u"B", None))
        self.pushButton_55.setText(QCoreApplication.translate("Game", u"V", None))
        self.pushButton_51.setText(QCoreApplication.translate("Game", u"C", None))
        self.pushButton_46.setText(QCoreApplication.translate("Game", u"N", None))
        self.pushButton_45.setText(QCoreApplication.translate("Game", u"M", None))
        self.pushButton_50.setText(QCoreApplication.translate("Game", u"/", None))
        self.pushButton_54.setText(QCoreApplication.translate("Game", u"Z", None))
        self.pushButton_53.setText(QCoreApplication.translate("Game", u"<", None))
        self.pushButton_57.setText(QCoreApplication.translate("Game", u"Shift", None))
        self.pushButton_47.setText(QCoreApplication.translate("Game", u">", None))
        self.pushButton_48.setText(QCoreApplication.translate("Game", u"X", None))
        self.pushButton_58.setText(QCoreApplication.translate("Game", u"Shift", None))
        self.pushButton_62.setText(QCoreApplication.translate("Game", u"Alt", None))
        self.pushButton_64.setText(QCoreApplication.translate("Game", u"Start", None))
        self.pushButton_68.setText(QCoreApplication.translate("Game", u"Ctrl", None))
        self.pushButton_67.setText(QCoreApplication.translate("Game", u"Alt", None))
        self.pushButton_61.setText(QCoreApplication.translate("Game", u"Space", None))
        self.pushButton_65.setText(QCoreApplication.translate("Game", u"Start", None))
        self.pushButton_66.setText(QCoreApplication.translate("Game", u"Ctrl", None))
    # retranslateUi

