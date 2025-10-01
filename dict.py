info = {
    "sub1" : "Maths",
    "lis" : ["virat", "rohit"],
    "sub2" : "Science",
    "age" : 65,
    "12" : 23,
    'name' : "Himanshu" ,
    "religion" : {
        "hindu" : 44,
        "chris" : 23,
        
    }  
    
    
}
info.get("sub1")
print(info.get("sub1"))

## SET IN PYTHON
collection = {1,2,3,4,4,4, "hello"}
print(collection)
print(type(collection))

# set method
collection.add(10)
print(collection)
collection.remove("hello")
print(collection)
# collection.clear()
# print(collection)
collection.pop()
print(collection)
print(collection.pop())

# Set union method and intersection method
set1 = {1, 2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))

#store following word meaning in a python dictionary
store = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figure"]

}
print(store)

# you are a given list of subject for student
# Assume one classroom is required for 1 subject
#How many classroom are needed by all students
# classroom = {
#     "python", "java", "c++", "python",
#     "javascript", "java", "python", "java",
#     "c++", "c"
# }
# print(len(classroom))

# WAP to enter marks of 3 subject from the user
# and store them in a dictionary. start with
# an empty dictionary & add by one. Use subject
# name as key & marks as value
"""
stu1 = int(input("Enter Your Maths Marks:- "))
stu2 = int(input("Enter Your Phy Marks:- "))
stu3 = int(input("Enter Your Chem Marks:- "))
dict ={}
dict.update({"Maths": stu1})
dict.update({"Phy": stu2})
dict.update({"Chem": stu3})
print(dict)  """

# Figure out a way to store 9 & 9.0 as separate
# values in the set (you can take help of built-in data types)
set = {9, 9.0}
print(set)
 