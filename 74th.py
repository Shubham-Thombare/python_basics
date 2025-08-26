# PyQt5 Digital Clock

import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

# instead of QMainWindow, we can use QWidget directly for simpler applications

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

        self.setWindowTitle("Digital Clock")

    def initUI(self):
       self.setWindowTitle("Digital Clock")
       self.setGeometry(600, 400, 300, 100)

       layout = QVBoxLayout()
       layout.addWidget(self.time_label)
       self.setLayout(layout)

       self.time_label.setAlignment(Qt.AlignCenter)

       self.time_label.setStyleSheet("font-size: 40px; color: green;")
       self.setStyleSheet("background-color: black;")

       font_id =  QFontDatabase.addApplicationFont("DS-DIGII.TTF") #TTF - True Type Font
       font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
       my_font =   QFont(font_family, 150)
       self.time_label.setFont(my_font)


       self.timer.timeout.connect(self.update_time)
       self.timer.start(1000)  # Update every second
       
       self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())