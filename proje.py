import sqlite3 as sql
import time
class book_implemetion:

    def __init__(self,name="",writer="",publisher="",book_type="",year=None,id=""):
        self.name=name
        self.writer=writer
        self.publisher=publisher
        self.book_type=book_type
        self.year=year
        self.id=id

    def __str__(self):
        return "Name: {}\nwriter: {}\npublisher: {}\nbook_type: {}\nyear: {}\nId: {}\n".format(self.name,self.writer,
                                                    self.publisher,self.book_type,self.year,self.id)

class Book_Data_base:

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.con=sql.connect("Books.db",timeout=10)
        self.imlec=self.con.cursor()
        sorgu = "Create Table If not Exists Books(name TEXT ,writer TEXT,publisher TEXT,book_type TEXT,year INT ,id TEXT)"
        self.imlec.execute(sorgu)
        self.con.commit()

    def baglanti_kes(self):
        self.con.close()

    def Insert_data(self,book):
        sorgu="Insert Into Books  values(?,?,?,?,?,?)"
        self.imlec.execute(sorgu, (book.name, book.writer, book.publisher,book.book_type,book.year,book.id))
        self.con.commit()

    def Ask_Book(self,name):
        self.imlec.execute("Select * From Books where name = ?",(name,))
        books=self.imlec.fetchall()
        if(len(books)==0):
            print("There is no exists same of this Books")
        else:
            book=book_implemetion(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4],books[0][5])
            print(book)

    def buy_Book(self,id):
        self.imlec.execute("Select * From Books where id = ?",(id,))
        Books=self.imlec.fetchall()
        if(len(Books)==0):
            print("There is no exists same of this product")
        else:
            Book=book_implemetion(Books[0][4])

            self.take += 1
            print(Book)

    def Show_Books(self):
        self.imlec.execute("Select * From Books")
        show_books=self.imlec.fetchall()
        if(len(show_books)==0):
            print("There is no exists Books")
        else:
            for data in show_books:
                print(book_implemetion(data[0],data[1],data[2],data[3],data[4],data[5]))


    def Count_Books(self):
        self.imlec.execute("Select * From Books")
        count_books=self.imlec.fetchall()
        count=0
        for data in count_books:
            count+=1
        print(count)


    def Delet_column(self):
        self.imlec.execute("DELETE from Books2 Wahidi1")
        print("Your column was deleted")
