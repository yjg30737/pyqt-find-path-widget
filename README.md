# pyqt-find-path-widget
PyQt find path widget (QLabel - QLineEdit - QPushButton)

This widget's theme is dark.

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-find-path-widget.git --upgrade```

## Included Packages
* <a href="pyqt-resource-helper">https://github.com/yjg30737/pyqt-resource-helper.git</a>

## Feature
* ```findClicked``` Signal will be emitted when find button clicks
* ```added``` Signal will be emitted when file's name is set in the QLineEdit
* "Open path" feature in context menu
* Showing tooltip to show full path when QLineEdit is too short to do so
* QLineEdit is set to read only in order to prevent malfunction from wrong input.
* Being able to use ```setLabel(label: str)``` method to set the label. Label doesn't exist as default.

## Example
```python
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser
from pyqt_find_path_widget import FindPathWidget


class FindPathWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        findPathWidget = FindPathWidget()
        findPathWidget.setExtOfFiles('Text Files (*.txt)') # Restrict file's extension to find

        findPathWidget.findClicked.connect(self.__findClicked) # Signal will be emitted when find button clicks
        findPathWidget.added.connect(self.__added) # Signal will be emitted when file's name is set in the QLineEdit

        self.__textBrowser = QTextBrowser() # Widget to show text file's content
        self.__textBrowser.setStyleSheet('QTextBrowser '
                                          '{'
                                          'color: #DDD;'
                                          'background-color: #444;'
                                          'border: 1px solid #222;'
                                          '}') # To match the style with FindPathWidget

        self.setStyleSheet('QWidget { background-color: #666; }') # To match the style with FindPathWidget

        lay = QVBoxLayout()
        lay.addWidget(findPathWidget)
        lay.addWidget(self.__textBrowser)

        self.setLayout(lay)

    def __findClicked(self):
        print('find clicked')

    def __added(self, filename):
        f = open(filename, 'r')
        text = f.read()
        f.close()
        self.__textBrowser.setText(text)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    searchMultiple = FindPathWidgetExample()
    searchMultiple.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/147036534-e8624abd-c5dc-4838-b6bc-4dc961499c43.png)

Mouse cursor should be next to that tooltip. Windows screenshot feature doesn't show the mouse cursor.
