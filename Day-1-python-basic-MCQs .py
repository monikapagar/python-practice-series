#Q1-Print alternate elements of a list using slicing.
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
print("****************")

#2-Demonstrate slice assignment on alternate elements of a list.
'''
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a) 
print("****************")'''

#3-Print elements of a list in reverse using slicing
a=[1,2,3,4,5]
print(a[3:0:-1])
print("****************")

 #4-Remove and print the last element from each row of a 2D list using pop().
'''
arr=[[1,2,3,4],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15]]
for i in range(0,):
    print(arr[i].pop())
    print("****************")'''

#5-Predict the output of a function with a mutable default argument.
def f(i, values =[]):
    values.append(i)
    print(values)
f(1)
f(2)
f(3)
print("****************")

#6-Shift all elements of a list one position to the left.
arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
for i in range(0,6):
    print(arr[i],end=" ")
print("****************")

#8-Explain the difference between list assignment and list copying using [:].
fruit_list1=['']
fruit_list2=fruit_list1
fruit_list3=fruit_list1[:]  #.....copy
fruit_list2[0]= 'Guava'
fruit_list3[1]="Kiwi"

sum=0 
for Is in (fruit_list1,fruit_list2,fruit_list3):
print("****************")

#9-Predict the output of a loop using zip() and continue
for i ,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i," ",j)
print("****************")

#10-Explain what happens when calling init_tuple.__le__() without an argument.
init_tuple=()
print(init_tuple.__le__())

#11-Compare two tuples and determine whether they are equal.
init_tuple_a = 'a','b'
init_tuple_b = ('a','b')
print(init_tuple_a==init_tuple_b)

#12-Predict the output of tuple multiplication using the list length
l=[1,2,3]
init_tuple=('python',)*(l.__le__() -l[::-1][0])
print(init_tuple)

#13-Create a single-element tuple and explain the syntax.
init_tuple = ('python')

#14-Access a dictionary value using a tuple as the key
a={(1,2):1,(2,3):2,(4,5):3}
print(a[(4,5)])

#15-Explain what happens when accessing a dictionary with a['a','b'].
a={'a':1,'b':2,'c':3}
print(a['a','b'])

#16-Count the occurrences of fruit names using a dictionary.
fruit =  {}
def addone(index):
    if index in fruit:
        fruit[index] +=1
    else:
        fruit[index]=1 
addone('Apple')
addone('Bpple')
addone('apple')
print(len(fruit))

#17-Demonstrate how integer and string keys (1 and '1') behave in a dictionary.
arr={}
arr[1]=1
arr['1']=2
arr[1] +=1

sum = 0
for k in arr:
    sum +=arr[k]
print(sum)

#18-Explain why 1 and 1.0 refer to the same dictionary key.
my_dict={}
my_dict[1]=1
my_dict['1']=2
my_dict[1.0]=4
print(my_dict)
sum=0
for k in my_dict:
    sum += my_dict[k]
print(sum)

#19-Use tuples as dictionary keys and calculate the sum of dictionary values.
my_dict={}
my_dict[1,2.4]=8
my_dict[4,2,1]=10
my_dict[1,2]=12
sum=0
for k in my_dict:
    sum += my_dict[k]
print(sum)
print(my_dict)

#20-Create nested dictionaries (box, jars, and crates) and access their contents
box = {}
jars = {}
crates = {}
box['biscuit']=1
box['cake']=3
jars['jam']=4
crates['box']=box
crates['jars']=jars
print(len(crates[box]))

#21-Print dictionary values in the order of sorted keys.
dict = {'c':97,'a':96,'b':98}
for _ in sorted(dict):
    print(dict[_])

#Addressing
math=50
chem=50
phy=50
print(id(math))
print(id(chem))
print(id(phy))

#22-Demonstrate the use of id() and dictionary copying.
rec={"name":"python","Age":"20"}
r=rec.copy()
print(id(r)==id(rec))
print(id(r))
print(id(rec))

#23-Demonstrate type conversion using int(), float(), and bool().
rec = {"Name":"python","Age":"20","Addr":"NJ","Country":"USA"}
id1=id(rec)
del rec
rec = {"Name":"python","Age":"20","Addr":"NJ","Country":"USA"}
id2=id(rec)
print(id1==id2) 

#Typecasting
print(int(3.14))
print(int(True))
print(int(False))
print(int("4"))

#print(int(10+5j))
#print(int("4.22"))

print(float(3))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))

#print(Float(3))

print(bool())

#24-Move all zeros in a list to the end.
val= [0,1,0,3,12]
for i in val:
    if i ==0:
        val.remove(i)
        val.append(i)
print(val)

#25-Find the common elements among three lists.  
A=[1,2,3]
B=[2,3,4]
C=[3,4,5]

for i in A:
    if i in B and i in C:
        print(i)


#26-Find the maximum number of consecutive 1s in a binary list.
val=[1,1,0,1,1,1,0,1,1,1,1]
count=0
max=0
for i in val:
    if i ==1: 
        

#27-Check whether a list is a palindrome.
list=[1,2,3,2,1]
if list[::-1]:
    print("Number is palindrome")
else:
     print("Number is not palindrome")

A=[1,2,3,2,1]
if A[:] == A[::-1]:
     print("Number is palindrome")
else:
     print("Number is not palindrome")

#28-Reverse a string.
string="hello"
rev=string[::-1]
print(rev)

'''name="hello"
N=len(name)-1
newname=""
for i in range(N,0,-1):
    newname += name[i]
print(newname)'''
   

#29-Remove duplicate characters from a string while preserving their order.
name="Programming"
newname=" "
for i in name:
    if i not in newname:
        newname += i
print(newname)

