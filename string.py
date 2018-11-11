title = "Hero Enterprise"
title1 = 'Program Python'

print(title)
print(title1)

print(title[0], title[1], title[-1], title[-2])

name = 'Hero Franesa'
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'Hero'
last_name = 'Franesa'
name = first_name + ' ' + last_name
print(name)
print(first_name + ' ' + last_name)
print(first_name + '\n' + last_name)

name = "          Mr.H          "
print('_' + name + '_')
print('_' + name.lstrip()+ '_')
print('_' + name.rstrip() + '_')
print('_' + name.strip() + '_')
print('_' + name.lstrip().rstrip() + '_')

print('Hero\'s Enterprice')

filename = 'database.txt'
print(filename.endswith('.txt'))
print(filename.startswith('data'))

sentence = "my name is Hero franesa, my hobby is watching anime"
print(sentence.find("hero"))
print(sentence.find("hiro"))

sentence = sentence.replace("Hero", "Harlequin")
print(sentence)

x = 'Hero'
y = 'Clara'
z = 'Risa'

print(x + ' | ' + y + ' | ' + z)
print(x, y, z, sep=' | ')

person = '%s\'age is %d'
print(person % ('Billy', 55))
print()

person = '{name}\'s age is {age}'
print(person.format(name= 'Hero', age= 21))
print(person.format(name= 'Risa', age= 21))

name = 'Hero'
age = 21
person = f'{name}\'s age is {age}'
print(person)

name = 'Hero Franesa'
print(name[0:4])