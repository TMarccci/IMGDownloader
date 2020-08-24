import os
import urllib.request

from PyQt5.QtWidgets import QMessageBox

if not os.path.exists('images'):
    os.makedirs('images')

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IMGDownoad(object):
    def setupUi(self, IMGDownoad):
        IMGDownoad.setObjectName("IMGDownoad")
        IMGDownoad.setMaximumSize(QtCore.QSize(500, 200))
        IMGDownoad.setGeometry(1000, 200, 500, 200)
        IMGDownoad.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.centralwidget = QtWidgets.QWidget(IMGDownoad)
        self.centralwidget.setObjectName("centralwidget")
        self.pngdown = QtWidgets.QPushButton(self.centralwidget)
        self.pngdown.setGeometry(QtCore.QRect(330, 160, 75, 23))
        self.pngdown.setObjectName("pngdown")
        self.gimmeurl = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.gimmeurl.setGeometry(QtCore.QRect(20, 30, 441, 31))
        self.gimmeurl.setAutoFillBackground(False)
        self.gimmeurl.setObjectName("gimmeurl")
        self.imgurl = QtWidgets.QLabel(self.centralwidget)
        self.imgurl.setGeometry(QtCore.QRect(20, 10, 161, 16))
        self.imgurl.setObjectName("imgurl")
        self.gimmename = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.gimmename.setGeometry(QtCore.QRect(20, 100, 311, 31))
        self.gimmename.setObjectName("gimmename")
        self.imgname = QtWidgets.QLabel(self.centralwidget)
        self.imgname.setGeometry(QtCore.QRect(20, 80, 231, 20))
        self.imgname.setObjectName("imgname")
        self.creator = QtWidgets.QPushButton(self.centralwidget)
        self.creator.setGeometry(QtCore.QRect(100, 150, 75, 23))
        self.creator.setObjectName("creator")
        self.version = QtWidgets.QPushButton(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(20, 150, 75, 23))
        self.version.setObjectName("version")
        self.jpgdown = QtWidgets.QPushButton(self.centralwidget)
        self.jpgdown.setGeometry(QtCore.QRect(410, 160, 75, 23))
        self.jpgdown.setObjectName("jpgdown")
        self.asdown = QtWidgets.QLabel(self.centralwidget)
        self.asdown.setGeometry(QtCore.QRect(330, 140, 101, 16))
        self.asdown.setObjectName("as")
        IMGDownoad.setCentralWidget(self.centralwidget)
        self.exitbutton = QtWidgets.QAction(IMGDownoad)
        self.exitbutton.setObjectName("exitbutton")
        self.showcreator = QtWidgets.QAction(IMGDownoad)
        self.showcreator.setObjectName("showcreator")

        self.retranslateUi(IMGDownoad)
        QtCore.QMetaObject.connectSlotsByName(IMGDownoad)

        self.version.clicked.connect(self.ver)
        self.creator.clicked.connect(self.themasterguy)
        self.jpgdown.clicked.connect(self.check)
        self.pngdown.clicked.connect(self.check2)

    def retranslateUi(self, IMGDownoad):
        _translate = QtCore.QCoreApplication.translate
        IMGDownoad.setWindowTitle(_translate("IMGDownoad", "IMG Downloader"))
        self.pngdown.setText(_translate("IMGDownoad", "PNG"))
        self.imgurl.setText(_translate("IMGDownoad", "Please give me the image URL"))
        self.imgname.setText(_translate("IMGDownoad", "Please give me the name you want to picture"))
        self.creator.setText(_translate("IMGDownoad", "Creator"))
        self.version.setText(_translate("IMGDownoad", "Version"))
        self.jpgdown.setText(_translate("IMGDownoad", "JPG"))
        self.asdown.setText(_translate("IMGDownoad", "Download as"))

    def check(self):
        file_name = self.gimmename.toPlainText()
        url = self.gimmeurl.toPlainText()
        file_path = "images/"
        full_path = file_path + file_name + '.jpg'
        urllib.request.urlretrieve(url, full_path)
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Image succesfully downloaded as a .jpg file!")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon("icon.ico"))
        x = msg.exec_()

    def check2(self):
        file_name = self.gimmename.toPlainText()
        url = self.gimmeurl.toPlainText()
        file_path = "images/"
        full_path = file_path + file_name + '.png'
        urllib.request.urlretrieve(url, full_path)
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Image succesfully downloaded as a .png file!")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon("icon.ico"))
        x = msg.exec_()

    def ver(self):
        msg = QMessageBox()
        msg.setWindowTitle("Program Version")
        msg.setText("The program version is 1.0.0")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon("icon.ico"))
        x = msg.exec_()

    def themasterguy(self):
        msg = QMessageBox()
        msg.setWindowTitle("Creator: TMarccci")
        msg.setText("Thanks for downloading!")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon("icon.ico"))
        x = msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    IMGDownoad = QtWidgets.QMainWindow()
    ui = Ui_IMGDownoad()
    ui.setupUi(IMGDownoad)
    IMGDownoad.show()
    sys.exit(app.exec_())
