
import sqlite3
class Data_base:
    def __init__(self):
        self.name=0;
        self.id=0;
        self.connect_to_sql()
    def connect_to_sql(self):
        self.con=sqlite3.connect("example1.db")
        self.cursor=self.con.cursor()
        self.cursor.execute("Create Table If Not Exists example1 (name text Null,id text Null)")
        self.con.commit()
    def baglanti_kes(self):
        self.con.commit()

    def bilgi_ekle(self,name,id,newSutun):
        self.cursor.execute("")
        self.cursor.execute("Insert Into example1 values(?,?,?)",(name,id,newSutun))
        self.con.commit()

    #Sayin hocalar bun bruada yeni sutun eklemek istiyorum
    def sutun_ekle(self):
        self.cursor.execute("ALTER TABLE example1 ADD Column varchar default  ")
        self.con.commit()
data_base=Data_base()
# alter table t1 add column status varchar default 'N';
# data_base.bilgi_ekle("Ogrenci","1234")
#yani burada yeni sutun eklemek istiyorum
# data_base.sutun_ekle("YeniSutun")
data_base.bilgi_ekle("Ogrenci","1234","NewSutun")

