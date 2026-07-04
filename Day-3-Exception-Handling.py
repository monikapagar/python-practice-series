# #Predefined Exception

#1)Write a Python program to perform division of two numbers using 
# a try-except block. Handle the exception when the denominator is zero.

# a = int(input("Enter value of A : "))
# b = int(input("Enter value of B : "))
# try: 
#     print(a/b)
# except:
#     print("Cannot divide by Zero")
# print("Continue")

#2)Write a Python program to accept two integer inputs from the user and handle 
# both ZeroDivisionError and ValueError using separate except blocks.

# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by Zero")
# except ValueError:
#     print("Enter only Integer Value")

#3)Write a Python program to display the actual exception message using 
# the as keyword while handling ZeroDivisionError and ValueError.

# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except ZeroDivisionError as message:
#     print("Cannot divide by Zero : ",message)
# except ValueError as message:
#     print("Enter only Integer Value : ",message)

#4)Handling multiple different kinds of exceptions with single except block
# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)

#5)If we have requirement of multiple except block then in that situation default except block 
# should be in the last otherwise syntax error will encountered.

# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# except: #Default except block
#     print("This is default block of except block")

#6)We can use else block if no error will generate it is depend on our own need and neccessity

# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# else: 
#     print("Everything is ok!")

#7)Finally Block will always executes whether try block generates error or not
# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print("Enter Correct Number ",message)
# finally:
#     print("I will always execyted!")

#8)Nested try-except block
# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     try:
#         print(a/b)
#     except ZeroDivisionError as message:
#         print("Cannot Divide by Zero ",message)
# except ValueError as message:
#     print("Enter Correct Number ",message)

#9)Write a Python program that demonstrates the combined use of try, except, else, and finally blocks.
# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print("Enter Correct Number ",message)
# else:    
#     print("There is no error in try block")
# finally:
#     print("I am Finally block, I will always execyted!")

# #Userdefined Exception

#1)User defined exception by raise keyword

# bank_bal = 5000
# if bank_bal < 2000:
#     raise Exception("Your account balance is below a accessing limit")
# else:
#     print("Your amount has withdrawal")

# #Logging File Configuration
#1)Write a Python program to configure logging and record different 
# logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) into a log file.

# import logging

# logging.basicConfig(filename="newFile.txt",level=logging.DEBUG)
# logging.debug("This indicates the debugging information")
# logging.info("This indicates the important information")
# logging.error("This indicates the error information")
# logging.warning("This indicates the warnning information")
# logging.critical("This indicates the critical information")

#2)Write a Python program to perform division of two numbers 
# and log the exception details into a log file if an error occurs.

# import logging
# logging.basicConfig(filename="arithmetic.txt.txt",level=logging.DEBUG)
# try: 
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)

# print("Logging level is set up. Check 'arithmetic.txt' fot log details")

#Example : WAP to accept three paper marks like phy, chem, math and calculate total, percentage and display total 
# marks, percentage 
# Condition :
#If user is passed in all subject then print pass else print fail and passing marks is 40.
#If percentage is greater than equal to 65 and gender is male then print you are eligible for 
# placement else not eligible for placement

# phy = int(input("Enter marks of Physics : "))
# chem = int(input("Enter marks of Chemistry : "))
# math = int(input("Enter marks of Mathematics : "))

# total = phy + chem + math
# per = (total/300)*100

# print("Total Marks : ",total)
# print("Percentage : ",per)

# if phy >= 40 and chem >= 40 and math >= 40:
#     print("Pass")
# else:
#     print("Fail")

# gender = input("Enter Your Gender M/F : ")
# if per >= 65 and gender == 'M':
#     print("You are eligible for Placement")
# else:
#     print("You are not eligible for placement")




