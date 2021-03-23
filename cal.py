import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import sqrt
import requests
import operator

def om():
    app = QApplication(sys.argv)
    win = QWidget()
    
    url = "https://114xuk3g3n5e3r239922rd7k-wpengine.netdna-ssl.com/wp-content/uploads/sites/8/2017/11/Vintage-Landscape2.jpg"
    image = QImage()
    image.loadFromData(requests.get(url).content)
    
    img = QLabel(win)
    img.setPixmap(QPixmap(image))
    img.show()
    
    def delete():
        l1.clear()
        
    def press1():
        str = l1.text()
        str += '1'
        l1.setText(str) 
         
    def press2():
        str = l1.text()
        str += '2'
        l1.setText(str)    
    
    def press3():
        str = l1.text()
        str += '3'
        l1.setText(str)
    
    def press4():
        str = l1.text()
        str += '4'
        l1.setText(str)        
    
    def press5():
        str = l1.text()
        str += '5'
        l1.setText(str)
    
    def press6():
        str = l1.text()
        str += '6'
        l1.setText(str)
        
    def press7():
        str = l1.text()
        str += '7'
        l1.setText(str)
        
    def press8():
        str = l1.text()
        str += "8"
        l1.setText(str)
    def press9():
        str = l1.text()
        str += '9'
        l1.setText(str)
    def press0():
        str = l1.text()
        str += '0'
        l1.setText(str)
    def plus1():
        str =l1.text()
        str += '+'
        l1.setText(str)
    def min1():
        str = l1.text()
        str += '-'
        l1.setText(str)
    def mul1():
        str = l1.text()
        str += '*'
        l1.setText(str)
    def div1():
        str = l1.text()
        str += "/" 
        l1.setText(str)
        
    def equal():
        
        try:
            expr = l1.text()
            result = eval(expr, {}, {})
        except Exception:
            result = "error" 
        l2 = print(result)
        l1.setText(str(result))
        
              
                       
    b1 = QPushButton(win)
    b1.setText("1")
    b1.setFont(QFont("Arial",20))
    b1.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b1.setDisabled
    b1.setGeometry(100,100,120,50)
    b1.move(20,120)
    b1.clicked.connect(press1)
    
    b2 = QPushButton(win)
    b2.setText("2")
    b2.setFont(QFont("Arial",20))
    b2.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b2.setGeometry(100,100,120,50)
    b2.move(150,120)
    b2.clicked.connect(press2)
    
  

    
    b3 = QPushButton(win)
    b3.setText("3")
    b3.setFont(QFont("Arial",20))
    b3.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b3.setGeometry(100,100,120,50)
    b3.move(280,120)
    b3.clicked.connect(press3)
    
    b4 = QPushButton(win)
    b4.setText("4")
    b4.setFont(QFont("Arial",20))
    b4.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b4.setGeometry(100,100,120,50)
    b4.move(20,180)
    b4.clicked.connect(press4)
    
    b5 = QPushButton(win)
    b5.setText("5")
    b5.setFont(QFont("Arial",20))
    b5.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b5.setGeometry(100,100,120,50)
    b5.move(150,180)
    b5.clicked.connect(press5)
    
    b6 = QPushButton(win)
    b6.setText("6")
    b6.setFont(QFont("Arial",20))
    b6.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b6.setGeometry(100,100,120,50)
    b6.move(280,180)
    b6.clicked.connect(press6)
    
    b7 = QPushButton(win)
    b7.setText("7")
    b7.setFont(QFont("Arial",20))
    b7.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b7.setGeometry(100,100,120,50)
    b7.move(20,240)
    b7.clicked.connect(press7)
    
    b8 = QPushButton(win)
    b8.setText("8")
    b8.setFont(QFont("Arial",20))
    b8.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b8.setGeometry(100,100,120,50)
    b8.move(150,240)
    b8.clicked.connect(press8)
    
    b9 = QPushButton(win)
    b9.setText("9")
    b9.setFont(QFont("Arial",20))
    b9.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b9.setGeometry(100,100,120,50)
    b9.move(280,240)
    b9.clicked.connect(press9)
    
    b0 = QPushButton(win)
    b0.setText("0")
    b0.setFont(QFont("Arial",20))
    b0.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    b0.setGeometry(100,100,290,80)
    b0.move(50,320)
    b0.clicked.connect(press0)
    
    plus = QPushButton(win)
    plus.setText("+")
    plus.setFont(QFont("Arial",20))
    plus.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    plus.setGeometry(100,100,80,50)
    plus.move(410,120)
    plus.clicked.connect(plus1)
    
    min = QPushButton(win)
    min.setText("-")
    min.setFont(QFont("Arial",20))
    min.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    min.setGeometry(100,100,80,50)
    min.move(410,180)
    min.clicked.connect(min1)
    
    div = QPushButton(win)
    div.setText("/")
    div.setFont(QFont("Arial",20))
    div.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    div.setGeometry(100,100,80,50)
    div.move(410,240)
    div.clicked.connect(div1)
    
    mul = QPushButton(win)
    mul.setText("*")
    mul.setFont(QFont("Arial",20))
    mul.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    mul.setGeometry(100,100,135,80)
    mul.move(350,320)
    mul.clicked.connect(mul1)
    
    e1 = QPushButton(win)
    e1.setText("=")
    e1.setFont(QFont("Arial",15))
    e1.setStyleSheet("QPushButton{color:White;background-color:rgba(0,0,0,100)}")
    e1.setGeometry(100,100,350,80)
    e1.move(50,410)
    e1.clicked.connect(equal)
    
    d = QPushButton(win)
    d.setText("Del")
    d.setFont(QFont("arial",20))
    d.setStyleSheet("QPushButton{color : white;background-color:rgba(0,0,0,100)}")
    d.setGeometry(100,100,80,80)
    d.move(410,410)
    d.clicked.connect(delete)
    
    l1 = QLineEdit(win)
    l1.setFont(QFont("arial",20))
    l1.setStyleSheet("QLineEdit{color : White;background-color:rgba(0,0,0,100)}")
    l1.setGeometry(100,100,460,80)
    l1.move(20,20)
    
   
    
    win.setGeometry(100,100,500,500)
    win.setWindowTitle("Calculator")
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    om()    
    