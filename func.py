"""
def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
cal_avg(98, 73, 88)
cal_avg(1, 2, 3)
"""

#calculate sum
'''
def calc_sum(a, b):# function and parameters
    sum=a+b
    print(sum) 
    # return a + b
calc_sum(3, 4)# function call
calc_sum(6, 6)# function call
calc_sum(4, 8)# function call 
'''
# New function
# def print_hello():
#     print("hello")
# print_hello()

# Calculate average

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum/3
#     print(avg)
#     return avg
# calc_avg(4, 5, 6)

# FUNCTION are three types 
# 1. In-Built Function
# 2. Module Function
# 3. Useer-Defined function

# Built-In Function
# print("Himanshu", end=" ")
# print("Singh")

# len()
# type()
# range()

## Default parameter
'''def mul_num(a=2, b=1): # default parameter
    print(a * b)
    # return a * b
mul_num()'''

#   Q1. WAF to print the length of a list. (list is the paramenter)
''' cities = ["Delhi", "Noida", "Gurgaon", "Pune"]
heroes = ["thor", "ironman", "superman", "shaktiman"] 
def print_len(cities):
    print(len(cities))   
print_len(cities)
print_len(heroes) '''

#Q2. WAF to print the elements of a list in a single line.(list is the parameter)
''' hero = ["thor", "ironman", "captain america", "shaktiman"]
print(hero[0], end=" ")
print(hero[1])

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(hero)  
print()  '''

#Q3 WAF to find factorial of n.(n is thee parameter)
''' n=5
def factorial(n):
    fact = 2
    for i in range(1, n+1):
        fact *= i
    print(fact)
factorial(5) '''

#Q4 WAF to convert USD TO INR
'''def con_money(usd):
    # usd = n
    inr = usd * 85
    print(usd, "USD =", inr, "INR")
con_money(2)'''

#make a function enter a number and find that number is even or odd
'''def decl_eo(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
decl_eo(6) '''

# RECURSION
"""
def show(n):
    # base case
    if n==6:
        return
    #recursive case
    print(n)
    show(n+1)
    # print('END')
show(1)  """

# Recursion through factorial
'''
def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1) * n
print(fact(5))  '''

# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n, end=" ")
   
# fun(3)

## Q1. Write a recursive function to calculate the sum
# of first n natural number
'''
def cal_sum(n):
    if n==0: 
        return 0
    return cal_sum(n-1) + n
sum=cal_sum(5)  
print(sum)   '''

##Q2. WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENT IN
# A LIST (HINT:- USE LIST AND INDEX AS PARAMETERS)
'''
def print_list(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["mango", "orange", "litchi", "apple", "banana"]
print_list(fruits)    '''


## File input/output in python
'''
f = open("demo.txt", "r")

data = f.read()
print(data)
# data = f.read(5)
line1 = f.readline() 
print(line1)
line2 = f.readline()
print(line2)
# print(data)
# print(type(data))
f.close()
#Reading a file    '''

## Write a file
'''
f=open("demo.txt", "w")

f.write("I want to leanrn js")
f.close()  '''

## If we have change in file
'''
f2 = open("demo.txt", "a")
f2.write("Then i will move to reactjs")
f2.close() '''

## Deleting a file
# import os
# os.remove("demo.txt")

## Practice question
#   Q1. CREATE A NEW FILE "prctice.txt" using python. add 
# the following data in it
'''
with open("practice.txt", "w") as f:
    f.write("Hi everyone\n we are learning File I/O\n")
    f.write("using java.\n I like programming in java.")
    '''

#Q2.WAF that replace all occurances of java with python on above file
'''with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("java", "Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)  '''

##Q3.Search if the word "learning" exiists in the file or not
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")

 

    




    
