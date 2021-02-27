from  kisi_bilgi import *
student_personality=Person()
from PyQt5 import QtCore, QtGui, QtWidgets


# here we create a cleass to check the input is an integer or not
class checkingInput():
    def __init__(self):
        pass
    def isInteger(self,operation):
        try:
            operation=int(operation)
        except ValueError:
            return "input is not correct"

checkinginput=checkingInput()
class Ui_sign_up_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 503)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 481, 481))
        self.groupBox.setObjectName("groupBox")
        self.lineEditName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditName.setGeometry(QtCore.QRect(30, 30, 171, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.labelname = QtWidgets.QLabel(self.groupBox)
        self.labelname.setGeometry(QtCore.QRect(30, 50, 171, 16))
        self.labelname.setObjectName("labelname")
        self.labelLastname_2 = QtWidgets.QLabel(self.groupBox)
        self.labelLastname_2.setGeometry(QtCore.QRect(30, 90, 171, 16))
        self.labelLastname_2.setObjectName("labelLastname_2")
        self.lineEditlastName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditlastName.setGeometry(QtCore.QRect(30, 70, 171, 21))
        self.lineEditlastName.setObjectName("lineEditlastName")
        self.labelFathername_3 = QtWidgets.QLabel(self.groupBox)
        self.labelFathername_3.setGeometry(QtCore.QRect(30, 130, 171, 16))
        self.labelFathername_3.setObjectName("labelFathername_3")
        self.lineEditFatherName_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditFatherName_3.setGeometry(QtCore.QRect(30, 110, 171, 21))
        self.lineEditFatherName_3.setObjectName("lineEditFatherName_3")
        self.comboBoxCountry = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxCountry.setGeometry(QtCore.QRect(280, 40, 191, 25))
        self.comboBoxCountry.setObjectName("comboBoxCountry")
        self.comboBoxCountry.addItem("")
        self.comboBoxCountry.setItemText(0, "Kyrgyzstan")
        self.comboBoxCountry.addItem("")
        self.comboBoxCountry.addItem("")
        self.comboBoxCountry.addItem("")
        self.comboBoxCountry.addItem("")
        self.comboBoxCountry.addItem("")
        self.comboBoxCountry.addItem("")
        self.comboBoxCountry.addItem("")
        self.comboBoxCountry.addItem("")
        self.labelContry = QtWidgets.QLabel(self.groupBox)
        self.labelContry.setGeometry(QtCore.QRect(290, 20, 151, 16))
        self.labelContry.setObjectName("labelContry")
        self.labelCity = QtWidgets.QLabel(self.groupBox)
        self.labelCity.setGeometry(QtCore.QRect(280, 65, 151, 16))
        self.labelCity.setObjectName("labelCity")
        self.comboBoxCity = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxCity.setGeometry(QtCore.QRect(280, 80, 191, 25))
        self.comboBoxCity.setObjectName("comboBoxCity")
        self.comboBoxCity.addItem("")
        self.comboBoxCity.setItemText(0, "Bishkek")
        self.comboBoxCity.addItem("")
        self.comboBoxCity.addItem("")
        self.comboBoxCity.addItem("")
        self.comboBoxCity.addItem("")
        self.comboBoxCity.addItem("")
        self.comboBoxCity.addItem("")
        self.labelFaculty = QtWidgets.QLabel(self.groupBox)
        self.labelFaculty.setGeometry(QtCore.QRect(280, 105, 151, 16))
        self.labelFaculty.setObjectName("labelFaculty")
        self.comboBoxFaculty = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxFaculty.setGeometry(QtCore.QRect(280, 120, 191, 25))
        self.comboBoxFaculty.setObjectName("comboBoxFaculty")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.setItemText(3, "Engineering")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.comboBoxFaculty.addItem("")
        self.labeldepartment = QtWidgets.QLabel(self.groupBox)
        self.labeldepartment.setGeometry(QtCore.QRect(280, 150, 151, 16))
        self.labeldepartment.setObjectName("labeldepartment")

        self.labelForID=QtWidgets.QLabel(self.groupBox)
        self.labelForID.setGeometry((QtCore.QRect(100,400,291,32)))
        self.labelForID.setObjectName("ForIDisCorrect")
        self.comboBoxDepartment = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxDepartment.setGeometry(QtCore.QRect(280, 170, 191, 25))
        self.comboBoxDepartment.setObjectName("comboBoxDepartment")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.setItemText(3, "Department of Journalism")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.comboBoxDepartment.addItem("")
        self.labelYear = QtWidgets.QLabel(self.groupBox)
        self.labelYear.setGeometry(QtCore.QRect(30, 170, 171, 16))
        self.labelYear.setObjectName("labelYear")
        self.lineEditYear = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditYear.setGeometry(QtCore.QRect(30, 150, 171, 21))
        self.lineEditYear.setObjectName("lineEditYear")
        self.labelStudent_number = QtWidgets.QLabel(self.groupBox)
        self.labelStudent_number.setGeometry(QtCore.QRect(30, 210, 175, 16))
        self.labelStudent_number.setObjectName("labelStudent_number")
        
        self.lineEditStudent_number = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditStudent_number.setGeometry(QtCore.QRect(30, 190, 171, 21))
        self.lineEditStudent_number.setObjectName("lineEditStudent_number")
        
        self.labelBirthdate2=QtWidgets.QLabel(self.groupBox)
        self.labelBirthdate2.setGeometry(30,285,171,16)
        self.labelBirthdate2.setObjectName("lineEditBirth2")
        self.lineEditBirth_date=QtWidgets.QLineEdit(self.groupBox)
        self.lineEditBirth_date.setGeometry(QtCore.QRect(30,300,171,21))
        self.lineEditBirth_date.setObjectName("lineEditBirth_date")
        self.labelBirthdate=QtWidgets.QLabel(self.groupBox)
        self.labelBirthdate.setGeometry(30,320,171,16)
        self.labelBirthdate.setObjectName("labelBirth_date")
        self.lineEditPhone_number = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPhone_number.setGeometry(QtCore.QRect(30, 340, 171, 21))
        self.lineEditPhone_number.setObjectName("lineEditPhone_number")
        self.labelPhoneNumber = QtWidgets.QLabel(self.groupBox)
        self.labelPhoneNumber.setGeometry(QtCore.QRect(30, 360, 171, 16))
        self.labelPhoneNumber.setObjectName("labelPhoneNumber")
        self.lineEditEmail_address = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEmail_address.setGeometry(QtCore.QRect(30, 380, 221, 21))
        self.lineEditEmail_address.setObjectName("lineEditEmail_address")
        self.labelEmail_address = QtWidgets.QLabel(self.groupBox)
        self.labelEmail_address.setGeometry(QtCore.QRect(30, 396, 191, 20))
        self.labelEmail_address.setObjectName("labelEmail_address")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 230, 171, 48))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelMale = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelMale.setObjectName("labelMale")
        self.verticalLayout.addWidget(self.labelMale)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 430, 431, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2Go_Back = QtWidgets.QPushButton(self.widget)
        self.pushButton_2Go_Back.setObjectName("pushButton_2Go_Back")
        self.horizontalLayout_2.addWidget(self.pushButton_2Go_Back)
        self.pushButton_3Cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_3Cancel.setObjectName("pushButton_3Cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_3Cancel)
        self.pushButtonOK = QtWidgets.QPushButton(self.widget)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.horizontalLayout_2.addWidget(self.pushButtonOK)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign_Up"))
        self.groupBox.setTitle(_translate("Dialog", "                               Welcome To Namatullah wahidi Program"))
        self.lineEditName.setPlaceholderText(_translate("Dialog", "Enter your name"))
        self.labelname.setText(_translate("Dialog", " "))
        self.labelLastname_2.setText(_translate("Dialog", ""))
        self.lineEditlastName.setPlaceholderText(_translate("Dialog", "Enter your last name"))
        self.labelFathername_3.setText(_translate("Dialog", ""))
        self.lineEditFatherName_3.setPlaceholderText(_translate("Dialog", "Enter your father name"))
        self.comboBoxCountry.setCurrentText(_translate("Dialog", "Kyrgyzstan"))
        self.comboBoxCountry.setItemText(1, _translate("Dialog", "Turkey"))
        self.comboBoxCountry.setItemText(2, _translate("Dialog", "Russia"))
        self.comboBoxCountry.setItemText(3, _translate("Dialog", "Afghanistan"))
        self.comboBoxCountry.setItemText(4, _translate("Dialog", "Tajikistan"))
        self.comboBoxCountry.setItemText(5, _translate("Dialog", "Ozbekistan"))
        self.comboBoxCountry.setItemText(6, _translate("Dialog", "Turkmenistan"))
        self.comboBoxCountry.setItemText(7, _translate("Dialog", "Kazakistan"))
        self.comboBoxCountry.setItemText(8, _translate("Dialog", "Other"))
        self.labelContry.setText(_translate("Dialog", "Select your country"))
        self.labelCity.setText(_translate("Dialog", "Select your city"))
        self.comboBoxCity.setCurrentText(_translate("Dialog", "Bishkek"))
        self.comboBoxCity.setItemText(1, _translate("Dialog", "Narin"))
        self.comboBoxCity.setItemText(2, _translate("Dialog", "Isyk kul"))
        self.comboBoxCity.setItemText(3, _translate("Dialog", "Talas"))
        self.comboBoxCity.setItemText(4, _translate("Dialog", "Osh"))
        self.comboBoxCity.setItemText(5, _translate("Dialog", "Batkin"))
        self.comboBoxCity.setItemText(6, _translate("Dialog", "Other"))
        self.labelFaculty.setText(_translate("Dialog", "Select your faculty"))

        self.comboBoxFaculty.setItemText(0, _translate("Dialog","Agriculture"))
        self.comboBoxFaculty.setItemText(1, _translate("Dialog", "Communication"))
        self.comboBoxFaculty.setItemText(2, _translate("Dialog", "Economics and Administrative Sciences"))
        self.comboBoxFaculty.setItemText(4, _translate("Dialog", "Fine Arts"))
        self.comboBoxFaculty.setItemText(5, _translate("Dialog", "Latter"))
        self.comboBoxFaculty.setItemText(6, _translate("Dialog", "Sciences"))
        self.comboBoxFaculty.setItemText(7, _translate("Dialog", "Theology"))
        self.comboBoxFaculty.setItemText(8, _translate("Dialog", "Veterinary"))
        self.comboBoxFaculty.setItemText(9, _translate("Dialog", "Medicine"))
        self.comboBoxFaculty.setItemText(10, _translate("Dialog","Language"))
        self.comboBoxFaculty.setItemText(11, _translate("Dialog","HIGH SCHOOL OF PHYSICAL EDUCATION AND SPORTS"))
        self.comboBoxFaculty.setItemText(12,_translate("Dialog","Fine Arts Resim"))
        self.comboBoxFaculty.setItemText(13,_translate("Dialog","SCHOOL OF TOURISM AND HOTELING"))
        self.labeldepartment.setText(_translate("Dialog", "Select your department"))
        self.comboBoxDepartment.setCurrentText(_translate("Dialog", "Department of Horticulture and Agronomy"))
        self.comboBoxDepartment.setItemText(0, _translate("Dialog", "Department of Horticulture and Agronomy"))
        self.comboBoxDepartment.setItemText(1, _translate("Dialog", "Department of Plant Protection"))
        self.comboBoxDepartment.setItemText(2, _translate("Dialog", "Department of Animal Science"))
        self.comboBoxDepartment.setItemText(4, _translate("Dialog", "Department of Public Relations and Advertising"))
        self.comboBoxDepartment.setItemText(5, _translate("Dialog", "Department of Radio, Television and Cinema"))
        self.comboBoxDepartment.setItemText(6, _translate("Dialog", "Department of Economy"))
        self.comboBoxDepartment.setItemText(7, _translate("Dialog", "Department of Management"))
        self.comboBoxDepartment.setItemText(8, _translate("Dialog", "Department of Finance"))
        self.comboBoxDepartment.setItemText(9, _translate("Dialog", "Department of International Relations"))
        self.comboBoxDepartment.setItemText(10, _translate("Dialog", "Department of Finance and Banking"))
        self.comboBoxDepartment.setItemText(11, _translate("Dialog", "Department of Computer Engineering"))
        self.comboBoxDepartment.setItemText(12, _translate("Dialog", "Department of Chemical Engineering"))
        self.comboBoxDepartment.setItemText(13, _translate("Dialog", "Department of Food Engineering"))
        self.comboBoxDepartment.setItemText(14, _translate("Dialog", "Department of Ecological Engineering"))
        self.comboBoxDepartment.setItemText(15, _translate("Dialog", "Department of Industry Engineering"))
        self.comboBoxDepartment.setItemText(16, _translate("Dialog", "Department of Electrical Engineering"))
        self.comboBoxDepartment.setItemText(17, _translate("Dialog", "Department of Painting"))
        self.comboBoxDepartment.setItemText(18, _translate("Dialog", "Department of Performing Arts"))
        self.comboBoxDepartment.setItemText(19, _translate("Dialog", "Department of Western Languages"))
        self.comboBoxDepartment.setItemText(20, _translate("Dialog", "Department of Eastern Languages"))
        self.comboBoxDepartment.setItemText(21, _translate("Dialog", "Department of Educational Science"))
        self.comboBoxDepartment.setItemText(22, _translate("Dialog", "Department of Philosophy"))
        self.comboBoxDepartment.setItemText(23, _translate("Dialog", "Department of Sociology"))
        self.comboBoxDepartment.setItemText(24, _translate("Dialog", "Department of History"))
        self.comboBoxDepartment.setItemText(25, _translate("Dialog", "Department of Turkology"))
        self.comboBoxDepartment.setItemText(26, _translate("Dialog", "Department of Translations"))
        self.comboBoxDepartment.setItemText(27, _translate("Dialog", "Department of Mathematics"))
        self.comboBoxDepartment.setItemText(28, _translate("Dialog", "Department of Applied Mathematics and Informatics"))
        self.comboBoxDepartment.setItemText(29, _translate("Dialog", "Department of Biology"))
        self.comboBoxDepartment.setItemText(30, _translate("Dialog", "Department of Islamic Studies"))
        self.comboBoxDepartment.setItemText(31, _translate("Dialog", "Department of Religious Studies"))
        self.comboBoxDepartment.setItemText(32, _translate("Dialog", "Other"))
        self.labelYear.setText(_translate("Dialog", ""))
        self.lineEditYear.setPlaceholderText(_translate("Dialog", "Enter Year"))
        self.labelStudent_number.setText(_translate("Dialog", ""))
        self.lineEditStudent_number.setPlaceholderText(_translate("Dialog", "Input number of student"))
        self.lineEditBirth_date.setPlaceholderText(_translate("Dialog","Enter your birth date"))
        self.labelBirthdate.setText(_translate("Dialog",""))
        self.labelBirthdate2.setText(_translate("Dialog","day/month/year"))
        self.lineEditPhone_number.setPlaceholderText(_translate("Dialog", "Enter your phone number"))
        self.labelPhoneNumber.setText(_translate("Dialog", ""))
        self.lineEditEmail_address.setPlaceholderText(_translate("Dialog", "Enter your email address"))
        self.labelEmail_address.setText(_translate("Dialog", ""))
        self.labelMale.setText(_translate("Dialog", "Sex"))
        self.radioButton_2.setText(_translate("Dialog", "Male"))
        self.radioButton.setText(_translate("Dialog", "Female"))
        self.pushButton_2Go_Back.setText(_translate("Dialog", "Go Back"))
        self.pushButton_3Cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButtonOK.setText(_translate("Dialog", "OK"))

        self.comboBoxCountry.currentIndexChanged.connect(self.selectCountry)
        self.comboBoxCity.currentIndexChanged.connect(self.selectCity)
        self.comboBoxFaculty.currentIndexChanged.connect(self.selectFaculty)
        self.comboBoxDepartment.currentIndexChanged.connect(self.selectDepartment)

        self.pushButtonOK.clicked.connect(lambda : self.StudentPersonality_function(self.radioButton_2.isChecked(),self.radioButton.isChecked(),
                    self.lineEditName,self.lineEditlastName,self.lineEditFatherName_3,self.lineEditYear,self.lineEditStudent_number,
                    self.lineEditPhone_number,self.lineEditEmail_address))


    def selectCountry(self):
        self.selectedCountry=self.comboBoxCountry.currentText()
        return self.selectedCountry
    def selectCity(self):
        self.selectedCity=self.comboBoxCity.currentText()
        return self.selectedCity
    def selectFaculty(self):
        self.selectedFaculty=0
        if self.comboBoxFaculty.currentText()=="Latter":
            self.selectedFaculty="01"
        elif self.comboBoxFaculty.currentText()=="Economics and Administrative Sciences":
            self.selectedFaculty="02"
        elif self.comboBoxFaculty.currentText() == "Communication":
            self.selectedFaculty="03"
        elif self.comboBoxFaculty.currentText()=="Engineering":
            self.selectedFaculty="04"
        elif self.comboBoxFaculty.currentText() == "Language":
            self.selectedFaculty="05"
        elif self.comboBoxFaculty.currentText() == "SCHOOL OF TOURISM AND HOTELING":
            self.selectedFaculty="07"
        elif self.comboBoxFaculty.currentText() == "Agriculture":
            self.selectedFaculty="08"
        elif self.comboBoxFaculty.currentText() == "Veterinary":
            self.selectedFaculty="09"
        elif self.comboBoxFaculty.currentText() == "Fine Arts":
            self.selectedFaculty="10"
        elif self.comboBoxFaculty.currentText() == "HIGH SCHOOL OF PHYSICAL EDUCATION AND SPORTS":
            self.selectedFaculty="11"
        elif self.comboBoxFaculty.currentText() == "Sciences":
            self.selectedFaculty="12"
        elif self.comboBoxFaculty.currentText() == "Fine Arts Resim":
            self.selectedFaculty="13"
        elif self.comboBoxFaculty.currentText() == "Theology":
            self.selectedFaculty="14"
        return self.selectedFaculty

    def selectDepartment(self):
        departmentSelect=self.comboBoxDepartment.currentText()
        if self.comboBoxDepartment.currentText()=="Other":
            print("That doesn't solve yet")
        else:
            departments={("Department of Horticulture and Agronomy","Department of Journalism","Department of Economy",
               "Department of Computer Engineering","Department of Painting","Department of Western Languages","Department of Mathematics",
               "Department of Islamic Studies"):"01",
                ("Department of Plant Protection","Department of Public Relations and Advertising",
                "Department of Management","Department of Chemical Engineering","Department of Performing Arts","Department of Eastern Languages",
                "Department of Applied Mathematics and Informatics","Department of Religious Studies"):"02",
                ("Department of Animal Science","Department of Radio, Television and Cinema","Department of Finance","Department of Food Engineering",
                 "Department of Educational Science","Department of Biology"):"03",
                ("Department of International Relations","Department of Ecological Engineering","Department of Philosophy"):"04",
                ("Department of Finance and Banking","Department of Industry Engineering","Department of Sociology"):"05",
                ("Department of Electrical Engineering","Department of History"):"06",
                ("Department of Turkology"):"07",("Department of Translations"):"08",}
            self.selectedDepartment=next(v for k,v in departments.items() if departmentSelect in k)
        return self.selectedDepartment



    def StudentPersonality_function(self,male,female,name,lastname,fathername,year,studentnummber,phonenumber,emaileddress):
        name=self.lineEditName.text()
        lastname=self.lineEditlastName.text()
        fathername=self.lineEditFatherName_3.text()
        year=self.lineEditYear.text()
        studentnummber=self.lineEditStudent_number.text()
        birth_date=self.lineEditBirth_date.text()
        phonenumber=self.lineEditPhone_number.text()
        emaileddress=self.lineEditEmail_address.text()
        Country=self.selectCountry()
        City=self.selectCity()
        Faculty=self.comboBoxFaculty.currentText()
        Department=self.comboBoxDepartment.currentText()
        facultynumber=self.selectFaculty()
        department_number=self.selectDepartment()


        if len(name) == 0 or name.isdigit():
            self.labelname.setText("<font color='red'>Please write your name</font>")
        elif len(lastname) == 0:
            self.labelLastname_2.setText("<font color='red'>Please write your last name</font>")

        elif len(fathername) == 0:
            self.labelFathername_3.setText("<font color='red'>Please write your father name</font>")

        elif len(year) == 0 or len(year)!=4:
            self.labelYear.setText("<font color='red'>Year is not correct</font>")

        elif len(studentnummber) == 0 or len(studentnummber) >= 4:

            self.labelStudent_number.setText("<font color='red'>Student's number is not correct</font>")
        elif len(birth_date) == 0:
            self.labelBirthdate.setText("<font color='red'>Please write your birth date</font>")
        elif len(phonenumber) == 0 or len(phonenumber) < 10 or len(phonenumber) > 12:

            self.labelPhoneNumber.setText("<font color='red'>phone number is not correct</font>")
        elif len(emaileddress) == 0:

            self.labelEmail_address.setText("<font color='red'>Please write your email address</font>")

        # here we referace to is Integer  funciton in checking class to check our input
        # Object of checking Input class
        elif checkinginput.isInteger(year):
            self.labelYear.setText(checkinginput.isInteger(year))

        elif checkinginput.isInteger(studentnummber):
            self.labelStudent_number.setText(checkinginput.isInteger(studentnummber))

        elif checkinginput.isInteger(phonenumber):
            self.labelStudent_number.setText(checkinginput.isInteger(studentnummber))

        else:
            alpna = name[0]
            alpna = ord(alpna)
            alplna = lastname[0]
            alplna = ord(alplna)
            alpfna = fathername[0]
            alpfna = ord(alpfna)
            year = int(year)
            year %= 100
            studentnummber = int(studentnummber)
            if studentnummber < 10:
                studentnummber = str(0)+str(0) + str(studentnummber)
                print(studentnummber)
            elif studentnummber < 100:
                studentnummber = str(0) + str(studentnummber)
                print(studentnummber)
            else:
                studentnummber = studentnummber
                print(studentnummber)

            if alpna >= 32 and alpna < 65 or alpna >= 91 and alpna <= 96 or alpna >= 123 and alpna <= 127:
                self.labelname.setText("<font color='red'>Name is not correct</font>")
            elif alplna >= 32 and alplna < 65 or alplna >= 91 and alplna <= 96 or alplna >= 123 and alplna <= 127:
                self.labelLastname_2.setText("<font color='red'>Last name is not correct</font>")
            elif alpfna >= 32 and alpfna < 65 or alpfna >= 91 and alpfna <= 96 or alpfna >= 123 and alpfna <= 127:
                self.labelFathername_3.setText("<font color='red'>Father name is not correct</font>")
            elif (emaileddress.find("@") == -1 or not emaileddress.endswith(".com")):
                self.labelEmail_address.setText("<font color='red'>Email address is not correct</font>")

            else:

                self.labelname.clear()
                self.labelLastname_2.clear()
                self.labelFathername_3.clear()
                self.labelYear.clear()
                self.labelStudent_number.clear()
                self.labelBirthdate.clear()
                self.labelPhoneNumber.clear()
                self.labelEmail_address.clear()
                self.ogrenciNumber=str(year)+str(facultynumber)+"."+str(department_number)+str(studentnummber)

                if student_personality.Ask_ID_OfStudent(self.ogrenciNumber):
                    self.labelForID.setText("<font color='red'>Student is also exists in your program</font>")
                else:
                    print("""
                      Your Name: {}
                      Your last Name: {}
                      Your Father Name: {}
                      Year :{}
                      Student number: {}
                      Phone : {}
                      Email : {}
                      Birth date: {}
                      Country: {}
                      City  :  {}
                      Faculty: {}
                      Department: {}
                      Student ID: {}
                    """.format(name,lastname,fathername,year,studentnummber,phonenumber,emaileddress,birth_date,Country,City,
                        Faculty,Department,self.ogrenciNumber))
                    time.sleep(3)
                    self.newStudent=Student_Identity(name,fathername,lastname,self.ogrenciNumber,City,Country,birth_date,emaileddress,
                                    phonenumber,Faculty,Department,"male")
                    student_personality.InsertData(self.newStudent)

                    self.labelForID.setText("<font color='green'>Congratulations! you inserted a student</font>")

    def Student_ID(self):
        return self.StudentID





if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QDialog()
    v1=Ui_sign_up_Dialog()
    v1.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

