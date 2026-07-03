#1)Create a class with a data member and a member function. Create an object and access both.
# class Student:
#     rollno = 101 #data member

#     def msg(self): #member function
#         print("Hello World")
        
# obj = Student()
# print(obj.rollno)
# obj.msg()
# print(obj)

#2)Write a Python program to demonstrate the use of a default constructor.
# class Demo:
#     def __init__(self):
#         print("I am a Constructor and i am always called first")

#     #Insance Method
#     def info(self):
#         print("one object")
# obj = Demo()
# obj.info()
# obj2 = Demo()

#3)Write a Python program to initialize object data using a constructor and display it.
# class Hod:
#     def __init__(self): #Constructor
#         self.name = "Monika Pagar"
#         self.age = 21
#         self.empid = 1001

#     def info(self):
#         print("My Name is : ",self.name)
#         print("My Age is : ",self.age)
#         print("My EmpID is : ",self.empid)
# obj = Hod() #Object Creation
# obj.info()

#4)Write a Python program to demonstrate a parameterized constructor.
# class Hod:
#     def __init__(self,name,age,rollno): #Parameterized Constructor
#         self.name = name
#         self.age = age
#         self.rollno = rollno

#     def show(self):
#         print("My Name is : ",self.name)
#         print("My Age is : ",self.age)
#         print("My Roll No. is : ",self.rollno)
# obj = Hod("Monika",21,19) #Object Creation
# obj.show()

#5)Write a Python program to demonstrate instance variables using multiple objects.
# class New:
#     def __init__(self):
#         self.a = 10

# obj1 = New()
# obj2 = New()
# obj3 = New()

# obj1.a = 20

# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#6)Write a Python program to demonstrate static (class) variables.
# class New:
#     a = 10 #Static variable

#     def __init__(self):
#         self.name = "Monika"

# obj1 = New()
# obj2 = New()
# obj3 = New()
# New.a = 50

# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# print(New.a)

#7)Write a Python program to differentiate between static and instance variables.
# class College:
#     collegename = "Modern College" #Static variable (1 Memory)

#     def __init__(self):
#         self.studentname = "Monika" #Instance Variable (2 Separate Memory)

# principal = College()
# teacher = College()
# accountant = College()
# print("Principal = ",principal.collegename,"....",principal.studentname)
# print("Teacher = ",teacher.collegename,"....",teacher.studentname)
# print("Accountant = ",accountant.collegename,"....",accountant.studentname)

# College.collegename = "HBD"
# principal.studentname = "Monika Pagar"

# print("Principal = ",principal.collegename," | ",principal.studentname)
# print("Teacher = ",teacher.collegename," | ",teacher.studentname)
# print("Accountant = ",accountant.collegename," | ",accountant.studentname)

#8)Write a Python program to add and delete instance variables dynamically.
# class Student:
#     def __init__(self):
#         self.s_name = input("Enter Your Name : ")
#         self.s_rollno = 101     #instance variable

#     def getdata(self):
#         self.s_mb = 2828282828      #instance variable

# obj = Student()
# obj.getdata()
# obj.s_branch = "CS"     #adding instance variable by using object
# del obj.s_rollno        #deleting a instance variable
# print(obj.__dict__)

#9)Write a Python program to demonstrate static methods.
# class Student:
#     @staticmethod
#     def get_personal_detail(firstname,lastname):
#         print("Your Personal Detail : ", firstname," ",lastname)

#     @staticmethod
#     def contact_detail(mobil_no, rollno):
#         print("Your Contact Detail : ",mobil_no," ",rollno)

# Student.get_personal_detail("Monika", "Pagar")
# Student.contact_detail(7796928589,1001)

#10)Write a Python program to demonstrate single inheritance.
# class College:
#     def college_name(self):     #member function of college
#         print("Modern College")

# class Student(College):
#     def student_info(self):     #member function
#         print("Name : Monika Pagar")
#         print("Branch : MCA")

# obj = Student()     #object create child class
# obj.college_name()
# obj.student_info()

#11)Write a Python program to demonstrate multilevel inheritance.
# class College:
#     def college_name(self):     #member function of college
#         print("Modern College")

# class Student(College):
#     def student_info(self):     #member function
#         print("Name : Monika Pagar")
#         print("Branch : MCA")

# class Exam(Student):
#     def subject(self):
#         print("Subject 1 : Python")
#         print("Subject 2 : Java")
#         print("Subject 3 : Linux")

# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

#12)Write a Python program to demonstrate multiple inheritance.
# class SubMarks:     #Class - 1
#     math = 89
#     java = 90
#     c = 86
#     english = 91

# class PractMarks:       #Class - 2
#     cpract = 45

# class Result(SubMarks,PractMarks):      #Child Class
#     #Student will be pass 
#     def total(self):
#         if self.math >= 40 and self.java >= 40 and self.c >= 40 and self.english >= 40 and self.cpract >= 20:
#             print("Pass")
#         else:
#             print("Fail")

# obj = Result()
# obj.total()

#13)Write a Python program to implement an abstract class and abstract methods.
# from abc import ABC, abstractmethod
# class Help4code(ABC):   #abstract class
#     @abstractmethod     #decorator
#     def training(self):     #abstract method
#         pass

#     @abstractmethod     #abstract method
#     def placement(self):
#         pass

# class Ashish(Help4code):
#     def training(self):
#         print('C, C++, Java')
    
#     def placement(self):
#         print("Java Placement")

# class Ankush(Help4code):
#     def training(self):
#         print('Python | Django')
    
#     def placement(self):
#         print("Python Placement Student")

# class Prashant(Help4code):
#     def training(self):
#         print('Machine Learning')
    
#     def placement(self):
#         print("Data Science Placement")

# obj1 = Ashish()
# obj1.training()
# obj1.placement()

# obj2 = Ankush()
# obj2.training()
# obj2.placement()

# obj3 = Prashant()
# obj3.training()
# obj3.placement()

#14)Write a Python program to demonstrate abstraction using an online ticket booking system.
# from abc import ABC, abstractmethod
# class Irctc(ABC):
#     @abstractmethod
#     def bookTicket(self):   #abstract method
#         pass

# class MakeMyTrip(Irctc):
#     def bookTicket(self):   #abstract method
#         print("----------------------------------")
#         print("     Welcome to makemytrip.com       ")
#         #self.source = input("Enter a source station name : ")
#         #self.destination = input("Enter destination name")
#         #self.date = input("Enter Date : ")
#         print("     -----------------------------------     ")

# class GoIbibo(Irctc):
#     def bookTicket(self):   #abstract method
#         print("     ----------------------------------      ")
#         print("     Welcome to goibibo.com       ")
#         print("     -----------------------------------     ")

# class Yatra(Irctc):
#     def bookTicket(self):   #abstract method
#         print("     ----------------------------------      ")
#         print("     Welcome to yatra.com       ")
#         print("     -----------------------------------     ")

# m = MakeMyTrip()
# m.bookTicket()

# g = GoIbibo()
# g.bookTicket()

# y = Yatra()
# y.bookTicket()

#15)Write a Python program to demonstrate method overloading in Python.
# class Arithmetic:
#     def add(self, a):
#         print(a)

#     def add(self,a,b):
#         print(a+b)

#     def add(self,a,b,c):
#         print(a+b+c)

# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

#16)Write a Python program to demonstrate constructor overloading in Python.
# class Arithmetic:
#     def __init__(self):
#         print("There is no argument")

#     def __init__(self, a):
#         print("Passing one argument")

#     def __init__(self, a, b):
#         print("Passing two arguments")

# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(10,20)

#17)Write a Python program to demonstrate method overriding using inheritance.
# class Rbi:  #parent class
#     def homeLoan(self):
#         print("Home loan rate of Interest is 8%")

#     def carLoan(self):
#         print("Car loan rate of Interest is 7%")

# class Sbi(Rbi): #child class 
#     def homeLoan(self):
#         print("Home loan rate of Interest is 10.5%")
#         super().homeLoan()

# sbiObj = Sbi()
# sbiObj.homeLoan()
# sbiObj.carLoan()

#18)Write a Python program to demonstrate the use of the super() function with constructors.
# class Father:
#     def __init__(self):
#         print("Father : I am on time at breakfast table")

# class Child(Father):
#     def __init__(self):
#         print("Child : I will be late for breakfast")
#         super().__init__()

# obj = Child()

#19)Write a Python program to demonstrate public and private data members.
# class Base: #Base class
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "Monika"   #public data member
#         self.__c = "Divya"  #private data member
# #creating a derived class / child class
# class Derived(Base):
#     def __init__(self):
#         #Calling constructor of Base class
#         Base.__init__(self)
#         #print("calling private member of base class : ")
#         # print(self.a)
#         # print(self.__c) #Not Accessible

# # obj1 = Derived()
# # print(obj1.a)
# # print(obj1.__c)   #Not Accessible

# obj2 = Base()
# print(obj2.a)   #Accessible
# print(obj2.__c) #Not Accessible

#20)Write a Python program to demonstrate protected data members.
# class Base: #Base class
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "Monika"   #public data member
#         self._c = "Divya"  #private data member
# #creating a derived class / child class
# class Derived(Base):
#     def __init__(self):
#         #Calling constructor of Base class
#         Base.__init__(self)
#         # print("calling private member of base class : ")
#         # print(self.a)
#         # print(self._c)    #Accessible

# obj1 = Derived()
# # print(obj1.a)
# # print(obj1._c)   #Accessible

# # obj2 = Base()
# # print(obj2.a)   #Accessible
# # print(obj2._c)  #Accessible

#21)Write a Python program to demonstrate public and private methods in Python.
class Rbi:
    #Declaring public method
    def publicPolicy(self):
        print("Check the public policy of RBI")

    #Declaring private method
    def __privatePolicy(self):
        print("There is some private policy which is not accessible for public")

class Sbi(Rbi):
    def __init__(self):
        Rbi.__init__(self)  #Second Parent class constructor called

    def callingPublicMethod(self):  #child class public method
        print("\n Inside Child Class")
        self.publicPolicy() #calling parent class public method

    def callingPrivateMethod(self): #child class public method
        self.__privatePolicy()  #calling parent class private method

#obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()

# obj1.publicPolicy()
# obj1.__privatePolicy()

#obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()
