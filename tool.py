import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QToolBar, QAction
from PyQt5.QtGui import QIcon

import qrc_res


class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle(r"Python Menus & Toolbars")
        self.resize(400, 200)
        self.centralWidget = QLabel('Hello, World')
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._create_menu_bar()
        self._create_tool_bars()

    def _create_menu_bar(self):
        menu_bar = self.menuBar()
        # Creating menus using a QMenu object
        file_menu = QMenu("&File", self)
        file_menu.addAction(self.openAction)
        file_menu.addAction(self.saveAction)
        menu_bar.addMenu(file_menu)
        # Creating menus using a title
        edit_menu = menu_bar.addMenu("&Edit")
        help_menu = menu_bar.addMenu("&Help")

    def _create_tool_bars(self):
        file_tool_bar = self.addToolBar('File')
        file_tool_bar.addAction(self.openAction)
        file_tool_bar.addAction(self.saveAction)
        edit_tool_bar = QToolBar('Edit', self)
        self.addToolBar(edit_tool_bar)

        help_tool_bar = QToolBar('Help', self)
        self.addToolBar(Qt.LeftToolBarArea, help_tool_bar)

    def _createActions(self):
        # File actions
        self.openAction = QAction(QIcon(":add.svg"), "&Add...", self)
        self.saveAction = QAction(QIcon(":help.svg"), "&Help", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

# pyrcc5 -o qrc_resources.py resources.qrc