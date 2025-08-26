# PyQt5 CSS (Cascading Style Sheets) style sheet for a custom widget

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 300, 300)

        self.button1 = QPushButton("Button 1", self)
        self.button2 = QPushButton("Button 2", self)
        self.button3 = QPushButton("Button 3", self)
        self.initUI()

    def initUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QVBoxLayout(centralWidget)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        centralWidget.setLayout(layout)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""   
            QPushButton{
                border: 3px solid;
                padding: 15px 32px;
                text-align: center;
                font-family: Arial;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 15px;
            }
                           

            QPushButton#button1{
                background-color: hsl(1, 90%, 52%);
            }
            QPushButton#button2{
                background-color: hsl(126, 92%, 20%);
            }
            QPushButton#button3{
                background-color: hsl(217, 54%, 34%);
            }
                           

            QPushButton#button1:hover{
                background-color: hsl(1, 90%, 82%);
            }
            QPushButton#button2:hover{
                background-color: hsl(126, 92%, 60%);
            }
            QPushButton#button3:hover{
                background-color: hsl(217, 54%, 74%);
            }
            """)
            

# Tripple quotes allow for multi-line strings
# for color codes, use google to find the hex code for your color

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())