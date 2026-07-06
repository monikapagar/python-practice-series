#Dictionary : We represent data as a key value pair
#1)Write a Python program to create a dictionary with different types of keys and values.
# mydict = {
#     101: "monika",
#     102: "ashish",
#     "103": "mohini",
#     "104": "triveni",
#     101: "ashish",
#     104: "ashish" 
# }

# print(mydict)
# print(type(mydict))

#O/P : 
# {101: 'ashish', 102: 'ashish', '103': 'mohini', '104': 'triveni', 104: 'ashish'}
# <class 'dict'>

#2)Write a Python program to access a dictionary value using its key.
# mydict = {
#     101: "monika",
#     102: "ashish",
#     "103": "mohini",
#     "104": "triveni",
#     101: "ashish",
#     104: "ashish" 
# }

# print(mydict)
# #With the help of key we have to print values
# a = mydict[102]
# print(a)

#O/P : 
# {101: 'ashish', 102: 'ashish', '103': 'mohini', '104': 'triveni', 104: 'ashish'}
# ashish

#3)Write a Python program to update the value of an existing key in a dictionary.
# mydict = {
#     101: "monika",
#     102: "ashish",
#     "103": "mohini",
#     "104": "triveni",
#     101: "ashish",
#     104: "ashish" 
# }

# #We will replace old value by new values
# mydict[102] = "peter"
# print(mydict)

#4)Write a Python program to iterate through and print all keys of a dictionary.
# mydict = {
#     101: "monika",
#     102: "ashish",
#     "103": "mohini",
#     "104": "triveni",
#     101: "ashish",
#     104: "ashish" 
# }

# #only print key 
# for x in mydict:
#     print(x)

#O/P : 
# 101
# 102
# 103
# 104
# 104

#5)Write a Python program to iterate through and print all values of a dictionary.
# mydict = {
#     101: "monika",
#     102: "ashish",
#     "103": "mohini",
#     "104": "triveni",
#     101: "ashish",
#     104: "ashish" 
# }
# #only print values 
# for x in mydict.values():
#     print(x)

#O/P : 
# ashish
# ashish
# mohini
# triveni
# ashish

# #6)Write a Python program to print both keys and values of a dictionary using the items() method.
# mydict = {
#     101: "monika",
#     102: "ashish",
#     "103": "mohini",
#     "104": "triveni",
#     101: "ashish",
#     104: "ashish" 
# }
# #printing key and values 
# for x,y in mydict.items():
#     print(x,y)

#O/P : 
# 101 ashish
# 102 ashish
# 103 mohini
# 104 triveni
# 104 ashish

#7)Write a Python program to add a new key-value pair to a dictionary.
# mydict = {
#     101: "monika",
#     102: "ashish",
#     "103": "mohini",
#     "104": "triveni",
#     101: "ashish",
#     104: "ashish" 
# }
# #printing key and values 
# mydict["mobile_no"] = 123567890
# print(mydict)

#O/P : 
# {101: 'ashish', 102: 'ashish', '103': 'mohini', '104': 'triveni', 104: 'ashish', 'mobile_no': 123567890}

#8)Write a Python program to remove a key-value pair from a dictionary using the pop() method.
# mydict = {
#     101: "monika",
#     "professional": "developer",
#     "empid": 1001
# }
# mydict.pop(101)
# print(mydict)

#O/P : 
# {'professional': 'developer', 'empid': 1001}

#9)Write a Python program to create a copy (clone) of a dictionary.
# mydict = {
#     101: "monika",
#     "professional": "developer",
#     "empid": 1001
# }
# newdict = mydict.copy()
# print(newdict)

#O/P : 
# {101: 'monika', 'professional': 'developer', 'empid': 1001}

#10)Write a Python program to check whether a dictionary is empty or not.
# mydict = {
#     101: "monika",
#     "professional": "developer",
#     "empid": 1001
# }
# if mydict == {}:
#     print("Dictionary is Empty")
# else:
#     print("Dictionary is Not Empty")

#O/P :
#Dictionary is Not Empty

#11)Write a Python program to find the key with the maximum value in a dictionary.
# mydict = {
#     "A": 50,
#     "B": 30,
#     "C": 70
# }
# max_key = ""
# max_value = 0

# for key in mydict:
#     if mydict[key] > max_value:
#         max_value = mydict[key]
#         max_key = key

# print(max_key)

#O/P : 
#C

#12)Write a Python program to reverse the keys and values of a dictionary.
# mydict = {
#     "A": 1,
#     "B": 2,
#     "C": 3
# }
# reverse_dict = {}

# for key in mydict:
#     reverse_dict[mydict[key]] = key

# print(reverse_dict)

#O/P :
# {1: 'A', 2: 'B', 3: 'C'}
 
#13)Write a Python program to find the common key-value pairs between two dictionaries.
dict1 = {
    "A": 1,
    "B": 2,
    "C": 3
}
dict2 = {
    "B": 2,
    "C": 4,
    "D": 5
}

common = {}

for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        common[key] = dict1[key]

print("Common key-value pairs:")
print(common)

#O/P : 
# Common key-value pairs:
# {'B': 2}