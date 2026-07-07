#1)Write a Python program to implement a menu-driven Stack application with the following operations:
# Push
# Pop
# Peek
# Display
# Delete Stack
# Exit

# import sys
# class Stack:
#     def __init__(self,stackSize):
#         self.stackSize = stackSize #Stack size define
#         self.myStack = [] #list represents stack
#         print("Stack has Created!")

#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True
#         else:
#             return False
    
#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False

#     def push(self,value):
#         if self.isFull():
#             print("Stack is Full")
#         else:
#             self.myStack.append(value)

#     def display(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("Stack elements are : ",self.myStack)

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("Poped Element : ",self.myStack.pop()) 
#             #print(self.myStack[-1]) 

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("Peeked Element : ",self.myStack[-1])

#     def deleteStack(self):
#         self.myStack = None #del self.myStack
#         print("Stack is Deleted Successfully!")

# size = int(input("Enter the size of Stack : "))
# obj = Stack(size)

# while True:
#     print("1. Push")
#     print("2. Display")
#     print("3. Pop")
#     print("4. Peek")
#     print("5. Delete Stack")
#     print("6. Exit")
#     choice = int(input("Enter your choice : "))
#     if choice == 1:
#         value = int(input("Enter a value to push in a Stack : "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteStack()
#     elif choice == 6:
#         sys.exit()

#2)Write a Python program to demonstrate the use of string validation methods: isalnum(), isalpha(), 
# isdigit(), islower(), isupper(), istitle(), isspace(), startswith(), and endswith().

print('monikapagar777'.isalnum()) #True
print('monikapagar'.isalpha()) #True
print('777f'.isdigit()) #False
print('sdsdsdsd'.islower())#True
print(''.islower())#False
print('MONIKA'.isupper())   #True
print('My Name Is Monika'.istitle())    #True
print(''.istitle()) #False
print(''.isspace()) #False
print('Hello'.startswith("He"))#True
print('Hello'.endswith("lo"))#True




