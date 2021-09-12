# Dicitionaries

# cost = dict()
# cost['apple'] = 2
# cost['banana'] = 3
# cost['orange'] = 2
#
# print(cost)
# print(cost['apple'])

# dictionary order is random

# Another way of making Dicitionaries

# fruits_cost = {'apple' : 1, 'banana' : 2, 'orange' : 3, 'kiwi' : 0}
# print(fruits_cost)
#
# if 'kiwi' in fruits_cost:
#     print('Kiwi is present')
# else:
#     print('Kiwi not found')

# counting vowels inputted

# count = dict()
#
# while True:
#     vowel = input('Enter a vowel:')
#     if vowel == 'Done':
#         break
#     for i in vowel:
#         if i not in count:
#             count[i] = 1
#         else:
#             count[i] = count[i] + 1
# print(count)
# x = count.get('a', 0)
# print(x)

# Alternative way of counting letters in dictionary

# count = dict()
# while True:
#     letters = input('Enter a vowel:')
#     if letters == 'Done':
#         break
#     for letter in letters:
#         count[letter] = count.get(letter, 0) + 1
#         # 0 is the default value if key is not present
# print(count)


# Looping through dictionary

# fruit = {'apple' : 1, 'banana' : 4, 'orange' : 5}
# print(fruit)
#
# for key in fruit:
#     print(key, fruit[key])

# Converting dictionary into keys and values

# fruit = {'apple' : 1, 'banana' : 4, 'orange' : 5}
#
# print(list(fruit))
# print(fruit.keys())
# print(fruit.values())
# print(fruit.items())

# iterating through two variables - e.g. increasing number

# fruit = {'apple' : 1, 'banana' : 4, 'orange' : 5}
#
# for aaa, bbb in fruit.items():
#     bbb = bbb + 1
#     print(aaa,bbb)

# Counting words from a document and finding the most common word

# fopen = open('practice.txt')
# count = dict()
#
# for line in fopen:
#     line = line.rstrip()
#     words = line.split()
#     for word in words:
#         count[word] = count.get(word,0) + 1

# Big_word = None
# Big_count = None
#
# for key,value in count.items():
#     if Big_word == None or value > Big_count:
#         Big_word = key
#         Big_count = value
# print(Big_word, Big_count)

# Exercise 9.2

# fopen = open('practice.txt')
# words = list()
# count = dict()
#
# for line in fopen:
#     line = line.rstrip()
#     line = line.split()
#     words.append(line[2])
# for word in words:
#     count[word] = count.get(word,0) + 1
# print(count)

#  Alternate methods
# for line in fopen:
#     line = line.rstrip()
#     line = line.split()
#     count[line[2]] = count.get(line[2],0) + 1
# print(count)

# Exercise 9.3

# fopen = open('mbox.txt')
# words = list()
# count = dict()
#
#
# for line in fopen:
#     line = line.rstrip()
#     if line.startswith('From'):
#         line = line.split()
#         if len(line) > 3:
#             words.append(line[1])
# for word in words:
#         count[word] = count.get(word,0) + 1
# # print(words)
# # print(count)
#
# # Exercise 9.4 - continues from 9.3
#
# max_email = None
# max_number = None
#
# for email,number in count.items():
#     if max_email == None or number > max_number:
#         max_email = email
#         max_number = number
# print(max_email,max_number)

# Exercise 9.5

# fopen = open('mbox-short.txt')
# count = dict()
#
# for line in fopen:
#     line = line.rstrip()
#     if line.startswith('From') and len(line.split()) > 3:
#         # print(line)
#         spos = line.find('@')
#         epos = line.find(' ',spos)
#         # print(line[spos + 1:epos])
#         count[line[spos+1:epos]] = count.get(line[spos + 1: epos], 0) + 1
# print(count)

# Alternative 9.5 using list.append

fopen = open('mbox-short.txt')
words = list()
count = dict()

for line in fopen:
    line = line.rstrip()
    if line.startswith('From') and len(line.split()) > 3:
        spos = line.find('@')
        epos = line.find(' ',spos)
        words.append(line[spos + 1 : epos])
for word in words:
    count[word] = count.get(word,0) + 1
print(count)
