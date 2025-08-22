# PyQt5 layouts

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self )
        label2 = QLabel("#2", self )
        label3 = QLabel("#3", self )
        label4 = QLabel("#4", self )
        label5 = QLabel("#5", self )

        label1.setStyleSheet("Background-color: red;")
        label2.setStyleSheet("Background-color: blue;")
        label3.setStyleSheet("Background-color: green;")
        label4.setStyleSheet("Background-color: indigo;")
        label5.setStyleSheet("Background-color: yellow;")

        grid = QGridLayout() #(for Horizontal put hbox)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ ==  "__main__":
    main()     
