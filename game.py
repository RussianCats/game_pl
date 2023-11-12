# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

from ui_form import Ui_Game


level1 = "Hello World"
level2 = "My name is Sema Romanov. I am eight.\nI am a pupil. I am a pupil of the second form. I live in Cheb."
level3 = "Sema Romanov is a passionate individual with a knack for humor and creativity.\nKnown for his love of crafting memes,\nSema has the unique ability to turn everyday moments into laughter-inducing, shareable content.\nHis witty captions and clever combinations of images make his memes stand out in the digital landscape."

class Game(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Game()
        self.ui.setupUi(self)
        self.level = ""


        # счетчик букв
        self.counterLatters = 0
        # счетик ошибок
        self.counterMistakes = 0

        self.ui.pushButton_level1.clicked.connect(self.on_button_clicked_level1)
        self.ui.pushButton_level2.clicked.connect(self.on_button_clicked_level2)
        self.ui.pushButton_level3.clicked.connect(self.on_button_clicked_level3)

    def on_button_clicked_level1(self):
        self.level = level1
        self.ui.label_Input.setText(self.level)
        self.clearData()

    def on_button_clicked_level2(self):
        self.level = level2
        self.ui.label_Input.setText(self.level)
        self.clearData()

    def on_button_clicked_level3(self):
        self.level = level3
        self.ui.label_Input.setText(self.level)
        self.clearData()

    def clearData(self):
        self.counterLatters = 0
        self.counterMistakes = 0
        self.ui.label_Output.setText("")


    def textChanged(self):
        # Эта функция будет вызываться при изменении текста
        new_text = self.ui.textEdit_Output.toPlainText()
        print(f"Новый текст: {new_text}")

        #Получаем текущий текст
        current_text = self.ui.textEdit_Output.toPlainText()
        current_textHtml = self.ui.textEdit_Output.toHtml()

        if(current_text[-1] == "N"):
            new_html_text = '<span style="color: red;">несколько красных символов</span>'
            self.ui.textEdit_Output.setHtml(current_textHtml[:-1] + new_html_text)




    def printText(self, inputText, shift):

        if(shift):
            inputText = inputText.upper()

        # Получаем текущий текст
        old_text = self.ui.label_Output.text()


        # Добавляем текст с поддержкой HTML
        if(self.level[self.counterLatters - 1] == inputText):
            html_text = f"<font color='black'>{inputText}</font>"
            self.ui.label_Output.setText(old_text + html_text.replace('\n', '<br>'))
        else:
            html_text = f"<font color='red'>{inputText}</font>"
            self.ui.label_Output.setText(old_text + html_text.replace('\n', '<br>'))
            print("mistake: " + str(self.counterLatters))


    def keyPressEvent(self, event):
        # проверка на шифт
        shift = bool(event.modifiers() & Qt.ShiftModifier)

        text = ""
        if(event.key() == Qt.Key_Q):
            self.ui.pushButton_Q.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "q"
        elif(event.key() == Qt.Key_W):
            self.ui.pushButton_W.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "w"
        elif(event.key() == Qt.Key_E):
            self.ui.pushButton_E.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "e"
        elif(event.key() == Qt.Key_R):
            self.ui.pushButton_R.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "r"
        elif(event.key() == Qt.Key_T):
            self.ui.pushButton_T.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "t"
        elif(event.key() == Qt.Key_Y):
            self.ui.pushButton_Y.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "y"
        elif(event.key() == Qt.Key_U):
            self.ui.pushButton_U.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "u"
        elif(event.key() == Qt.Key_I):
            self.ui.pushButton_I.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "i"
        elif(event.key() == Qt.Key_O):
            self.ui.pushButton_O.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "o"
        elif(event.key() == Qt.Key_P):
            self.ui.pushButton_P.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "p"


        elif(event.key() == Qt.Key_A):
            self.ui.pushButton_A.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "a"
        elif(event.key() == Qt.Key_S):
            self.ui.pushButton_S.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "s"
        elif(event.key() == Qt.Key_D):
            self.ui.pushButton_D.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "d"
        elif(event.key() == Qt.Key_F):
            self.ui.pushButton_F.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "f"
        elif(event.key() == Qt.Key_G):
            self.ui.pushButton_G.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "g"
        elif(event.key() == Qt.Key_H):
            self.ui.pushButton_H.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "h"
        elif(event.key() == Qt.Key_J):
            self.ui.pushButton_J.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "j"
        elif(event.key() == Qt.Key_K):
            self.ui.pushButton_K.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "k"
        elif(event.key() == Qt.Key_L):
            self.ui.pushButton_L.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "l"


        elif(event.key() == Qt.Key_Z):
            self.ui.pushButton_Z.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "z"
        elif(event.key() == Qt.Key_X):
            self.ui.pushButton_X.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "x"
        elif(event.key() == Qt.Key_C):
            self.ui.pushButton_C.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "c"
        elif(event.key() == Qt.Key_V):
            self.ui.pushButton_V.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "v"
        elif(event.key() == Qt.Key_B):
            self.ui.pushButton_B.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "b"
        elif(event.key() == Qt.Key_N):
            self.ui.pushButton_N.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "n"
        elif(event.key() == Qt.Key_M):
            self.ui.pushButton_M.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "m"

        elif(event.key() == Qt.Key_Period):
            self.ui.pushButton_Point.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "."
        elif(event.key() == Qt.Key_Comma):
            self.ui.pushButton_comma1.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = ","
        elif(event.key() == Qt.Key_Return):
            self.ui.pushButton_Enther.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = "\n"
            shift = False


        elif(event.key() == Qt.Key_Shift):
            self.ui.pushButton_Shift.animateClick()

        elif(event.key() == Qt.Key_Space):
            self.ui.pushButton_Space.animateClick()
            self.counterLatters = 1 + self.counterLatters
            text = " "


        #  вызывает печать буквы
        self.printText(text, shift)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Подключаем обработчик событий клавиатуры ко всему приложению
    widget = Game()
    widget.show()
    sys.exit(app.exec())



