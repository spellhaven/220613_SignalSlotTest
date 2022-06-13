import sys
from PyQt5.QtWidgets import *

#본 윈도 애플리케이션은 여러분이 하는 것에 따라 커질 수도 작아질 수도 있습니다

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        lcd = QLCDNumber(self) # 슬롯 할 놈
        dial = QDial(self) # 시그널 할 놈

        btn1 = QPushButton('BIG', self)
        btn2 = QPushButton('SMALL', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)

        vbox.addLayout(hbox) # vbox 밑에 hbox를 달아봐.
        self.setLayout(vbox) # self를 vbox 모양으로 만들어봐.

        dial.valueChanged.connect(lcd.display) #커넥트에선 display() 아니고 display... 크킄... 이름만... 크. 크킄...!
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)

        self.setGeometry(100, 100, 200, 200)
        self.show()

    def resizeBig(self):
        self.resize(400, 400)

    def resizeSmall(self):
        self.resize(150, 150)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
