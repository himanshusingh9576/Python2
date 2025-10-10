# In tuple only some operation is possiblenot much as list
'''len()
negative indexing and positive indexing
slicing
count()
index() '''


tuple1 = ("hello", 2323, 3442, True, 4324.23)
tuple2 = tuple1
print(tuple1, id(tuple1))
print(tuple1, id(tuple2))
print(tuple1)
print(tuple1)
print(tuple1[2])
print(tuple1[-2])
print(len(tuple1))
print(type(tuple1))
# Slicing
tuple3 = (3, 4, 544, 422, 423, 43, 3)
print(tuple3[2:4])  #slicing
print(tuple3.count(4))
print(tuple3[2])
print(tuple3[3:5])