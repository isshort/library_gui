from proje import *
from  kisi_bilgi import *
from infoWindow import *
from sing_up import *
from PIL import Image,ImageFilter

producted_book=Book_Data_base()
Persona_info=Person()
book_date=Book_Data_base()

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 512)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 601, 511))
        self.groupBox.setObjectName("groupBox")
        self.KPU = QtWidgets.QTextEdit(self.groupBox)
        self.KPU.setGeometry(QtCore.QRect(70, 40, 431, 171))
        self.KPU.setReadOnly(True)
        self.KPU.setObjectName("KPU")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 290, 431,41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 220, 431, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 420, 431, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 250, 431, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 360, 411, 31))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", " "))
        self.KPU.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#e82c25;\">Manas University  <br></span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.radioButton.setText(_translate("Dialog", "Teacher"))
        self.radioButton_3.setText(_translate("Dialog", "Student"))
        self.radioButton_2.setText(_translate("Dialog", "Personal"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your name"))
        self.pushButton_3.setText(_translate("Dialog", "Sign up"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Enter your ID"))

        self.pushButton.clicked.connect(lambda: self.sign_in_function(self.radioButton.isChecked(),
                                                                      self.radioButton_3.isChecked(),
                                                                      self.radioButton_2.isChecked(), self.lineEdit,
                                                                      self.lineEdit_2))
        self.pushButton_2.clicked.connect(self.cancel_function)
        self.pushButton_3.clicked.connect(lambda: self.sign_up_function(self.radioButton.isChecked(),
                                                                    self.radioButton_3.isChecked(),
                                                                    self.radioButton_2.isChecked(), self.lineEdit,
                                                                    self.lineEdit_2))


    def sign_up_function(self,teacher,student,personal,lineEdit1,lineEdit):
        self.window_sign_up=QtWidgets.QMainWindow()
        self.ui_sign_up=Ui_sign_up_Dialog()
        self.ui_sign_up.setupUi(self.window_sign_up)
        self.window_sign_up.show()
        self.ui_sign_up.pushButton_3Cancel.clicked.connect(self.cancel_function_of_sing_up)
        self.ui_sign_up.pushButton_2Go_Back.clicked.connect(self.go_back_function_of_sign_up)

    def go_back_function_of_sign_up(self):
        self.window_sign_up.hide()

    def cancel_function_of_sing_up(self):
        
        self.window_sign_up.close()

    def sign_in_function(self,teacher,student,personal,lineEdit1,lineEdit):

        self.window_te = QtWidgets.QMainWindow()
        self.ui_te = Ui_info_Dialog()
        self.ui_te.setupUi(self.window_te)
        self.ui_te.pushButton_6Cancel.clicked.connect(self.sign_in_cancel)
        self.ui_te.pushButton_5GoBack.clicked.connect(self.sign_in_GoBack)
        Name = lineEdit1.text()
        Id = lineEdit.text()

        if len(Id)==0:
            self.label.setText("<font color='red'>Please write your ID</font>")
        else:
            self.label.clear()
            if teacher:
                self.ui_te.label.setText("Mr rouf hello  "+Name+" To Namatullah wahidi Program")
                self.window_te.show()
            elif student:
                self.ui_te.label.setText("Welcome Mr "+Name+" To Namatulla wahidi Programm")
                if Persona_info.Ask_ID_OfStudent(Id)==False:
                    self.label.setText("<font color='red'>Your Id does not exist in your progaram</font>")
                else:
                    self.ui_te.label_2.setText(str(Persona_info.Ask_ID_OfStudent_Phone(Id)))
                    self.ui_te.label_3.setText(str(Persona_info.Ask_ID_OfStudent_Email(Id)))
                    self.window_te.show()
                    self.ui_te.pushButton_2.clicked.connect(lambda :self.personality_function(Id))

            elif personal:
                self.ui_te.label.setText("Welcome Mr "+Name+" To Namatulla wahidi Programm")
                self.window_te.close()
            else:
                self.label.setText("<font color='red'>Please select a point</font>")
    def sign_in_cancel(self):
        self.window_te.close()
    def sign_in_GoBack(self):
        self.window_te.hide()
    def personality_function(self,Id):
        self.window_personal = QtWidgets.QMainWindow()
        self.personality = Ui_Personality_Dialog()
        self.personality.setupUi(self.window_personal)
        self.personality.lineEditName.setText(str(Persona_info.Ask_Name_OfStudent(Id)))
        self.personality.lineEdit_3LastName.setText(str(Persona_info.Ask_LastName_OfStudent(Id)))
        self.personality.lineEdit_4FatherName.setText(str(Persona_info.Ask_FatherName_OfStudent(Id)))
        self.personality.lineEdit_6StudentID.setText(str(Persona_info.Ask_ID_OfStudent(Id)))
        self.personality.lineEdit_7BirthCity.setText(str(Persona_info.Ask_BirthCity_OfStudent(Id)))
        self.personality.lineEdit_8Country.setText((str(Persona_info.Ask_Country_OfStudent(Id))))
        self.personality.lineEdit_9BirthDate.setText(str(Persona_info.Ask_Birth_Date_OfStudent(Id)))
        self.personality.lineEdit_10EmailAddress.setText(str(Persona_info.Ask_ID_OfStudent_Email(Id)))
        self.personality.lineEdit_11PhoneNumber.setText(str(Persona_info.Ask_ID_OfStudent_Phone(Id)))

        self.personality.Cancel.clicked.connect(self.personality_Cancel_function)
        self.window_personal.show()


    def cancel_function(self):
        self.pushButton_2=quit()
    def personality_Cancel_function(self):
        self.window_personal.close()




if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QDialog()
    v1=Ui_Dialog()
    v1.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
