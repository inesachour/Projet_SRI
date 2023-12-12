from PyQt5 import QtCore, QtGui, QtWidgets
import SearchBoolUI, SearchVecUI, EvaluationUI

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color: #fff; color: #0C2444;")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.hideWindow = Form.hide

        #Recherche Booleenne
        self.rech_bool = QtWidgets.QLabel(Form)
        self.rech_bool.setGeometry(QtCore.QRect(250, 50, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rech_bool.setFont(font)
        self.rech_bool.setObjectName("rech_bool")

         # Separator Line 1
        self.line1 = QtWidgets.QFrame(Form)
        self.line1.setGeometry(QtCore.QRect(240, 110, 300, 3))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")

        #Recherche Vectorielle
        self.rech_vect = QtWidgets.QLabel(Form)
        self.rech_vect.setGeometry(QtCore.QRect(250, 120, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rech_vect.setFont(font)
        self.rech_vect.setObjectName("rech_vect")

        # Separator Line 2
        self.line2 = QtWidgets.QFrame(Form)
        self.line2.setGeometry(QtCore.QRect(240, 180, 300, 3))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")

        #Evaluation
        self.evaluation = QtWidgets.QLabel(Form)
        self.evaluation.setGeometry(QtCore.QRect(250, 190, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.evaluation.setFont(font)
        self.evaluation.setObjectName("evaluation")

        # Separator Line 3
        self.line3 = QtWidgets.QFrame(Form)
        self.line3.setGeometry(QtCore.QRect(240, 250, 300, 3))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")

        # Empty space
        self.space = QtWidgets.QFrame(Form)
        self.space.setGeometry(QtCore.QRect(240, 260, 300, 20))
        self.space.setObjectName("space")

        self.rech_bool.mousePressEvent = self.openBoolean
        self.rech_vect.mousePressEvent = self.openVectorial
        self.evaluation.mousePressEvent = self.openEvaluation

        self.rech_vect.setStyleSheet("font-weight:600")
        self.rech_bool.setStyleSheet("font-weight:600")
        self.evaluation.setStyleSheet("font-weight:600")

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
        self.ui = SearchBoolUI.SearchBoolUI()
        self.ui.setupUi(self.window)
        self.window.show()


    def openVectorial(self, event):
        self.window = QtWidgets.QWidget()
        self.ui = SearchVecUI.SearchVecUI()
        self.ui.setupUi(self.window)
        self.window.show()


    def openEvaluation(self, event):
        self.window = QtWidgets.QWidget()
        self.ui = EvaluationUI.EvaluationUI()
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
