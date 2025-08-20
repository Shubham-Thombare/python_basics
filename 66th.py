# PyQt5 Qlabels
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello, PyQt5!", self)
        label.setFont(QFont("Arial", 24))
        label.setGeometry(0, 0, 400, 100)
        label.setStyleSheet("color: #292929; background-color: #6fdcf7;" 
                            "font-weight: bold; text-align: center;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
       #label.setAlignment(Qt.AlignTop)  #vertically TOP
        #label.setAlignment(Qt.AlignBottom)  #vertically BOTTOM
        #label.setAlignment(Qt.AlignVCenter)  #vertically CENTER

        #label.setAlignment(Qt.AlignRight)  #horizontally RIGHT
        #abel.setAlignment(Qt.AlignHCenter)  #horizontally CENTER
        #label.setAlignment(Qt.AlignLeft)  #horizontally LEFT

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #horizontally CENTER and vertically TOP
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #horizontally CENTER and vertically BOTTOM
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #horizontally CENTER and vertically CENTER
        label.setAlignment(Qt.AlignCenter)  #horizontally and vertically CENTER


def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":        
    main()