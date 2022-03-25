from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QFileDialog, QLabel, QApplication
from pyqt_resource_helper import PyQtResourceHelper

from pyqt_find_path_widget.findPathLineEdit import FindPathLineEdit


class FindPathWidget(QWidget):
    findClicked = pyqtSignal()
    added = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__ext_of_files = ''
        self.__initUi()

    def __initUi(self):
        self.__pathLineEdit = FindPathLineEdit()

        self.__pathFindBtn = QPushButton('Find...')

        PyQtResourceHelper.setStyleSheet([self.__pathLineEdit, self.__pathFindBtn],
                                         ['style/lineedit.css', 'style/button.css'])

        self.__pathFindBtn.clicked.connect(self.__find)

        self.__pathLineEdit.setMaximumHeight(self.__pathFindBtn.sizeHint().height())

        lay = QHBoxLayout()
        lay.addWidget(self.__pathLineEdit)
        lay.addWidget(self.__pathFindBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

    def setLabel(self, text):
        self.layout().insertWidget(0, QLabel(text))

    def setExtOfFiles(self, ext_of_files):
        self.__ext_of_files = ext_of_files

    def getLineEdit(self):
        return self.__pathLineEdit

    def getButton(self):
        return self.__pathFindBtn

    def getFileName(self):
        return self.__pathLineEdit.text()

    def setCustomFind(self, f: bool):
        if f:
            self.__pathFindBtn.clicked.disconnect(self.__find)
            self.__pathFindBtn.clicked.connect(self.__customFind)

    def __customFind(self):
        self.findClicked.emit()

    def __find(self):
        str_exp_files_to_open = self.__ext_of_files if self.__ext_of_files else 'All Files (*.*)'
        filename = QFileDialog.getOpenFileName(self, 'Find', '', str_exp_files_to_open)
        if filename[0]:
            filename = filename[0]
            self.__pathLineEdit.setText(filename)
            self.added.emit(filename)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = FindPathWidget()
    ex.show()
    sys.exit(app.exec_())

