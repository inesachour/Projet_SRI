from PyQt5 import QtCore, QtGui, QtWidgets
import Indexation
import functools

repertory = ""

class SearchBoolUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 450)
        Form.setGeometry(300, 150, 800, 500)
        Form.setStyleSheet("background-color: #fff; color: #0C2444;")
        self.closeWindow = Form.close

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setGeometry(QtCore.QRect(280, 35, 500, 30))
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setStyleSheet("font-weight:500; font-size:24px; color: #2596be;")
        self.labelTitle.setText("Recherche booléenne")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")

        pixmap1 = QtGui.QPixmap('images/back.png').scaledToWidth(30)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(QtCore.QRect(25, 15, 30, 30))
        self.label.mousePressEvent = self.retour

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 80, 550, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFrame(False)
        self.lineEdit.setStyleSheet("background-color: #fff; border: 1px solid #2596be;")
        self.lineEdit.setPlaceholderText("rechercher")
        self.lineEdit.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(660, 80, 80, 30))
        self.pushButton_2.setStyleSheet("background-color: #2596be; color:#fff; font-size:14px;")
        self.pushButton_2.clicked.connect(self.getDir)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 500, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font-weight:500; font-size:17px; color: #2596be;")


        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(130, 180, 500, 200))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color:#f7f7f7; font-size:20px; font-weight:500; border: 1px solid #2596be;")

        self.lineEdit.returnPressed.connect(self.booleanSearch)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Résultats par ordre de pertinence:"))
        self.pushButton_2.setText(_translate("Form", "Importer"))
        

    def retour(self, event):
        self.closeWindow()


    def getDir(self):
        global repertory
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setDisabled(False)
        repertory = directory
        print(repertory)

    
    def booleanSearch(self, event = False):
        global repertory
        query = str(self.lineEdit.text().lower())
        dirrr = str(repertory)+"/"
        result = []
        index = Indexation.Indexation(False)
        result = index.booleanSearch(dirrr, query)
        self.listWidget.clear()
        sizeResult = len(result)
        for i, res in zip(range(sizeResult),result):
            self.listWidget.addItem(res)

        
    def openFile(self, item):
        import os
        file = repertory+"/"+item.text()
        os.system("subl "+file)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SearchBoolUI()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

