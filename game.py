# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Game

dictLetters = {
    'dict': Qt.Key_Q,
    'dictionary': 2
}
class Game(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Game()
        self.ui.setupUi(self)

        self.ui.label_Input.setWordWrap(True)
        self.ui.label_Output.setWordWrap(True)

        self.ui.label_Input.setText("Hello World")




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


#        # Получаем текущий текст
#        current_text = self.ui.textEdit_Output.toPlainText()

#        # Проверяем, является ли текущий текст новым
#        if (len(current_text) - 1) == len(self.previous_text):
#            # Откатываем к предыдущему значению
#            self.ui.textEdit_Output.setPlainText(self.previous_text)

#        # Обновляем предыдущий текст
#        self.previous_text = self.ui.textEdit_Output.toPlainText()

    def printText(self, inputText, shift):
        if(shift):
            inputText = inputText.upper()

        # Получаем текущий текст
        old_text = self.ui.label_Output.text()

        # Добавляем текст с поддержкой HTML
        html_text = f"<font color='red'>{inputText}</font>"
        self.ui.label_Output.setText(old_text + html_text)


    def keyPressEvent(self, event):
        # проверка на шифт
        shift = bool(event.modifiers() & Qt.ShiftModifier)

        text = ""
        if(event.key() == Qt.Key_Q):
            self.ui.pushButton_Q.animateClick()
            text = "q"
        elif(event.key() == Qt.Key_W):
            self.ui.pushButton_W.animateClick()
            text = "w"
        elif(event.key() == Qt.Key_E):
            self.ui.pushButton_E.animateClick()
            text = "e"
        elif(event.key() == Qt.Key_R):
            self.ui.pushButton_R.animateClick()
            text = "r"
        elif(event.key() == Qt.Key_T):
            self.ui.pushButton_T.animateClick()
            text = "t"
        elif(event.key() == Qt.Key_Y):
            self.ui.pushButton_Y.animateClick()
            text = "y"
        elif(event.key() == Qt.Key_U):
            self.ui.pushButton_U.animateClick()
            text = "u"
        elif(event.key() == Qt.Key_I):
            self.ui.pushButton_I.animateClick()
            text = "i"
        elif(event.key() == Qt.Key_O):
            self.ui.pushButton_O.animateClick()
            text = "o"
        elif(event.key() == Qt.Key_P):
            self.ui.pushButton_P.animateClick()
            text = "p"


        elif(event.key() == Qt.Key_A):
            self.ui.pushButton_A.animateClick()
            text = "a"
        elif(event.key() == Qt.Key_S):
            self.ui.pushButton_S.animateClick()
            text = "s"
        elif(event.key() == Qt.Key_D):
            self.ui.pushButton_D.animateClick()
            text = "d"
        elif(event.key() == Qt.Key_F):
            self.ui.pushButton_F.animateClick()
            text = "f"
        elif(event.key() == Qt.Key_G):
            self.ui.pushButton_G.animateClick()
            text = "g"
        elif(event.key() == Qt.Key_H):
            self.ui.pushButton_H.animateClick()
            text = "h"
        elif(event.key() == Qt.Key_J):
            self.ui.pushButton_J.animateClick()
            text = "j"
        elif(event.key() == Qt.Key_K):
            self.ui.pushButton_K.animateClick()
            text = "k"
        elif(event.key() == Qt.Key_L):
            self.ui.pushButton_L.animateClick()
            text = "l"


        elif(event.key() == Qt.Key_Z):
            self.ui.pushButton_Z.animateClick()
            text = "z"
        elif(event.key() == Qt.Key_X):
            self.ui.pushButton_X.animateClick()
            text = "x"
        elif(event.key() == Qt.Key_C):
            self.ui.pushButton_C.animateClick()
            text = "c"
        elif(event.key() == Qt.Key_V):
            self.ui.pushButton_V.animateClick()
            text = "v"
        elif(event.key() == Qt.Key_B):
            self.ui.pushButton_B.animateClick()
            text = "b"
        elif(event.key() == Qt.Key_N):
            self.ui.pushButton_N.animateClick()
            text = "n"
        elif(event.key() == Qt.Key_M):
            self.ui.pushButton_M.animateClick()
            text = "m"


        elif(event.key() == Qt.Key_Shift):
            self.ui.pushButton_Shift.animateClick()

        self.printText(text, shift)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Game()
    widget.show()
    sys.exit(app.exec())



