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
l = 2
while l<=10:
    
    if l==5:
        l += 1
        continue
        
    print(l)
    l += 1

# For loops in python

   
