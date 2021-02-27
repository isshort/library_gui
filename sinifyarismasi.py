from  awal import *
from PyQt5 import QtCore, QtWidgets
from datetime import datetime
from PyQt5 import QtGui
class Ui_sinif_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(682, 648)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(40, 10, 601, 611))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 609))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.labelListe = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelListe.setGeometry(QtCore.QRect(80, 20, 571, 31))
        self.labelListe.setObjectName("labelListe")
        self.layoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_2.setGeometry(QtCore.QRect(250, 280, 76, 271))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelExample = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelExample.setObjectName("labelExample")
        self.verticalLayout_3.addWidget(self.labelExample)
        self.textEditExample = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEditExample.setReadOnly(True)
        self.textEditExample.setObjectName("textEditExample")
        self.verticalLayout_3.addWidget(self.textEditExample)
        self.layoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_3.setGeometry(QtCore.QRect(330, 280, 61, 271))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelRating = QtWidgets.QLabel(self.layoutWidget_3)
        self.labelRating.setObjectName("labelRating")
        self.verticalLayout_4.addWidget(self.labelRating)
        self.textEditRating = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.textEditRating.setReadOnly(True)
        self.textEditRating.setObjectName("textEditRating")
        self.verticalLayout_4.addWidget(self.textEditRating)
        self.layoutWidget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_4.setGeometry(QtCore.QRect(400, 280, 71, 271))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelParcentage = QtWidgets.QLabel(self.layoutWidget_4)
        self.labelParcentage.setObjectName("labelParcentage")
        self.verticalLayout_5.addWidget(self.labelParcentage)
        self.textEditParcentage = QtWidgets.QTextEdit(self.layoutWidget_4)
        self.textEditParcentage.setReadOnly(True)
        self.textEditParcentage.setObjectName("textEditParcentage")
        self.verticalLayout_5.addWidget(self.textEditParcentage)
        self.layoutWidget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_5.setGeometry(QtCore.QRect(480, 280, 91, 271))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelDate = QtWidgets.QLabel(self.layoutWidget_5)
        self.labelDate.setObjectName("labelDate")
        self.verticalLayout_6.addWidget(self.labelDate)
        self.textEditDate = QtWidgets.QTextEdit(self.layoutWidget_5)
        self.textEditDate.setReadOnly(True)
        self.textEditDate.setObjectName("textEditDate")
        self.verticalLayout_6.addWidget(self.textEditDate)
        self.pushButtonOK = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonOK.setGeometry(QtCore.QRect(460, 570, 114, 32))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtunCancel = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtunCancel.setGeometry(QtCore.QRect(70, 570, 114, 32))
        self.pushButtunCancel.setObjectName("pushButtunCancel")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(130, 59, 311, 21))
        self.label.setObjectName("label")

        self.labelgraphic = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelgraphic.setGeometry(QtCore.QRect(90, 90, 381, 181))
        self.labelgraphic.setObjectName("graphicsView")
        self.pixmap = QtGui.QPixmap('image.jpg')
        self.labelgraphic.setPixmap(self.pixmap)

        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 280, 151, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelName = QtWidgets.QLabel(self.layoutWidget)
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.textEditName = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEditName.setReadOnly(True)
        self.textEditName.setObjectName("textEditName")
        self.verticalLayout.addWidget(self.textEditName)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelListe.setText(_translate("Dialog", "Компютер ийнженердик 2-курстар арасындагы жарышуу"))
        self.labelExample.setText(_translate("Dialog", "Group"))
        self.labelRating.setText(_translate("Dialog", "Rating"))
        self.labelParcentage.setText(_translate("Dialog", "Parcentage"))
        self.labelDate.setText(_translate("Dialog", "Microsecond"))
        self.pushButtonOK.setText(_translate("Dialog", "OK"))
        self.pushButtunCancel.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "AData 2 Group"))
        self.labelName.setText(_translate("Dialog", "Name"))

        self.pushButtonOK.clicked.connect(self.Computation_function)
        self.pushButtunCancel.clicked.connect(self.Cancel_facution)

    def Cancel_facution(self):
        self.window_sinif = QtWidgets.QMainWindow()
        self.window_sinif = Ui_sinif_Dialog()
        self.window_sinif = quit()

    def Computation_function(self):
        url = "http://acmp.ru/index.asp?main=rating&str=+%E4%EE%F2%E0+2"

        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        liste = []
        for i in soup.find_all("tr", {"class": "white"}):
            bilgi = i.text
            bilgi = bilgi[:-1]
            liste.append(bilgi)
            with open("file.txt", "w")as file:
                for i in liste:
                    file.write(i)
        liste1 = []
        with open("file.txt", 'r')as file12:
            ekle = file12.readlines()
            for bilgi in ekle:
                bilgi = bilgi[:-1]
                bilgi = bilgi.lstrip()
                liste1.append(bilgi)

        sizeofarray = len(liste1)
        print(sizeofarray)
        n = sizeofarray // 5 + 1
        m = 5
        h = 1
        a = [[0] * m] * n
        namelist = []
        examplelist = []
        ratinglist = []
        percentagelist = []
        Date = []
        for row in range(len(a) - 1):
            Date1 = datetime.now()
            for column in range(len(a[row])):
                a[row][column] = liste1[h]
                h += 1
            namelist.append(a[row][1])
            examplelist.append(a[row][2])
            ratinglist.append(a[row][3])
            percentagelist.append(a[row][4])
            Date.append(Date1.microsecond)

        self.textEditName.setText(str(namelist))
        self.textEditExample.setText(str(examplelist))
        self.textEditRating.setText(str(ratinglist))
        self.textEditParcentage.setText(str(percentagelist))
        self.textEditDate.setText(str(Date))


if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QDialog()
    v1=Ui_sinif_Dialog()
    v1.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

