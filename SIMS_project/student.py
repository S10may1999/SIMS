import mysql.connector
import re
from prettytable import from_db_cursor
class student_act:
    def __init__(self):
        self.db=mysql.connector.connect(username="root",password="S@10may1999",host="localhost",database="basicdb")
        self.cur=self.db.cursor()
    def action(self):
        stud_lst={}

        print("|++++++++++++++++++++++HOME PAGE+++++++++++++++++++++|")
        print("1.Register New Student\n2.Log In\n3.Exit")
        print("========================")
        stud_inpt=input("Enter your selection: ")

        while True:
            if stud_inpt=="1":
                print("*******************Welcome New User**********************")
                stud_name=input("Enter your name: ")
                if re.search('\d',stud_name):
                    print("You have Entered incorrect Name")
                else:
                    stud_lst.update({stud_name:[]})
                try:
                    stud_num=int(input("Enter your mobile Number: "))
                    if stud_num in range(6000000000,9999999999):
                        stud_lst.update({stud_name: [stud_num]})
                    else:
                        print("$$$$$$$$incorrect number!!$$$$$$$$$$$")
                        stud_num2=int(input("Enter your number again:"))
                        stud_lst.update({stud_name: [stud_num2]})
                except Exception:
                    print("*******>please don't Enter exempted entry<************")
                    stud_num = int(input("Enter your mobile Number: "))
                    if stud_num in range(6000000000, 9999999999):
                        stud_lst.update({stud_name: [stud_num]})
                    else:
                        print("$$$$$$$$incorrect number!!$$$$$$$$$$$")
                        stud_num2 = int(input("Enter your number again:"))
                        stud_lst.update({stud_name: [stud_num2]})
                try:
                    stud_Email=input("Enter your Email Id: ")
                    if re.search("\.com$",stud_Email):
                        stud_lst.update({stud_name: [stud_num,stud_Email]})
                    else:
                        print("$$$$$$$$incorrect Email Id!!$$$$$$$$$$$")
                        stud_Email2 = input("Enter your Email Id: ")
                        stud_lst.update({stud_name: [stud_num, stud_Email2]})
                except Exception:
                    print("*******>please don't Enter exempted entry<************")
                    stud_Email = input("Enter your Email Id: ")
                    if re.search(r"\.com$", stud_Email):
                        stud_lst.update({stud_name: [stud_num, stud_Email]})
                    else:
                        print("$$$$$$$$incorrect Email Id!!$$$$$$$$$$$")
                        stud_Email2 = input("Enter your Email Id: ")
                        stud_lst.update({stud_name: [stud_num, stud_Email2]})
                try:
                    stud_pass=int(input("Set your passward(in digit): "))
                    if stud_pass in range(5000,9999):
                        stud_lst.update({stud_name: [stud_num, stud_Email,stud_pass]})
                    else:
                        print("Enter password between range of 5000 to 9999")
                        stud_pass3 = int(input("Set your passward(in digit): "))
                        if stud_pass3 in range(5000, 9999):
                            stud_lst.update({stud_name: [stud_num, stud_Email, stud_pass3]})
                except Exception:
                    print("please don't Enter alphabet")
                    stud_pass2 = int(input("Set your passward(in digit): "))
                    if stud_pass2 in range(1000, 9999):
                        stud_lst.update({stud_name: [stud_num, stud_Email, stud_pass2]})
                    else:
                        print("Enter password between range of 5000 to 9999")

                try:
                    table1="create table if not exists"+" "+" student_data"+"(Name varchar(250),Mobile_number bigint(250),Email_Id varchar(250),Password int(250))"
                    self.cur.execute(table1)
                    value1=[(stud_name,stud_lst.get(stud_name)[0],stud_lst.get(stud_name)[1],stud_lst.get(stud_name)[2])]
                    self.cur.executemany("insert into student_data values(%s,%s,%s,%s)",value1)
                    self.db.commit()
                except Exception:
                    print("===================Something Exceptional Happen=========================")
                    table1 = "create table if not exists" + " " + " student_data" + "(Name varchar(250),Mobile_number bigint(250),Email_Id varchar(250),Password int(250))"
                    self.cur.execute(table1)
                    value1 = [(stud_name, stud_lst.get(stud_name)[0], stud_lst.get(stud_name)[1], stud_lst.get(stud_name)[2])]
                    self.cur.executemany("insert into student_data values(%s,%s,%s,%s)", value1)
                    self.db.commit()
                break
            elif stud_inpt=="2":
                print("=========================* Log In *=======================")

                stud_login=input("Enter your Email Id: ")
                self.cur.execute(f"select Email_Id from student_data where Email_Id='{stud_login}'")
                var=self.cur.fetchall()
                try:
                    if stud_login==var[0][0]:
                        stud_password=int(input("Enter your 4 digit password: "))
                        self.cur.execute(f"select Password from student_data where Password={stud_password}")
                        var2=self.cur.fetchall()
                        if stud_password==var2[0][0]:
                            while True:
                                print("++++++++++++++++++++++++++++")
                                print("1.Update your detail\n2.check your marks\n3.Exit")
                                print("++++++++++++++++++++++++++++")
                                print("============================")
                                stud_act=input("Enter your selection: ")
                                print("============================")
                                while True:
                                    if stud_act=="1":
                                        while True:
                                            print("++++++++++++++++++++++++++")
                                            print("1.Update your password\n2.Update your Email Id\n3.Exit")
                                            print("+++++++++++++++++++++++++")
                                            print("=========================")
                                            stud_inn=input("Enter your Selection: ")
                                            print("=========================")
                                            if stud_inn=="1":
                                                try:
                                                    old=int(input("Enter your old password: "))
                                                    new=int(input("Enter your New password: "))
                                                    self.cur.execute(f"update student_data set Password={new} where Password={old}")
                                                    self.db.commit()
                                                    print("***********Password Changed Sucessfully***************")
                                                except Exception:
                                                    print("You have entered Alphabet, Password only takes integer Value")
                                                    print("+-----------------------Enter Password Again------------------------+")
                                                    old = int(input("Enter your old password: "))
                                                    new = int(input("Enter your New password: "))
                                                    self.cur.execute(f"update student_data set Password={new} where Password={old}")
                                                    self.db.commit()
                                            elif stud_inn=="2":
                                                try:
                                                    old=int(input("Enter your old Email Id: "))
                                                    new=int(input("Enter your New Email Id: "))
                                                    self.cur.execute(f"update student_data set Email_Id={new} where Email_Id={old}")
                                                    self.db.commit()
                                                    print("***********Password Changed Successfully***************")
                                                except Exception:
                                                    print("You have entered Alphabet, Password only takes integer Value")
                                                    print("+-----------------------Enter Password Again------------------------+")
                                                    old = int(input("Enter your old Email Id: "))
                                                    new = int(input("Enter your New Email Id: "))
                                                    self.cur.execute(f"update student_data set Email_Id={new} where Email_Id={old}")
                                                    self.db.commit()
                                                    print("***********Password Changed Successfully***************")
                                            elif stud_inn=="3":
                                                break
                                            break
                                        break
                                    elif stud_act=="2":
                                        print("================================================")
                                        print("Marks for Academic year 2022-23")
                                        print("================================================")
                                        try:
                                            stud_name=input("Enter your Name: ")
                                            self.cur.execute(f"select * from student_mark where name='{stud_name}'")
                                            var3=from_db_cursor(self.cur)
                                            print(var3)
                                        except Exception:
                                            print("============>Something Exceptional Happen<=============")
                                    elif stud_act=="3":
                                        break
                                    break
                                break
                            break

                        else:
                            print("================Incorrect Password============")
                except Exception:
                    print("|++++++++++++++++++Exception Occur+++++++++++++++++++|")
            elif stud_inpt=="3":
                break
            break









