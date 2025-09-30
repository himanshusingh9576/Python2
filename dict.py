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
classroom = {
    "python", "java", "c++", "python",
    "javascript", "java", "python", "java",
    "c++", "c"
}
print(len(classroom))