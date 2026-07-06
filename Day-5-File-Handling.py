#1)Write a Python program to create a file in write mode and display its properties such as file name, mode, readability, writability, and closed status.
# f = open("myFile.txt","w")
# print("Name of File : ",f.name)
# print("File Mode : ",f.mode)
# print("Readable : ",f.readable())
# print("Writable : ",f.writable())
# print("File Closed: ",f.closed)

# f.close()
# print("File Closed: ",f.closed)

#O/P : 
# Name of File :  myFile.txt
# File Mode :  w
# Readable :  False
# Writable :  True
# File Closed:  False
# File Closed:  True

#2)Performing Write Operation
#Write a Python program to write multiple lines into a text file using the write() method.

# f = open("myFile.txt","w")
# f.write("\n Nashik is a Smart City")
# f.write("\n Pune is a Smart City")
# f.write("\n Banglore is a Smart City")
# f.write("\n Nagpur is a Smart City")
# f.close()
# print("File Operation is Done")

#O/P : 
#File Operation is Done

#3)Write a Python program to append data to an existing text file using append mode (a).
# f = open("myFile.txt","a")
# f.write("\n Nashik is a Smart City")
# f.write("\n Pune is a Smart City")
# f.write("\n Banglore is a Smart City")
# f.write("\n Nagpur is a Smart City")
# f.write("\n Indore is a Smart City")
# f.close()
# print("File Operation is Done")

#O/P : 
#File Operation is Done

#4)Write a Python program to write multiple strings into a file using the writelines() method.
# f = open("newFile.txt","w")
# mylist = ["Monika"," ","Neha"," ","Diya"]

# f.writelines(mylist)
# f.close()
# print("Written work has done Successfully")

#O/P : 
#Written work has done Successfully

#5)Write a Python program to read and display the contents of a text file using the read() method.
# f = open("newFile.txt","r")
# print(f.read())
# f.close()

#O/P : 
#Monika Neha Diya

#6)Write a Python program to write data into a file using the with statement (context manager).
# with open("myfile.txt","w") as f:
#     f.write("Monika \n")
#     f.write("Ashish \n")
#     f.write("Prasant \n")
#     print("File closed : ",f.closed)
# print("file closed : ",f.closed)

#7)Write a Python program to read a file using the with statement.
# with open("myfile.txt","r") as f:
#     content = f.read()
#     print(content)

#O/P : 
# Monika 
# Ashish 
# Prasant 

#8)Write a Python program to copy the contents of one binary file (e.g., an image) to another binary file.
# f1 = open("Photo-Passport.png","rb")
# f2 = open("Passport.png","wb")

# data = f1.read() #it will read entire binary information
# f2.write(data)

#csv File

#1)Write a Python program to store student details (Student ID, Roll No, Name, and Mobile Number) into a CSV file.
# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f) #here it will return csvwriter object
# # a .writerow(["studentid","rollno","name","mobileno"])

# studentid = int(input("Enter Student ID : "))
# rollno = int(input("Enter a Roll No. : "))
# name = input("Enter your Name : ")
# mobileno = int(input("Enter your Mobile No. : "))
# a.writerow([studentid,rollno,name,mobileno])
# print("Student Record has Saved!!")

#2) Write a Python program to accept student details, calculate the total marks, percentage, determine the result (Pass/Fail), 
# and save the record into a CSV file.
# rollno,name,monileno,p1,p2,p3,email
# calculate :
# total,percentage
# condition :
# if user is passed in all subject so save pass else save fail and passing marks
# 40

# import csv
# f = open("student2.csv","a",newline="")
# a = csv.writer(f) #here it will return csvwriter object
#a .writerow(["rollno","name","mobileno","p1","p2","p3","total","per","email","result"])

# rollno = int(input("Enter a Roll No. : "))
# name = input("Enter your Name : ")
# mobileno = int(input("Enter your Mobile No. : "))
# p1 = int(input("Enter Paper 1 Marks: "))
# p2 = int(input("Enter Paper 2 Marks: "))
# p3 = int(input("Enter Paper 3 Marks: "))
# email = input("Enter Email : ")

# total = (p1+p2+p3)
# per = total/3.0

# if p1 > 40 and p2 > 40 and p3 > 40:
#     result = "Pass"
# else:
#     result = "Fail"

# a.writerow([rollno,name,mobileno,p1,p2,p3,total,per,email,result])
# print("Student Record has Saved!!")