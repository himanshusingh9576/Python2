# Loops in python
# Loops are used to repeat instruction
# for loop and while loop
# count = 4
# while count<=5:
#     print("Himanshu")
#     count += 1

#Q1 print number from 1 to 100
# num = 1
# while num <= 100:
#     print(num)
#     num += 1
#   Q2.Print numbers from 100 to 1
"""
num2 = 100
while num2 >= 1:
    print(num2)
    num2 -= 1  """
# Print the multiplication table of a number n 
"""
n=2
m=1
while m<=10:
    # print(f"{n} *  {m} = {n*m}")
    print(f"{n} * {m} = {n*m}")
    m += 1   
"""

# Print the elements of the following list using a loop
"""
ele2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
ele3= 0

while ele3<len(ele2):
 
    print(ele2[ele3])
    ele3 += 1    """


# Print the element of the following list using loop
# heroes = ["ironman", "thor", "superman", "batman"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1
# Search for a number x in this tuple using loop:
"""
elex = (1, 4, 16, 25, 36, 49, 64, 81, 100)
elen = 36
eley = 0
while eley < len(elex):
    if elex[eley] == elen:
        print(eley)
    eley += 1
    """

# Break and Continue Keyword
'''
i = 1
while i <= 5:
    print(i)
    if i==3:
        break
    i += 1 '''

#Continue
# i = 0 
# while i <= 5:
#     if(i==3):
#         i += 1
#         continue
#     print(i)
#     i += 1
# Continue skip that mention element in if condition
# l = 2
# while l<=10:
    
#     if l==5:
#         l += 1
#         continue
        
#     print(l)
#     l += 1

# For loops in python
# veggies = ["potato", "brinjal", "Ladyfinger"]
# for val in veggies:
#     print(val)

# Q1 Using for loop print the element of the following list using a loop
# [1, 4, 16, 25, 36, 49, 64, 81,100]
# ele = [1, 4, 16, 25, 36, 49, 81, 100]
# ele1 = 1
# for ele1 in ele:
#     print(ele1)

#Q2 Search for a number x in this tuple using loop
#[1, 4, 16, 25, 36, 49, 81, 100]
# x = [1, 4, 16, 25, 36, 49, 81, 100]
# i = 16
# for el in x:
#     if el==i:
#         print(el)

# Range function returns a sequence of number starting 
# from 0 bby default and increment by 1 and stops before a specified number
"""
for i in range(10): #END
    print(i)
for i in range(2, 10): #start and stop
    print(i)
for i in range(3, 10, 3): #start , stop, step
    print(i)
"""
# for i in range(2, 22, 2):
#     print(i)

# print numbers from 1 to 100
# for i in range(1, 101, 1):
#     print(i)
#Print numbers from 100 to 1
# for i in range(100, 0, -1):
#     print(i)
# num = int(input("Enter Your Number:- "))

# for(i==1, i<=10, i++): ye python me nahi hota python me range se hota hai 
# for i in range(1, 11):
#     print(num * i)
#WAP to find the sum of first n numbers. Using while
num2 = int(input("Enter your number:- "))
i = 1
sum = 0
while i<=num2:
    sum += i
    i += 1
print(sum)

#WAP to find the factorial of first n numbers. (using for)
num3 = int(input("Enter user Input:- "))
i = 1
fact = 1
while i <= num3:
    fact *= i
    i += 1
print(fact)
