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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Game(object):
    def setupUi(self, Game):
        if not Game.objectName():
            Game.setObjectName(u"Game")
        Game.resize(800, 600)
        self.pushButton_F = QPushButton(Game)
        self.pushButton_F.setObjectName(u"pushButton_F")
        self.pushButton_F.setGeometry(QRect(200, 160, 80, 23))
        self.label = QLabel(Game)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 0, 231, 111))

        self.retranslateUi(Game)

        QMetaObject.connectSlotsByName(Game)
    # setupUi

    def retranslateUi(self, Game):
        Game.setWindowTitle(QCoreApplication.translate("Game", u"Game", None))
        self.pushButton_F.setText(QCoreApplication.translate("Game", u"F", None))
        self.label.setText(QCoreApplication.translate("Game", u"TextLabel", None))
    # retranslateUi

