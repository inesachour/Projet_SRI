from PyQt5 import QtCore, QtGui, QtWidgets
import SearchSpaceBool, SearchSpaceVec, EvaluationSpace

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #fff;\n" "color: #0C2444;")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.hideWindow = Form.hide

        #Recherche Booleenne
        self.rech_bool = QtWidgets.QLabel(Form)
        self.rech_bool.setGeometry(QtCore.QRect(250, 50, 500, 75))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(15)
        self.rech_bool.setFont(font)
        self.rech_bool.setObjectName("rech_bool")

        #Recherche Vectorielle
        self.rech_vect = QtWidgets.QLabel(Form)
        self.rech_vect.setGeometry(QtCore.QRect(250, 100, 500, 75))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(15)
        self.rech_vect.setFont(font)
        self.rech_vect.setObjectName("rech_vect")

        #Evaluation
        self.evaluation = QtWidgets.QLabel(Form)
        self.evaluation.setGeometry(QtCore.QRect(250, 150, 500, 75))
        self.evaluation.setFont(font)
        self.evaluation.setObjectName("evaluation")
        self.evaluation.setStyleSheet("font-weight:600")
        self.evaluation.mousePressEvent = self.openEvaluation

        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)

        self.rech_bool.mousePressEvent = self.openBoolean
        self.rech_vect.mousePressEvent = self.openVectorial

        self.rech_vect.setStyleSheet("font-weight:600")
        self.rech_bool.setStyleSheet("font-weight:600")


        self.exit = QtWidgets.QLabel(Form)
        self.exit.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.exit.setObjectName("exit")

        pixmap1 = QtGui.QPixmap('images/back.png').scaledToWidth(50)
        self.exit.setPixmap(pixmap1)
        self.exit.setGeometry(QtCore.QRect(25, 15, 50, 50))
        self.exit.mousePressEvent = self.retour


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef."))
        self.rech_bool.setText(_translate("Form", "Recherche Booléenne"))
        self.rech_vect.setText(_translate("Form", "Recherche Vectorielle"))
        self.evaluation.setText(_translate("Form", "Évaluation"))

        self.exit.setText(_translate("Form", ""))

    def openBoolean(self, event):
        self.window = QtWidgets.QMainWindow()
        self.ui = SearchSpaceBool.SearchSpaceBool()
        self.ui.setupUi(self.window)
        self.window.show()

    def openVectorial(self, event):
        self.window = QtWidgets.QWidget()
        self.ui = SearchSpaceVec.SearchSpaceVec()
        self.ui.setupUi(self.window)
        self.window.show()

    def openEvaluation(self, event):
        self.window = QtWidgets.QWidget()
        self.ui = EvaluationSpace.EvaluationSpace()
        self.ui.setupUi(self.window)
        self.window.show()

    def retour(self, event):
        Form.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
