import student
import teacher
import admin
class main_func:
    def second_func(self):
        while True:
            print("+++++++++++++++++++++++++++++++++++++++++++++++")
            print("1.Student Login\n2.Teachers Login\n3.Admin Login")
            print("+++++++++++++++++++++++++++++++++++++++++++++++")
            gen_inpt=input("Enter your Selection: ")
            if gen_inpt=="1":
                obj = student.student_act()
                obj.action()
            elif gen_inpt=="2":
                obj2=teacher.teacher_act()
                obj2.action2()
            elif gen_inpt=="3":
                obj3=admin.admin_act()
                obj3.action3()
            else:
                print("incorrect input")


obj=main_func()
obj.second_func()