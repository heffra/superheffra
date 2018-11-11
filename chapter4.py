# Condition
num = 100
if num % 2 == 0:
    print("Even Number")
    print("Thank You")

num = input("Please enter a number : ")
num = int(num)
if num % 2 == 0:
    print("Even Number")
    print("Thank You")
else:
    print("Odd Number")
    print("Come Again")

num = input("Please enter a number : ")
num = int(num)
if num == 50:
    print("Half Century")
elif num == 100:
    print("Century")
elif num > 100:
    print("Century +")
else:
    print("Unknown number")

# Logical operators AND OR
num = 6
if num >= 3 and num < 5:
    print('3 to 5')
else :
    print('5 +')
    
num = -2
if num >= 3 or num == -2:
    print('3 + or -2')

#Compare String
name1 = input("Enter name 1 : ")
name2 = input("Enter name 2 : ")

if name1.lower() == name2.lower():
    print("Same Name")
else:
    print("Name doesn't match")

# Not equals to
name ="Unknown Person"
if name != 'Steve Jobs':
    print(name)

# Nested condition
x= 5
if x < 2:
    print('less than 2')
else:
    if x == 3:
        print('x is 3')
    else :
        if x == 5:
            print('x is 5')


# Iteration

# while loop
'''
while condition:
    body
'''

x =1
while x <= 500:
    print(x)
    x += 10

# Infinite loop
x = 1
while True:
    print(x)
    x += 10
    if x > 1000:
        break

# Omit even number 1 to 20
x= 0
while x < 20:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

# for loop
'''
for element in iterable:
    body
'''

# sum 1 to 10
sum = 0
for num in range(1, 22):
    print(num)
    sum += num
print("Sum is {sum}".format(sum=sum))

# string characters by for loop
title = "Hero Franesa"
for char in title:
    print(char)
