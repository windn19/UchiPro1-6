import sys

from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication, QVBoxLayout, QLabel, QDesktopWidget)

# Определите класс для создания формы с несколькими флажками


class MultipleCheckbox(QWidget):
    def __init__(self):
        super().__init__()
        # Установите текст метки для пользователя
        lb = QLabel('Выберите свою любимую еду(ы):', self)
        lb.setGeometry(20, 20, 100, 20)
        lb.move(20, 20)
        # Создайте три флажка
        cb1 = QCheckBox('Шоколадный торт', self)
        cb1.move(20, 70)
        cb1.stateChanged.connect(lambda: self.Selected_Value(cb1))
        cb2 = QCheckBox('Мороженое', self)
        cb2.move(20, 90)
        cb2.stateChanged.connect(lambda: self.Selected_Value(cb2))
        cb3 = QCheckBox('Макароны', self)
        cb3.move(20, 110)
        cb3.stateChanged.connect(lambda: self.Selected_Value(cb3))
        self.label = QLabel('Ничего не выбрано')
        self.label.move(20, 150)
        # Установить вертикальную планировку интервала QT
        vbox = QVBoxLayout()
        vbox.addWidget(lb)
        vbox.addWidget(cb1)
        vbox.addWidget(cb2)
        vbox.addWidget(cb3)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.setWindowTitle('Форма с несколькими флажками')
        self.setGeometry(60, 60, 350, 200)
        self.lblText = ''
        # Отображение окна в центре экрана
        win = self.frameGeometry()
        pos = QDesktopWidget().availableGeometry().center()
        win.moveCenter(pos)
        self.move(win.topLeft())
        self.show()

# Определите функцию для чтения входных данных пользователя

    def Selected_Value(self, btn):
        if self.lblText != '':
            str = self.lblText
            strArray = str.split(',')
            self.lblText = ''
            for val in strArray:
                if btn.text() != val:
                    if self.lblText == '':
                        self.lblText = val
                    else:
                        self.lblText += ',' + val
        if btn.isChecked():
            if self.lblText == '':
                self.lblText = btn.text()
            else:
                self.lblText += ',' + btn.text()
        else:
            if btn.isChecked():
                if self.lblText == '':
                    self.lblText = btn.text()
                else:
                    self.lblText += ',' + btn.text()
        self.label.setText('Вы выбрали \n' + self.lblText)

# Создайте объект приложения и выполните его


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MultipleCheckbox()
    sys.exit(app.exec_())
