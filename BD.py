from getpass import getpass
from mysql.connector import connect, Error
from tkinter import *

root=Tk()
root.geometry("700x700")
e1=Entry(root,  width=25, font="Arial 20")
e11=Entry(root,width=25, font="Arial 20")
e111=Entry(root,width=25, font="Arial 20")
b2=Button(root,text="Set",font="Arial 20")
b1=Button(root,text="Get",font="Arial 20")
e2=Entry(root,width=25, font="Arial 20")
t1=Text(root,font="Arial 20")
def getinf(event):
    try:
        with connect(
                host="localhost",
                user="root",
                password="gosha90",
                database="BH1"
        ) as connection:
            show_db_query = """SELECT * FROM BH1.books;"""
            x="""CREATE TABLE BH1.customer(
                     id .....,
                     fio ...
                     );"""
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                pr=""
                # print(cursor)
                for db in cursor:
                    s2=str(db)
                    s2=s2.replace("Decimal","")
                    s2=s2.replace("(", "")
                    s2=s2.replace(")", "")
                    s2 = s2.replace("'", "")
                    s2 = s2.replace(",", "")
                    pr=pr+s2+"\n"
                t1.delete(1.0,END)
                t1.insert(1.0,pr)
    except Error as e:
        print(e)
b1.bind("<Button-1>",getinf)
def setinf(event):
    try:
        with connect(
                host="localhost",
                user="root",
                password="gosha90",
                database="BH1"
        ) as connection:
            # sp=e1.get().split()
            sp=[]
            sp.append(e1.get())
            sp.append(e11.get())
            sp.append(e111.get())
            print(sp)
            show_db_query = """INSERT INTO BH1.books(title,author,price) 
            VALUES(%s,%s,%s);"""
            sc=[(sp[0],sp[1],sp[2])]
            with connection.cursor() as cursor:
                cursor.executemany(show_db_query,sc)
                connection.commit()
                # pr=""
                # for db in cursor:
                #     pr=pr+str(db)
                # t1.delete(1.0,END)
                # t1.insert(1.0,pr)
    except Error as e:
        print(e)

b2.bind("<Button-1>",setinf)
Label(root,text="Название",font="Arial 15").pack()
e1.pack()
Label(root,text="Автор",font="Arial 15").pack()
e11.pack()
Label(root,text="Цена",font="Arial 15").pack()
e111.pack()
b2.pack()
b1.pack()
e2.pack()
t1.pack()
root.mainloop()