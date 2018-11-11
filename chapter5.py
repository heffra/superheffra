# List
name = ['Hero', 'Risa', 'Clara']
print(name)
print(name[0])
print(name[1])

# Mixed list
mix_list = ['Hero', 22, True]
print(mix_list)

# last element of list
print(mix_list[-1])

# empty list
'''
name =[]
print(name[0])
'''

# Nested list
matrix = [ [1, 2, 3, 4, 5],
           [4, 5, 6, 7, 8],
           [2, 2, 2, 2, 2],
           [0, 0, 0, 0, 0],
         ]

for x in matrix:
    for y in x:
        print(y, end=' ')
    print()

# list slicing
number_list = [1, 2, 3, 4, 5,]
print(number_list[0:2])
print(number_list[2:-1])