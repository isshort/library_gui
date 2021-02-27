from proje import *
from kisi_bilgi import *
producted_data=Book_Data_base()
student_sinif=Student_Name()
toplam=0
while True:
    print("""++++++++++++++++++++++++++++++
        Wellcome to Library program
     1. Show Books          6   insert Student
     2. Insert book         6-1 Student show
     3. Ask book            6-3 Ask Student
     4. Buy book            6-4 Insert New Student
     5. count books
              
     q. Exit Program
    ++++++++++++++++++++++++++++""")
    islem=input("Enter any operation: ")
    if (islem == "q"):
        print("Program is closing...")
        time.sleep(2)
        print("Program was closed.")
        break

    elif(islem=='1'):
        producted_data.Show_Books()

    elif(islem=='2'):
        name=input("Name: ")
        writer=input("writer: ")
        publisher=input("publisher:")
        book_type=input("book_type:")
        year=int(input("year: "))
        id=input("ID:")

        print("Book is inserting...")
        time.sleep(2)
        newProduct=book_implemetion(name,writer,publisher,book_type,year,id)
        producted_data.Insert_data(newProduct)
        print("Books were inserted.")

    elif(islem=='3'):
        name=input("Enter book's name:")
        producted_data.Ask_Book(name)

    elif(islem=='4'):
        id=input("Enter id of book:")
        producted_data.buy_Book(id)

    elif(islem=='5'):
        print("Count of book is:")
        producted_data.Count_Books()

    elif(islem=='6'):
        name=input("Name:")
        last_name=input("Last_Name:")
        f_name=input("F_Name:")
        id=input("ID:")
        print("Student is saving...")
        time.sleep(2)
        newStudent=Student_Identity(name,last_name,f_name,id)
        student_sinif.InsertData(newStudent)
        print("Datas were inserted")

    elif (islem=="6-1"):
        print("Data in student file are")
        student_sinif.Show_data()


    elif (islem=="6-3"):
        name=input("Enter student name:")
        student_sinif.Ask_Student(name)

    elif(islem=="6-4"):
        print("New student is inserting....")
        student_sinif.Insert_New_Student()