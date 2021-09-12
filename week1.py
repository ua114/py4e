# Using strong functions
# fruit = 'banana'
# print(len(fruit)) #Lengh of the string

# fruit = 'mango'
# count = 0
# while count < len(fruit):
#     print(count, fruit[count])
#     count = count +1
# print('Done')
#
# for letter in 'banana':
#     print(letter)


# word = 'abrasion'
# count = 0
# a_count = 0
#
# for i in word:
#     if i =='a':
#         a_count = a_count + 1
#     count = count + 1
#     print(count, a_count)

# word = 'once upon a time'
# print(word[:5])
# print(word[5:])
# print(word[:])

# in is a logical operator
# fruit = 'pineapple'
#
# if 'a' in fruit:
#     print('a is present')

# String commands: lowercase, locating
# greet = 'HELLO world'
# greet_lower = greet.lower()
#
# fruit = 'tomato'
# pos = fruit.find('o')
# print(pos)
#
# greet_2 = 'Good Morning'
# print(greet_2.replace('Morning', 'Evening'))
# print(greet_2.replace('o','u'))

# Removing white space
# greet = '  Hello World    '
# print(greet)
# print(greet.lstrip())
# print(greet.rstrip())
# print(greet.strip())

# Starts with
# line = 'Please close the doors'
# print(line.startswith('Please'))

# Exercise 6.5
str = 'X-DSPAM-Confidence:0.8475'
pos = str.find(':')
data = str[pos+1 :]
data = float(data)
print(data)
