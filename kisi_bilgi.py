import sqlite3 as sql
import  time

class Student_Identity:

    def __init__(self,name,f_name,last_name,id,birth_city,country,birth_date,email_address="",phone_number="",faculty=" ",departmen=" ",male=" "):
        self.name=name
        self.f_name=f_name
        self.last_name=last_name
        self.id=id
        self.birth_city=birth_city
        self.country=country
        self.birth_date = birth_date
        self.email_address=email_address
        self.phone_number=phone_number
        self.faculty=faculty
        self.department=departmen
        self.male=male

    def __str__(self):
        return "Name: {}\nF_Name: {}\nLast_Name: {}\nID: {}\nBirth_date: {}\nBirth_City: {}\n" \
               "Country: {}\nEmail Address: {}\nPhone Number: {}\nFaculty: {}\nDepartmen: {}\nMale: {}".format(self.name,
        self.f_name,self.last_name,self.id,self.birth_date,self.birth_city,self.country,self.email_address,
                                                        self.phone_number,self.faculty,self.department,self.male)

class Student_Name(Student_Identity):
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.name

class Student_Father_name(Student_Identity):
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.f_name

class Student_last_name(Student_Identity):
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.last_name

class Student_ID(Student_Identity):
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.id

class Student_Birth_city(Student_Identity):
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.birth_city

class Student_Country(Student_Identity):
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.country

class Student_Birth_Date(Student_Identity):
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.birth_date

class Student_Email(Student_Identity):
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.email_address

class Student_Phone:
    def __init__(self, name, f_name, last_name, id, birth_city, country, birth_date, email_address="", phone_number="",
                 faculty=" ", departmen=" ", male=" "):
        self.name = name
        self.f_name = f_name
        self.last_name = last_name
        self.id = id
        self.birth_city = birth_city
        self.country = country
        self.birth_date = birth_date
        self.email_address = email_address
        self.phobe_number = phone_number
        self.faculty = faculty
        self.department = departmen
        self.male = male
    def __str__(self):
        return self.phobe_number


class Person:

    def __init__(self):
        self.baglanti()

    def baglanti(self):
        self.con=sql.connect("Student.db")
        self.cursor=self.con.cursor()
        self.cursor.execute("Create Table If not Exists Student(name TEXT,f_name Text,last_name TEXT,id TEXT,"
        "birth_city TEXT,country TEXT,birth_date TEXT,email_number TEXT,phone_number TEXT,faculty TEXT,department TEXT,male TEXT)")
        self.con.commit()

    def baglanti_kes(self):
        self.con.close()

    def InsertData(self,student):
        self.cursor.execute("Insert Into Student Values(?,?,?,?,?,?,?,?,?,?,?,?)",(student.name,student.f_name,
                    student.last_name,student.id,student.birth_city,student.country,student.birth_date,
                                student.email_address,student.phone_number,student.faculty,student.department,student.male))

        self.con.commit()

    def Show_data(self):
        self.cursor.execute("Select * From Student")
        students=self.cursor.fetchall()
        if(len(students)==0):
            print("There is no exists any thing.")
        else:
            for stu in students:
                print(Student_Identity(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7],stu[8],stu[9],stu[10],stu[11]))


    def Insert_New_Student(self):
        name=input("Enter name:")
        surname=input("Enter surname:")
        f_name=input("Enter Father name:")
        birth_date=input("Enter birth date:")
        birth_city=input("Enter birth city:")
        country=input("Enter country:")
        email_address=input("Email adress:")
        phone_number=input("Phone number:")
        faculty_number=int(input("Enter faculty number:"))
        department_number=int(input("Enter department number:"))
        Input_year=int(input("Enter year:"))
        Input_number=int(input("Enter the input number of student of the same year:"))
        faculty=0
        department=0
        male=0
        self.studentId=0
        if(faculty_number<10):
            faculty_number=("0"+str(faculty_number))

        elif(faculty_number>99):
            faculty_number%=100
            if(faculty_number<10):
                faculty_number = ("0" + str(faculty_number))
            else:
                faculty_number=str(faculty_number)

        else:
            faculty_number = str(faculty_number)


        if (department_number < 10):
            department_number = ("0" + str(department_number))

        elif (department_number > 99):
            department_number %= 100
            if (department_number < 10):
                department_number = ("0" + str(department_number))
            else:
                department_number = str(department_number)

        else:
            department_number = str(department_number)


        if (Input_year < 10):
            Input_year = ("0" + str(Input_year))

        elif (Input_year > 99):
            Input_year %= 100
            if (Input_year < 10):
                Input_year = ("0" + str(Input_year))
            else:
                Input_year = str(Input_year)

        else:
            Input_year = str(Input_year)

        if (Input_number < 10):
            Input_number = ("00" + str(Input_number))

        elif (Input_number < 100):
            Input_number = ("0" + str(Input_number))

        elif (Input_number > 999):
            Input_number %= 1000
            if (Input_number < 10):
                Input_number = ("00" + str(Input_number))
            elif(Input_number<100):
                Input_number=("0"+str(Input_number))
            else:
                Input_number = str(Input_number)

        else:
            Input_number = str(Input_number)

        studentId = str(Input_year) + str(faculty_number) + "." + str(department_number) + str(Input_number)
        print("Studendt inserting...")

        newStudent=Student_Identity(name,f_name,surname,studentId,birth_city,country,birth_date,email_address,phone_number)
        self.cursor.execute("Insert Into Student Values(?,?,?,?,?,?,?,?,?,?,?,?)",(newStudent.name,newStudent.f_name,
                    newStudent.last_name,newStudent.id,newStudent.birth_city,newStudent.country,newStudent.birth_date,
                                    newStudent.email_address,newStudent.phone_number,faculty,department,male))

        self.con.commit()
        time.sleep(2)
        print("Student inserted")



    def Ask_Student(self,name):
        self.cursor.execute("Select * From Student Where name=?",(name,))
        stu=self.cursor.fetchall()

        try:
            stu=Student_Identity(stu[0][0],stu[0][1],stu[0][2],stu[0][3],stu[0][4],stu[0][5],stu[0][6],stu[0][7],stu[0][8],
                                 stu[0][9],stu[0][10],stu[0][11])
            return stu
        except:
            print("There is no exists student same of {} name".format(name))


    def Ask_Name_OfStudent(self,id):
        self.cursor.execute("Select * From Student Where id=?", (id,))
        Name = self.cursor.fetchall()
        if (len(Name) == 0):
            return False
        else:
            Name= Student_Name(Name[0][0], Name[0][1], Name[0][2], Name[0][3], Name[0][4], Name[0][5], Name[0][6],
                            Name[0][7], Name[0][8], Name[0][9], Name[0][10], Name[0][11])
            return Name
    def Ask_LastName_OfStudent(self,id):
        self.cursor.execute("Select * From Student Where id=?", (id,))
        ID = self.cursor.fetchall()
        if (len(ID) == 0):
            return False
        else:
            ID = Student_last_name(ID[0][0], ID[0][1], ID[0][2], ID[0][3], ID[0][4], ID[0][5], ID[0][6], ID[0][7], ID[0][8],
                                   ID[0][9],ID[0][10],ID[0][11])
            return ID

    def Ask_FatherName_OfStudent(self,id):
        self.cursor.execute("Select * From Student Where id=?", (id,))
        ID = self.cursor.fetchall()
        if (len(ID) == 0):
            return False
        else:
            ID = Student_Father_name(ID[0][0], ID[0][1], ID[0][2], ID[0][3], ID[0][4], ID[0][5], ID[0][6], ID[0][7], ID[0][8],
                                   ID[0][9],ID[0][10],ID[0][11])
            return ID


    def Ask_ID_OfStudent(self,id):
        self.cursor.execute("Select * From Student Where id=?", (id,))
        ID = self.cursor.fetchall()
        if (len(ID) == 0):
            return False
        else:
            ID = Student_ID(ID[0][0], ID[0][1], ID[0][2], ID[0][3], ID[0][4], ID[0][5], ID[0][6], ID[0][7], ID[0][8],
                                   ID[0][9],ID[0][10],ID[0][11])
            return ID


    def Ask_BirthCity_OfStudent(self, id):
        self.cursor.execute("Select * From Student Where id=?", (id,))
        ID = self.cursor.fetchall()
        if (len(ID) == 0):
            return False
        else:
            ID = Student_Birth_city(ID[0][0], ID[0][1], ID[0][2], ID[0][3], ID[0][4], ID[0][5], ID[0][6], ID[0][7], ID[0][8],
                                   ID[0][9],ID[0][10],ID[0][11])
            return ID


    def Ask_Country_OfStudent(self, id):
        self.cursor.execute("Select * From Student Where id=?", (id,))
        ID = self.cursor.fetchall()
        if (len(ID) == 0):
            return False
        else:
            ID = Student_Country(ID[0][0], ID[0][1], ID[0][2], ID[0][3], ID[0][4], ID[0][5], ID[0][6], ID[0][7], ID[0][8],
                                   ID[0][9],ID[0][10],ID[0][11])
            return ID

    def Ask_Birth_Date_OfStudent(self,id):
        self.cursor.execute("Select * From Student Where id=?", (id,))
        ID = self.cursor.fetchall()
        if (len(ID) == 0):
            return False
        else:
            ID = Student_Birth_Date(ID[0][0], ID[0][1], ID[0][2], ID[0][3], ID[0][4], ID[0][5], ID[0][6], ID[0][7], ID[0][8],
                                                   ID[0][9],ID[0][10],ID[0][11])
            return ID


    def Ask_ID_OfStudent_Phone(self,id):
        self.cursor.execute("Select * From Student Where id=?",(id,))
        ID=self.cursor.fetchall()
        if(len(ID)==0):
            return False
        else:
            ID=Student_Phone(ID[0][0],ID[0][1],ID[0][2],ID[0][3],ID[0][4],ID[0][5],ID[0][6],ID[0][7],ID[0][8],
                                   ID[0][9],ID[0][10],ID[0][11])
            return ID

    def Ask_ID_OfStudent_Email(self,id):
        self.cursor.execute("Select * From Student Where id=?", (id,))
        ID = self.cursor.fetchall()
        if (len(ID) == 0):
            return False
        else:
            ID = Student_Email(ID[0][0], ID[0][1], ID[0][2], ID[0][3], ID[0][4], ID[0][5], ID[0][6], ID[0][7], ID[0][8],
                                   ID[0][9],ID[0][10],ID[0][11])
            return ID


    def Delet_Student(self,id):
        self.cursor.execute("Select * FROM Student Where id=?",(id,))
        student=self.cursor.fetchall()
        if len(student)==0:
            print("The student does'n exist")
        else:
            self.cursor.execute("DELETE FROM Student WHERE id=?",(id,))
            self.con.commit()
            time.sleep(2)
            print("Student deleted")


#person=Person()
# person.Delet_Student("4508.01476")
# person.denem("1704.03023")
# print(person.Ask_ID_OfStudent_Phone("1604.01040"))
# person.Insert_New_Student()
# person.Show_data()
# print(person.Ask_Student("Nawid"))
# if person.Ask_ID_OfStudent("1604.01040"):
#     print("This ID also exists in your program")
# else:
#     print(person.Ask_ID_OfStudent("1604.01040"))

# person.Ask_Student("Nawid")//1805.00142
# print(person.Ask_Name_OfStudent("1704.03023"))