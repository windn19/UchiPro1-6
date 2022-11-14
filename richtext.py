from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("QTextEdit")
        self.resize(300, 270)

        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("Button 1")
        self.btnPress2 = QPushButton("Button 2")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btn_press1_clicked)
        self.btnPress2.clicked.connect(self.btn_press2_clicked)

    def btn_press1_clicked(self):
        self.textEdit.insertPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

    def btn_press2_clicked(self):
        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
