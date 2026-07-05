#1)Create a Person class with a constructor to initialize name and age, and display the details.
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display()
#         print("person1 is an Object with name = ",self.name,"Age = ",self.age)

#2)Write a Python program to demonstrate method overriding using inheritance.
# class Student:
#     def introduce(self,name,sid):
#         self.name = name
#         self.sid = sid
#         print("My name is ",self.name,", and my student ID is ",self.sid)
# class Student1(Student):
#     def introduce(self,name,sid):
#         self.name = name
#         self.sid = sid
#         print("My name is ",self.name,", and my student ID is ",self.sid)

# s1 = Student1()
# s1.introduce('Monika',101)

#3)Write a Python program to validate a student ID using a static method.
# class Student:
#     @staticmethod
#     def validate_student_id(sid):
#         if sid == 12345:
#             print("True")
#         else:
#             print("False")
# s1 = Student()
# Student.validate_student_id(12345)

#List

#1)Create a list and demonstrate indexing, slicing, and negative indexing.
# mylist = ["prashant", "Ashish", "Komal", "Ankush", "Ashish", 77, "Sandip", 60.52, "Monika"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# O/P : 
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# <class 'list'>
# prashant
# Ashish
# Komal
# Monika
# ['Komal', 'Ankush', 'Ashish']
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish']
# ['Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# ['Ashish', 'Ankush', 77, 60.52]
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# ['Monika', 60.52, 'Sandip', 77, 'Ashish', 'Ankush', 'Komal', 'Ashish', 'prashant']

#2)Write a Python program to update an element in a list.
# mylist = ["prashant", "Ashish", "Komal", "Ankush", "Ashish", 77, "Sandip", 60.52, "Monika"]
# print(mylist)
# mylist[2]="Akshay"
# print(mylist)

#O/P : 
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# ['prashant', 'Ashish', 'Akshay', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']

#3)Write a Python program to check whether a given element exists in a list.
# mylist = ["prashant", "Ashish", "Komal", "Ankush", "Ashish", 77, "Sandip", 60.52, "Monika"]
# print(mylist)
# if "Ankush" in mylist:
#     print("Yes Ankush is Available")
# else:
#     print("Not Available")

#O/P
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# Yes Ankush is Available

#4)Write a Python program to add elements to a list using append().
# mylist = ["prashant", "Ashish", "Komal", "Ankush", "Ashish", 77, "Sandip", 60.52, "Monika"]
# print(mylist)
# mylist.append("Harsh")
# mylist.append("Lakshman")
# print(mylist)

#O/P
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika', 'Harsh', 'Lakshman']

#5)Write a Python program to insert an element at a specific position using insert().
# mylist = ["prashant", "Ashish", "Komal", "Ankush", "Ashish", 77, "Sandip", 60.52, "Monika"]
# print(mylist)
# mylist.insert(1,"Sanket")
# print(mylist)

#O/P
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# ['prashant', 'Sanket', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']

#6)Write a Python program to remove an element from a list using remove().
# mylist = ["prashant", "Ashish", "Komal", "Ankush", "Ashish", 77, "Sandip", 60.52, "Monika"]
# print(mylist)
# mylist.remove("Sandip")
# print(mylist)

# O/P
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 60.52, 'Monika']

#7)Write a Python program to create a copy (clone) of a list.
# mylist = ["prashant", "Ashish", "Komal", "Ankush", "Ashish", 77, "Sandip", 60.52, "Monika"]
# print(mylist)
# newlist = mylist.copy() #cloning
# print(newlist)

#O/P
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']
# ['prashant', 'Ashish', 'Komal', 'Ankush', 'Ashish', 77, 'Sandip', 60.52, 'Monika']

#Multidimensional List
#1)Write a Python program to create and access a multidimensional list.
# mylist = [['monika','pagar'],['85.56'],[440022,'yyy']]
# print("Example of Multidimensional List")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

#O/P : 
# Example of Multidimensional List
# [['monika', 'pagar'], ['85.56'], [440022, 'yyy']]
# monika
# pagar
# 85.56
# 440022
# yyy

#2)Write a Python program to repeat a list using the * operator.
# list1 = ['monika','pagar']
# print(list1*3)

# #O/P : 
# ['monika', 'pagar', 'monika', 'pagar', 'monika', 'pagar']

#3)Write a Python program to concatenate two lists.
# list1 = ['monika','pagar']
# list2 = [50,25,50]
# print(list1+list2)

#O/P :
# ['monika', 'pagar', 50, 25, 50]

#4)Write a Python program to delete elements from a list using del.
# list2 = [50,25.50,'Monika']
# del list2[2]
# #del list2 
# print(list2)

#O/P
[50, 25.5]

#5)Write a Python program to clear all elements from a list.
# list2 = [50,25.50,'Monika']
# list2.clear()
# print(list2)

#O/P : 
[]

#6)Write a Python program to convert a string into a list.
# name = "Monika"
# print(name)
# myname = list(name) #typecasting
# print(myname)

#O/P : 
# Monika
# ['M', 'o', 'n', 'i', 'k', 'a']

#7)Write a Python program to reverse a list.
# mylist = [40,30,20,10]
# mylist.reverse()
# print(mylist)

#O/P : 
#[10, 20, 30, 40]

#8)Write a Python program to sort a list in ascending and order.
# mylist = [44,22,77,0,9,88]
# mylist.sort()
# print(mylist)

#O/P : 
#[0, 9, 22, 44, 77, 88]

#9)Write a Python program to sort a list in descending order.
# mylist = [44,22,77,0,9,88]
# mylist.sort(reverse=True) #Descending Order
# print(mylist)

#O/P : 
#[88, 77, 44, 22, 9, 0]

#Alising
#1)Write a Python program to demonstrate list aliasing
# mylist = [44,22,77,0,9,88]
# newlist = mylist #assigning the address
# print(id(mylist))
# print(id(newlist))
# mylist[0] = "monika"
# print(mylist)
# print(newlist)

#O/P : 
# 2255727212416
# 2255727212416
# ['monika', 22, 77, 0, 9, 88]
# ['monika', 22, 77, 0, 9, 88]

#Membership Operators : 
# 1. in 2. not in

#1)Write a Python program to demonstrate membership operators (in and not in).
# name = "monika"
# print("n" in name)
# print("p" not in name)

#O/P : 
# True
# True

#For loop
# for(start:end:step)
#1)Write Python programs using for loops with different range() variations.
# for i in range(5): #i starts with 0
#     print(i)

#O/P : 
# 0
# 1
# 2
# 3
# 4

#2)Write Python programs using for loops with different range() variations.
# for i in range(1,5): #i starts with 1
#     print(i)

#O/P : 
1
2
3
4

#3)Write Python programs using for loops with different range() variations.
# for i in range(1,10,2): 
#     print(i)

#O/P : 
# 1
# 3
# 5
# 7
# 9

#4)Write Python programs using for loops with different range() variations.
# for i in range(5,0,-1): 
#     print(i)

#O/P : 
# 5
# 4
# 3
# 2
# 1

#5)Write a Python program to print the multiplication table of 2.
# for i in range(1,11): 
#     print(i*2)

#O/P : 
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


#6)Write a Python program to print multiplication tables from 2 to 20.
# for i in range(1,11): 
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)

# print("------------------------------------------------------------------------------------")

# for j in range(1,11): 
#     print(j*11," ",j*12," ",j*13," ",j*14," ",j*15," ",j*16," ",j*17," ",j*18," ",j*19," ",j*20)
    
#7)Write a Python program to iterate through a list using a for loop.
# list3 = [10,20,30,40,50,]

# for i in list3:
#     print(i)

#O/P : 
# 10
# 20
# 30
# 40
# 50

#8)Write a Python program to calculate the sum of all elements in a list.
# list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for x in list:
#     sum += x
# print("The Sum is : ",sum)

#O/P : 
#The Sum is :  55

#9)Write a Python program to demonstrate the use of continue.
# mycart = [10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This is my purchased cart item")
#         continue
#     print(i)

#O/P :
# 10
# 20
# 200
# 300
# This is my purchased cart item
# 60
# This is my purchased cart item

#10)Write a Python program to demonstrate the use of break.
# mycart = [10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This is my purchased cart item")
#         break
#     print(i)

#O/P : 
# 10
# 20
# 200
# 300
# This is my purchased cart item

#11)Write a Python program to count odd numbers using a loop.
# count = 0
# for i in range(9):
#     if i%2 == 0:
#         print(i)
#     else:
#         print(i)
#         count += 1
# print("Count : ",count)

#O/P : 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# Count :  4

#12)Write a Python program to find the first even number in a list using break.
# rollno = [3,5,7,1,11,4,5,2]
# for x in rollno:
#     if x==2 or x==4 or x==6 or x==8 or x==10:
#         print("Even Number found : ",x)
#         break

#O/P : 
#Even Number found :  4

#13)WAP to accept any one day and check it is weekend or working day.(Mon-Fri Working Days)   
# day = input("Enter a Day : ").lower()

# if day == 'saturday' or day == 'sunday':
#     print(day,"is a Weekend Day")
# else:
#     print(day,"is a Working Day")

#14)Write a Python program to reverse a 3-digit number.
# num = 123 #321

# a = num % 10
# num = num // 10

# b = num % 10
# c = num // 10

# rev = a*100 + b*10 + c*1
# print("reverse : ",rev)

#15)Write a Python program to reverse a 7-digit number.
# num = 1234567

# a = num % 10
# num = num // 10

# b = num % 10
# num = num // 10

# c = num % 10
# num = num // 10

# d = num % 10
# num = num // 10

# e = num % 10
# num = num // 10

# f = num % 10
# num = num // 10

# g = num % 10
# h = num // 10

# rev = a*10000000 + b*1000000 + c*100000 + d*10000 + e*1000 + f*100 + g*10 + h*1
# print("reverse : ",rev)

#16)Write a Python program to calculate the minimum number of currency notes required for a withdrawal amount.
# Amount = int(input("Enter amount for withdraw : "))

# print("100 notes = ",Amount//100)
# print("50 notes = ",(Amount % 100) //50)
# print("20 notes = ",((Amount % 100) %50) //20)
# print("10 notes = ",(((Amount % 100) %50) %20) //10)
# print("5 notes = ",((((Amount % 100) %50) %20) %10) //5)
# print("2 notes = ",(((((Amount % 100) %50) %20) %10) %5) //2)
# print("1 notes = ",((((((Amount % 100) %50) %20) %10) %5) %2) //1)

#17)Write a Python program to find the maximum of three ages using nested if-else.
# Nested if else :
#WAP to accept a three age and check maximum age and print.

# a1 = int(input("Enter 1st Age : "))
# a2 = int(input("Enter 2nd Age : "))
# a3 = int(input("Enter 3rd Age : "))

# if a1 > a2:
#     if a1 > a3:
#         print("1st Age is Greater")
#     else:
#         print("3rd Age is Greater")
# else:
#     if a2 > a3:
#         print("2nd Age is Greater")
#     else:
#         print("3rd Age is greater")

#18)WAP to accept a any one character and check the entered character is UPPER CASE, LOWER CASE, DIGIT, SPECIAL SYMBOL so print msg with respect to the entered character.
# ch = input("Enter a character : ")

# if ch.isupper():
#     print("Character is UPPER CASE")
# elif ch.islower():
#     print("Character is LOWER CASE")
# elif ch.isdigit():
#     print("Character is DIGIT")
# else:
#     print("Character is SPECIAL SYMBOL")

# 19)Write a Python program to classify a character using its ASCII value.
# ch = ord(input("Enter any character : "))

# ord function used to convert in ASCII code
# if ch >= 65 and ch <= 91:   #A=65
#     print("Your entered character is in Upper Case")
# elif ch >= 97 and ch <= 122:    #a=97
#     print("Your entered character is in Lower Case")
# elif ch <= 48 and ch <= 57: #0=48
#     print("Your entered character is in Special Symbol")

# 20)Write a Python program to validate a username and password.
# username = input("Enter Username : ").lower()
# Password = input("Enter Password : ").lower()

# if username == Password:
#     print("Login Successfully!!")
# else:
#     print("Invalid Login")

# 21)Write a Python program to repeatedly ask for login credentials until they are correct.
# while(True):
#         username = input("Enter Username : ").lower()
#         Password = input("Enter Password : ").lower()

#         if username == Password:
#             print("Login Successfully!!")
#             break
#         else:
#               print("Invalid Login")

#22)Write a Python program to demonstrate the find() method.
# s = "help4code is a best platform for practicing programming"

# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))

#find() return starting index number of string if it found else if string doesn't exist then it return -1

#23)Write a Python program to join multiple strings using join().
# s = "Monika", "Neha", "Diya"
# m = '|'.join(s)
# print(m)

#24)Write a Python program to demonstrate string case conversion methods (lower(), upper(), swapcase(), title(), capitalize()).
# s = "Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

#25)Write a Python program to format strings using format() and f-strings.
# print('Subject Marks : ')
# phy = 50
# chem = 60
# math = 70

# print("physics ={}  chemistry ={}   math ={}".format(phy,chem,math))
# print("physics ={0}  chemistry ={1}   math ={2}".format(phy,chem,math))
# print("physics ={x}  chemistry ={y}   math ={z}".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total Marks : ",f"{total}")
# print("Roll No : ","7".zfill(4))

#26)Write a Python program to iterate through each character of a string.
# name = "help4code"

# for i in name:
#     print(i)

#27)Write a Python program to find the index of a specific character in a string.
name = "monika"
# i = 0
# for x in name:
#     if x == 'n':
#         print("The character is present at index no. ",i," Value = ",x)
#         break
#     i = i + 1 #update by 1

#28)Write a Python program to print all occurrences of the character 'w' from the string "shiwaleew" using a for loop.
# a = 'shiwaleew'
# for i in a:
#     if i == 'w':
#         print(i)

#29)Write a Python program to compare two lists using comparison operators.
# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]

# print(x==y)
# print(x==z)
# print(x!=z)

#30)Write a Python program to evaluate arithmetic expressions using operator precedence.
# a = 50
# b = 30
# c = 20
# d = 10

# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

#31)Write a Python program to remove leading and trailing spaces from a string.
#Removing spaces from the string :
#1. rstrip()===>To remove spaces at right hand side
#2. lstrip()===>To remove spaces at left hand side
#3. strip()===>To remove spaces at both sides

# city = input("Enter your city Name : ")
# scity = city.strip()
# if scity == 'Hydrabad':
#     print("Hello Hydrabadi..Adab")
# elif scity == 'Chennai':
#     print("Hello Madrasi..Vanakkam")
# elif scity == "Banglore":
#     print("Hello Kannadiga..Shubhodaya")
# else:
#     print("Your entered city is invalid")

#32)Write a Python program to replace a substring using replace().
#Replacing a string with another string:
#s.replace(oldstring,newstring)
#inside s, every occurrence of oldstring will be replaced with new string

# s = ""
# s1 = s.replace("difficult","easy")
# print(s1)

# #All occurrences will be replaced
# s = "abababababab"
# s1 = s.replace("a","b")
# print(s1)

#33)Write a Python program to count the number of special characters in a string.
str1 = 'gasaa54@#vscsd!s*'
cnt = 0
for i in str1:
    if i == '@' or i == '!' or i == '#' or i == '$' or i == '%' or i == '&' or i == '*' or i == '^':
        cnt += 1

print(cnt)
