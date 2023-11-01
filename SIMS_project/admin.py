import mysql.connector
import numpy as np
from prettytable import from_db_cursor
import matplotlib.pyplot as mp
import smtplib as s


class admin_act:
    def __init__(self):
        self.db = mysql.connector.connect(username="root", password="S@10may1999", host="localhost", database="basicdb")
        self.cur = self.db.cursor()
    def action3(self):

        username=input("enter your username: ")
        if username=="admin":
            password=input("Enter your password: ")
            if password=="admin":
                while True:
                    print("+++++++++++++++++++++++++++++++")
                    print("1.check Student fees collection\n2.Add School expenses\n3.MIS\n4.Send Email\n5.Exit")
                    print("+++++++++++++++++++++++++++++++")
                    act=input("Enter your selection: ")
                    print("===========================")
                    if act=="1":
                        fee="create table if not exists"+" "+"Fees_collection"+"(Id int primary key auto_increment,student_name varchar(250),student_fees int(250) default 25000)"
                        self.cur.execute(fee)
                        self.cur.execute("insert into Fees_collection(student_name) select Name from student_data")
                        self.cur.execute("select * from Fees_collection")
                        table=from_db_cursor(self.cur)
                        print(table)
                        print("=======================")
                        print("Total fees Collection")
                        print("======================")
                        self.cur.execute("select sum(student_fees) from Fees_collection")
                        table2=from_db_cursor(self.cur)
                        print(table2)
                    elif act=="2":
                        for i in range(5):
                            try:
                                self.cur.execute("create table if not exists expenses(name varchar(250),amount int(250))")
                                exp=input("Name of Expense: ")
                                amt=int(input("Enter amount"))
                                entry=[(exp,amt)]
                                self.cur.executemany("insert into expenses values(%s,%s)",entry)
                            except Exception:
                                print("===========exceptional error occured============")
                        self.cur.execute("select * from expenses")
                        table3=from_db_cursor(self.cur)
                        print(table3)
                    elif act=="3":
                        print("1.check Expenses report\n2.check student marks report\n.3 Exit")
                        self.cur.execute("select amount from expenses")
                        bar_lst=[]
                        bar_lst2=[]
                        for i in self.cur.fetchall():
                            bar_lst.append(i[0])
                        x=np.array(bar_lst)
                        self.cur.execute("select name from expenses")
                        for i in self.cur.fetchall():
                            bar_lst2.append(i[0])
                        y = np.array(bar_lst2)
                        mp.bar(x,y)
                        mp.show()
                    elif act=="4":
                        print("**************Send an Notification Email to students********************")
                        ob=s.SMTP("smtp.gmail.com",587)
                        ob.starttls()
                        ob.login("sandeepsharma89244@gmail.com","ihuxpsviijpxaxsc")
                        subject=input("Enter your Subject: ")
                        body=input("Enter message: ")
                        message="Subject:{}\n\n{}".format(subject,body)
                        self.cur.execute("select Email_Id from student_data")
                        emails=self.cur.fetchall()
                        email_lst=[]
                        for i in emails:
                            for j in i:
                                email_lst.append(j)
                        ob.sendmail("sandeepsharma89244@gmail.com",email_lst,message)
                        print("=============successfully send the email===========")
                    elif act=="5":
                        break
                    break

            else:
                print("Incorrect password!!")
        else:
            print("incorrect username !!!")
