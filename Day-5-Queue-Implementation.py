#1)Write a Python program to implement a Queue using a class. Implement the following operations using a menu-driven approach:
# Enqueue (Insert an element)
# Dequeue (Remove an element)
# Display the queue
# Peek the front element
# Check whether the queue is full
# Check whether the queue is empty
# Delete the queue
# Exit the program
#Use a list to implement the queue and handle overflow and underflow conditions appropriately.

import sys
class Queue:
    def __init__(self,queueSize):
        self.queueSize = queueSize
        self.myQueue = []

    def isFull(self):
        if len(self.myQueue) == self.queueSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False
        
    def enQueue(self,value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.myQueue.append(value)

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.myQueue)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.myQueue.pop(0))
    
    def frontPeek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Peeked Element : ",self.myQueue[0])
    
    def delete(self):
        self.myQueue = None
        print("Queue is Deleted Successfully!!")

size = int(input("Enter the Size of Queue : "))
queObj = Queue(size)
while True:
    print("1. enQueue")
    print("2. Display")
    print("3. deQueue")
    print("4. frontPeek")
    print("5. Delete Queue")
    print("6. Exit")
    
    choice = int(input("Enter your Choice : "))
    if choice == 1:
        value = int(input("Enter a value to add in Queue : "))
        queObj.enQueue(value)
    elif choice == 2:
        queObj.display()
    elif choice == 3:
        queObj.deQueue()
    elif choice == 4:
        queObj.frontPeek()
    elif choice == 5:
        queObj.delete()
    elif choice == 6:
        sys.exit()
    