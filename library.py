import sys,time
from proje import *
from kisi_bilgi import *


from  PyQt5 import QtWidgets,QtGui,QtCore
class Pencre(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(Pencre,self).__init__(parent)

        self.Window()
        self.book_data=Book_Data_base()
    def Window(self):
        self.window=QtWidgets.QWidget()
        self.window.setWindowTitle('Wellcome to Namatullah Program')

        self.lable=QtWidgets.QCheckBox("Hello")
        self.lable2=QtWidgets.QLabel(self.window)
        self.lable2.setPixmap(QtGui.QPixmap("library.jpg"))


        self.lable.setGeometry(110,2,400,10)
        self.lable2.setGeometry(110,100,400,360)

        self.select_command = QtWidgets.QPushButton(self.window)
        self.select_command.setGeometry(100,15,100,20)

        self.write_name=QtWidgets.QLineEdit(self.window)
        self.write_name.setGeometry(80,60,180,20)
        self.write_name.setPlaceholderText("کتاب نوم")


        self.write_writer = QtWidgets.QLineEdit(self.window)
        self.write_writer.setGeometry(80, 80, 180, 20)
        self.write_writer.setPlaceholderText("لیکوال نوم")

        self.write_publisher = QtWidgets.QLineEdit(self.window)
        self.write_publisher.setGeometry(80, 100, 180, 20)
        self.write_publisher.setPlaceholderText("نشرکوونکي نوم")

        self.write_book_type = QtWidgets.QLineEdit(self.window)
        self.write_book_type.setGeometry(80, 120, 180, 20)
        self.write_book_type.setPlaceholderText("کتاب ډول")

        self.write_year = QtWidgets.QLineEdit(self.window)
        self.write_year.setGeometry(80, 140, 180, 20)
        self.write_year.setPlaceholderText("کال")

        self.write_id = QtWidgets.QLineEdit(self.window)
        self.write_id.setGeometry(80, 160, 180, 20)
        self.write_id.setPlaceholderText("دکتاب بارکود")

        self.clear=QtWidgets.QPushButton(self.window)
        self.cancel=QtWidgets.QPushButton(self.window)
        self.write=QtWidgets.QPushButton(self.window)
        self.show=QtWidgets.QPushButton(self.window)
        self.write_area=QtWidgets.QLineEdit(self.window)


        self.clear.setText("clear")
        self.cancel.setText("Cancel")
        self.write.setText("OK")
        self.show.setText("Show Info")
        self.select_command.setText("Select")

        self.clear.clicked.connect(self.clear_function)
        self.cancel.clicked.connect(self.cancel_fucntion)
        self.write.clicked.connect(self.write_function)
        # self.show.clicked.connect(self.show_function)
        # self.select_command.clicked.connect(lambda : self.select(self))


        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.clear)
        h_box.addWidget(self.cancel)
        h_box.addWidget(self.write)
        h_box.addWidget(self.show)
        h_box.addStretch()

        v_box=QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.write_area)
        v_box.addLayout(h_box)



        self.window.setLayout(v_box)



        self.window.setGeometry(30,40,600,500)
        self.window.show()
    def clear_function(self):
        self.write_area.clear()
    def cancel_fucntion(self):
        self.cancel=quit()

    def write_function(self):
        name=self.write_name.text()
        writer=self.write_writer.text()
        publisher=self.write_publisher.text()
        book_type=self.write_book_type.text()
        year=self.write_year.text()
        id=self.write_id.text()
        newBook=book_implemetion(name,writer,publisher,book_type,year,id)
        if newBook:
            self.book_data.Insert_data(newBook)
            self.write_area.setText("Your book was inserted")
        else:
            self.write_area.setText("Your book wasn't intsert")








app=QtWidgets.QApplication(sys.argv)
pencre=Pencre()
sys.exit(app.exec_())
