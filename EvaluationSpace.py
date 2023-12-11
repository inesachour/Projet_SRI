from PyQt5 import QtCore, QtGui, QtWidgets
import Indexation, Vectorial
import functools

repertory = ""
class EvaluationSpace(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 600)
        Form.setGeometry(300, 50, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #fff;\n" "color: #0C2444;")
        self.closeWindow = Form.close
        
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setGeometry(QtCore.QRect(340, 35, 500, 30))
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setStyleSheet("font-weight:500;\n" "font-size:20px")
        self.labelTitle.setText("Évaluation")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 67, 17))
        self.label_2.setObjectName("label_2")

        pixmap = QtGui.QPixmap('images/MonChef-logo.png').scaledToWidth(90)
        self.label_2.setPixmap(pixmap)
        self.label_2.setGeometry(QtCore.QRect(680, 15, 100, 30))

        pixmap1 = QtGui.QPixmap('images/back.png').scaledToWidth(50)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(QtCore.QRect(25, 15, 50, 50))
        self.label.mousePressEvent = self.retour

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 100, 450, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFrame(False)
        self.lineEdit.setStyleSheet("background-color: #fff;border: 1px solid #0C2444;border-left:0px")
        self.lineEdit.setPlaceholderText('Chercher')
        self.lineEdit.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(Form) 
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(600, 100, 50, 30))
        self.pushButton_2.setStyleSheet("background-color: #2596be;\n" "color:#fff;font-size:14px;border-top-right-radius: 15px;border-bottom-right-radius: 15px;")
        self.pushButton_2.clicked.connect(self.getDir)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 180, 500, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font-weight:500;\n" "font-size:17px")
        self.label_3.hide()

        self.label2Hide = QtWidgets.QLabel(Form)
        self.label2Hide.setGeometry(QtCore.QRect(110, 250, 600, 30))
        self.label2Hide.setObjectName("label2Hide")
        self.label2Hide.setStyleSheet("font-weight:200;\n" "font-size:15px")
        self.label2Hide.setText("NOTE: Ajouter votre collection, taper votre requête et cliquer sur l’icône de recherche. ") 
        self.label2Hide.hide()    


        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("background-color: #fff;\n" "border-top-left-radius: 15px;border-bottom-left-radius: 15px;border: 1px solid #0C2444;border-right:0px")
        pixmap2 = QtGui.QPixmap('images/search.png').scaledToWidth(18)
        self.label_4.setPixmap(pixmap2)
        self.label_4.setGeometry(QtCore.QRect(140, 100, 30, 30))
        self.label_4.setDisabled(True)


        self.labelTitleOne = QtWidgets.QLabel(Form)
        self.labelTitleOne.setGeometry(QtCore.QRect(130, 150, 220, 30))
        self.labelTitleOne.setObjectName("labelTitleOne")
        self.labelTitleOne.setStyleSheet("font-weight:600;font-size:13px")
        self.labelTitleOne.setText("Liste de tout les documents:")

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(130, 180, 250, 120))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color:#f7f7f7;font-size:22px;font-weight:500;")

        self.labelTitleTwo = QtWidgets.QLabel(Form)
        self.labelTitleTwo.setGeometry(QtCore.QRect(410, 150, 220, 30))
        self.labelTitleTwo.setObjectName("labelTitleTwo")
        self.labelTitleTwo.setStyleSheet("font-weight:600;font-size:13px")
        self.labelTitleTwo.setText("Liste des documents sélectionnés:")

        self.listWidget2 = QtWidgets.QListWidget(Form)
        self.listWidget2.setGeometry(QtCore.QRect(410, 180, 250, 120))
        self.listWidget2.setObjectName("listWidget2")
        self.listWidget2.setStyleSheet("background-color:#f7f7f7;font-size:22px;font-weight:500;")

        self.pushButton3 = QtWidgets.QPushButton(Form) 
        self.pushButton3.setEnabled(True)
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.setGeometry(QtCore.QRect(290, 320, 100, 30))
        self.pushButton3.setStyleSheet("background-color: #2596be;color:#fff;font-size:14px;border-radius: 15px")
        self.pushButton3.clicked.connect(self.vectorialSearch)
        self.pushButton3.clicked.connect(self.evaluation)
        self.lineEdit.returnPressed.connect(self.vectorialSearch)


        self.pushButton4 = QtWidgets.QPushButton(Form) 
        self.pushButton4.setEnabled(True)
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.setGeometry(QtCore.QRect(395, 320, 100, 30))
        self.pushButton4.setStyleSheet("background-color: #2596be;color:#fff;font-size:14px;border-radius: 15px")
        self.pushButton4.clicked.connect(self.reinit)


        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(145, 360, 515, 120))
        self.tableView.setObjectName("tableView")
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Dice. Coef', 'Jaccard', 'Cosin'])

        self.tableView.verticalHeader().hide()       

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setDefaultSectionSize(124)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(145, 490, 120, 40))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("font-weight:500;font-size:22px")
        self.label_5.setText('Rappel:')

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(232, 492, 120, 40))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("font-weight:500;font-size:18px")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(410, 490, 140, 40))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("font-weight:500;font-size:22px")
        self.label_6.setText('Précision:')

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(520, 492, 120, 40))
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("font-weight:500;font-size:18px")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Les résultats de la recherche dans l'ordre de pertinence:"))
        self.pushButton_2.setText(_translate("Form", "..."))
        self.pushButton3.setText(_translate("Form", "  Évaluer  "))
        self.pushButton4.setText(_translate("Form", "  Réinitialiser  "))


        self.label_4.setText(_translate("Form", ""))
        

    def retour(self, event):
        self.closeWindow()

    def getDir(self):
        global repertory

        self.listWidget.clear()
        self.listWidget2.clear()

        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setDisabled(False)
        self.label_4.setDisabled(False)
        repertory = directory
        import os
        self.files = os.listdir(repertory)

        for file in self.files:
            self.listWidget.addItem(file)

        self.label2Hide.hide()
        self.listWidget.show()
        self.listWidget2.show()
        self.listWidget.itemClicked.connect(self.addSelectItem)


    def addSelectItem(self, item):
        items = []
        for index in range(self.listWidget2.count()):
            items.append(self.listWidget2.item(index).text())
        if item.text() not in items:
            self.listWidget2.addItem(item.text())


    def vectorialSearch(self):
        global repertory
        self.tableView.model().clear()
        
        query = str(self.lineEdit.text().lower())
        dirrr, everything = [], []

        for index in range(self.listWidget2.count()):
            dirrr.append(str(repertory)+"/"+self.listWidget2.item(index).text())

        for index in range(self.listWidget.count()):
            everything.append(str(repertory)+"/"+self.listWidget.item(index).text())

        self.filesSelected, self.allFiles = dirrr, everything

        vectorial = Vectorial.Vectorial(dirrr, query, 2)
        dice, cos, jaccard = [], [], []
        dice = vectorial.diceCoef()
        cos = vectorial.cosinusMesure()
        jaccard = vectorial.jaccardMesure()

        for i in range(len(dirrr)):
            rowPosition = self.model.rowCount()
            self.model.insertRow(rowPosition)
            self.model.setItem(rowPosition , 0, QtGui.QStandardItem(dice[i][0].split('/')[-1]+','+str(dice[i][1])))
            self.model.setItem(rowPosition , 1, QtGui.QStandardItem(jaccard[i][0].split('/')[-1]+','+str(jaccard[i][1])))
            self.model.setItem(rowPosition , 2, QtGui.QStandardItem(cos[i][0].split('/')[-1]+','+str(cos[i][1])))


    def evaluation(self):

        dirrr = self.filesSelected
        allFiles = self.allFiles

        query = str(self.lineEdit.text().lower())
        selected, everything = [], []
        vectorial = Vectorial.Vectorial(dirrr, query, 2)
        vectorialAll = Vectorial.Vectorial(allFiles, query, 2)

        selected = vectorial.jaccardMesure()
        everything = vectorialAll.jaccardMesure()  

        selectedPert = []
        for doc in selected:    
            if doc[1] != 0:
                docName = doc[0].split('/')[-1]
                selectedPert.append(docName)

        everythingPert = []
        for doc in everything:    
            if doc[1] != 0:
                docName = doc[0].split('/')[-1]
                everythingPert.append(docName)

        print(selected)
        if len(everythingPert) == 0:
            rappel = 0
        else:
            rappel = round(float(len(selectedPert) / len(everythingPert)),2)*100
        self.label_7.setText(str(rappel)+'%')

        if len(dirrr) == 0:
            precision = 0
        else:
            precision = round(float(len(selectedPert) / len(dirrr)),2)*100
        self.label_8.setText(str(precision)+'%')


    def reinit(self):
        global repertory
        repertory = ''
        self.filesSelected = []
        self.allFiles = []
        self.label_7.setText('')
        self.label_8.setText('')
        self.lineEdit.setText('')
        self.listWidget.clear()
        self.listWidget2.clear()
        self.tableView.model().clear()







    def openFile(self, event, file):
        import os
        os.system("subl "+file)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = EvaluationSpace()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

