# Lists

# objects = ['apple', 'car', 'plane', 'tree']
#
# for i in objects:
#     print(i)
#
# for m in range(len(objects)):
#     print('I have a',objects[m])

# list commands: append

# fruit = list()
# fruit.append('apple')
# fruit.append('banana')
# print(fruit)

# Is the item present in the list?

# num_list = [1, 2, 3, 4, 5, 'seven']
#
# print(2 in num_list)
# print(6 in num_list)
# print('seven' in num_list)
# print(3 not in num_list)

# Experimentation with using a list to sum and Average

# num_list = list()
# while True:
#     num = input('Enter a number:')
#     if num == 'Done':
#         break
#     try:
#         num_list.append(int(num))
#     except:
#         print('input not recognised')
#         continue
# print(num_list)
# avg = sum(num_list)/len(num_list)
# print('Average is:', avg)

# Strings and Lists
# fruits = 'apple banana orange'
# words = fruits.split()
# print(fruits, words)

# Uising different delimeters in split

# fruits = 'orange;apple;banana'
# words = fruits.split(';')
# print(words)

# Experimenting

# fopen = open('mbox-short.txt')

# for line in fopen:
#     line = line.rstrip()
#     if line.startswith('From'):
#         words = line.split()
#         if len(words) <3:
#             continue
#         print(words[2])

# fhand = open('mbox-short.txt')
#
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From'):
#         continue
#     words = line.split()
#     if len(words) <3:
#         continue
#     print(words[2])

# Exercise 8.4

# fopen = open('romeo.txt')
# unique = list()
#
# for line in fopen:
#     line = line.rstrip()
#     words = line.split()
#     for i in words:
#         count = words.count(i)
#         if count == 1:
#             unique.append(i)
# unique.sort()
# print(unique)


# Removes repeated words
# fopen = open('romeo.txt')
# unique = list()
#
# for line in fopen:
#     line = line.rstrip()
#     words = line.split()
#     for letter in words:
#         if letter in unique:
#             continue
#         else :
#             unique.append(letter)
#     print(line)
# print(unique)

# Exercise 8.5

fopen = open('romeo.txt')
count = 0

# for line in fopen:
#     line = line.rstrip()
#     words = line.split()
#     print(words)
#     for word in words:
#         if word == 'From':
#             print(words[1])
#             count = count + 1
# print('The file contains', count, 'lines with From as the first word')

# Alternatlively
fopen = open('mbox-short.txt')

for line in fopen:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])

# Exercise 8.6
# numbers = list()
#
# while True:
#     number = input('Enter a number:')
#     if number == 'Done':
#         break
#     try:
#         number = int(number)
#         numbers.append(number)
#     except:
#         print('Input not recognised!')
#         continue
# print(numbers)
# print('The largest number is:', max(numbers))
# print('The smallest number is:', min(numbers))
