import mysql.connector
import re
from prettytable import from_db_cursor


class teacher_act:
    def __init__(self):
        self.db = mysql.connector.connect(username="root", password="S@10may1999", host="localhost", database="basicdb")
        self.cur = self.db.cursor()

    def action2(self):
        teach_lst = {}
        print("|++++++++++++++++++++++HOME PAGE+++++++++++++++++++++|")
        print("1.Register New Teacher\n2.Log In\n3.Exit")
        print("========================")
        teach_inpt = input("Enter your selection: ")

        while True:
            if teach_inpt == "1":
                print("*******************Welcome New User**********************")
                teach_name = input("Enter your name: ")
                if re.search('\d', teach_name):
                    print("You have Entered incorrect Name")
                else:
                    teach_lst.update({teach_name: []})
                try:
                    teach_num = int(input("Enter your mobile Number: "))
                    if teach_num in range(6000000000, 9999999999):
                        teach_lst.update({teach_name: [teach_num]})
                    else:
                        print("$$$$$$$$incorrect number!!$$$$$$$$$$$")
                        teach_num2 = int(input("Enter your number again:"))
                        teach_lst.update({teach_name: [teach_num2]})
                except Exception:
                    print("*******>please don't Enter exempted entry<************")
                    teach_num = int(input("Enter your mobile Number: "))
                    if teach_num in range(6000000000, 9999999999):
                        teach_lst.update({teach_name: [teach_num]})
                    else:
                        print("$$$$$$$$incorrect number!!$$$$$$$$$$$")
                        teach_num2 = int(input("Enter your number again:"))
                        teach_lst.update({teach_name: [teach_num2]})
                try:
                    teach_Email = input("Enter your Email Id: ")
                    if re.search("\.com$", teach_Email):
                        teach_lst.update({teach_name: [teach_num, teach_Email]})
                    else:
                        print("$$$$$$$$incorrect Email Id!!$$$$$$$$$$$")
                        teach_Email2 = input("Enter your Email Id: ")
                        teach_lst.update({teach_name: [teach_num, teach_Email2]})
                except Exception:
                    print("*******>please don't Enter exempted entry<************")
                    teach_Email = input("Enter your Email Id: ")
                    if re.search(r"\.com$", teach_Email):
                        teach_lst.update({teach_name: [teach_num, teach_Email]})
                    else:
                        print("$$$$$$$$incorrect Email Id!!$$$$$$$$$$$")
                        teach_Email2 = input("Enter your Email Id: ")
                        teach_lst.update({teach_name: [teach_num, teach_Email2]})
                try:
                    teach_pass = int(input("Set your passward(in digit): "))
                    if teach_pass in range(1000, 9999):
                        teach_lst.update({teach_name: [teach_num, teach_Email, teach_pass]})
                    else:
                        print("Enter password between range of 5000 to 9999")
                        teach_pass3 = int(input("Set your passward(in digit): "))
                        if teach_pass3 in range(5000, 9999):
                            teach_lst.update({teach_name: [teach_num, teach_Email, teach_pass3]})
                except Exception:
                    print("please don't Enter alphabet")
                    teach_pass2 = int(input("Set your passward(in digit): "))
                    if teach_pass2 in range(5000, 9999):
                        teach_lst.update({teach_name: [teach_num, teach_Email, teach_pass2]})
                    else:
                        print("Enter password between range of 5000 to 9999")

                try:
                    table1 = "create table if not exists" + " " + " teacher_data" + "(Name varchar(250),Mobile_number bigint(250),Email_Id varchar(250),Password int(250))"
                    self.cur.execute(table1)
                    value1 = [
                        (teach_name, teach_lst.get(teach_name)[0], teach_lst.get(teach_name)[1], teach_lst.get(teach_name)[2])]
                    self.cur.executemany("insert into teacher_data values(%s,%s,%s,%s)", value1)
                    self.db.commit()
                except Exception:
                    print("===================Something Exceptional Happen=========================")
                    table1 = "create table if not exists" + " " + " teacher_data" + "(Name varchar(250),Mobile_number bigint(250),Email_Id varchar(250),Password int(250))"
                    self.cur.execute(table1)
                    value1 = [
                        (teach_name, teach_lst.get(teach_name)[0], teach_lst.get(teach_name)[1], teach_lst.get(teach_name)[2])]
                    self.cur.executemany("insert into teacher_data values(%s,%s,%s,%s)", value1)
                    self.db.commit()
                break
            elif teach_inpt == "2":
                print("=========================* Log In *=======================")
                while True:
                    teach_login = input("Enter your Email Id: ")
                    self.cur.execute(f"select Email_Id from teacher_data where Email_Id='{teach_login}'")
                    var = self.cur.fetchall()
                    try:
                        if teach_login == var[0][0]:
                            teach_password = int(input("Enter your 4 digit password: "))
                            self.cur.execute(f"select Password from teacher_data where Password={teach_password}")
                            var2 = self.cur.fetchall()
                            if teach_password == var2[0][0]:
                                while True:
                                    print("++++++++++++++++++++++++++++")
                                    print("1.Update your detail\n2.check your marks\n3.Exit")
                                    print("++++++++++++++++++++++++++++")
                                    print("============================")
                                    teach_act = input("Enter your selection: ")
                                    print("============================")
                                    while True:
                                        if teach_act == "1":
                                            while True:
                                                print("++++++++++++++++++++++++++")
                                                print("1.Update your password\n2.Update your Email Id\n3.Exit")
                                                print("+++++++++++++++++++++++++")
                                                print("=========================")
                                                teach_inn = input("Enter your Selection: ")
                                                print("=========================")
                                                if teach_inn == "1":
                                                    try:
                                                        old = int(input("Enter your old password: "))
                                                        new = int(input("Enter your New password: "))
                                                        self.cur.execute(
                                                            f"update teacher_data set Password={new} where Password={old}")
                                                        self.db.commit()
                                                        print("***********Password Changed Sucessfully***************")
                                                    except Exception:
                                                        print(
                                                            "You have entered Alphabet, Password only takes integer Value")
                                                        print(
                                                            "+-----------------------Enter Password Again------------------------+")
                                                        old = int(input("Enter your old password: "))
                                                        new = int(input("Enter your New password: "))
                                                        self.cur.execute(
                                                            f"update teacher_data set Password={new} where Password={old}")
                                                        self.db.commit()
                                                elif teach_inn == "2":
                                                    try:
                                                        old = int(input("Enter your old Email Id: "))
                                                        new = int(input("Enter your New Email Id: "))
                                                        self.cur.execute(
                                                            f"update teacher_data set Email_Id={new} where Email_Id={old}")
                                                        self.db.commit()
                                                        print("***********Password Changed Successfully***************")
                                                    except Exception:
                                                        print(
                                                            "You have entered Alphabet, Password only takes integer Value")
                                                        print(
                                                            "+-----------------------Enter Password Again------------------------+")
                                                        old = int(input("Enter your old Email Id: "))
                                                        new = int(input("Enter your New Email Id: "))
                                                        self.cur.execute(
                                                            f"update teacher_data set Email_Id={new} where Email_Id={old}")
                                                        self.db.commit()
                                                        print("***********Password Changed Successfully***************")
                                                elif teach_inn == "3":
                                                    break
                                                break
                                            break
                                        elif teach_act == "2":
                                            print("================================================")
                                            print("Marks for Academic year 2022-23")
                                            print("================================================")
                                            try:
                                                stud_marks = "create table if not exists" + " " + "student_mark" + "(Id int primary key auto_increment,name varchar(250),subject varchar(250),marks int(250))"
                                                self.cur.execute(stud_marks)
                                                for i in range(5):
                                                    stud_name=input("Enter student name: ")
                                                    for j in range(6):
                                                        stud_sub=input("enter subject name: ")
                                                        mark=int(input("Enter Score: "))
                                                        values=[(stud_name,stud_sub,mark),]
                                                        self.cur.executemany("insert into student_mark(name,subject,marks) values(%s,%s,%s)",values)
                                                        self.db.commit()
                                                self.cur.execute("select * from student_mark")
                                                var3=from_db_cursor(self.cur)
                                                print(var3)
                                            except Exception:
                                                print("============>Something Exceptional Happen<=============")
                                        elif teach_act == "3":
                                            break
                                        break
                                    break
                                break

                            else:
                                print("================Incorrect Password============")
                    except Exception:
                        print("|++++++++++++++++++Exception Occur+++++++++++++++++++|")
            elif teach_inpt=="3":
                break
            break



