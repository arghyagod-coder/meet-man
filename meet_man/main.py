from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

app= QApplication(sys.argv)

def main():  
    web= QWebEngineView()
    web.load(QUrl('https://meet.google.com/?hl=en'))
    web.show()

    sys.exit(app.exec_())

main()