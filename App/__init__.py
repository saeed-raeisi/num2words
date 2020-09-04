import re
import sys
import designer
from PyQt5 import QtWidgets
from App.convert2per import convert2per
from PyQt5.QtWidgets import (QPushButton, QApplication, QDialog, QLabel)


# build ui
# pyuic5 form.ui -o designer.py

class create_ui(QtWidgets.QMainWindow, designer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(create_ui, self).__init__(parent)
        self.text = self.findChild(QtWidgets.QTextEdit, 'input_text')
        self.setupUi(self)


def main():
    print("------------start----------")
    app = QApplication(sys.argv)
    form = create_ui()
    form.setFixedSize(form.size())

    # error dialog
    def showdialog():
        dialog = QDialog()

        def close():
            dialog.close()

        btn = QPushButton("باشه", dialog)
        lable = QLabel(" Enter integer\n عدد را صحیح وارد کنید ", dialog)
        lable.move(20, 20)
        btn.move(50, 70)
        btn.clicked.connect(close)
        dialog.setWindowTitle("اخطار")
        dialog.exec_()

    # button click
    def play_btn():
        if len(str(form.input_text.toPlainText())) > 15:
            form.input_text.setText("")
            showdialog()
        try:
            output = ""
            # 545345345435345
            val = int(form.input_text.toPlainText())
            form.input_text.setText("")
            output = convert2per(val).get_result()
            # print(output)
            flag = len(output)
            flag = flag / 40 + 1
            for j in range(int(flag)):
                res = [i.start() for i in re.finditer('و', output)]
                for ii in res:

                    temp =(j + 1) * 45
                    if temp - ii <= 5:
                        output = output[:ii] + "\n " + output[ii:]
                        break
            print(output)
            form.output.setText(" "+output)
            # form.output.adjustSize()

            print("  input : " + str(val))
        except ValueError:
            showdialog()

    form.play_button.clicked.connect(play_btn)
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
