# Using touples to sort Dicitionaries

# a = {'apple' : 1, 'oranges' : 4, 'banana' : 2, 'mangoes' : 3 }
# b = list()
#
# for k,v in a.items():
#     b.append( (v,k) )
# c = sorted(b, reverse=True)
# print(c)

# c = [(1, 'apple'), (4, 'oranges'), (2, 'banana'), (3, 'mangoes')]

# Alternate method

# a = {'apple' : 1, 'oranges' : 4, 'banana' : 2, 'mangoes' : 3 }
#
# print( sorted( [ (v,k) for k,v in a.items() ] ) )

#  items inside sorted generate a list (v,k) which is then sorted

# Sorting words from longest to shortest

# txt = 'but soft what light in yonder window breaks'
# length = list()
#
# lst = txt.split()
#
# for i in lst:
#     length.append( (len(i),i) )
# length.sort(reverse=True)
#
# for length, word in length:
#     print(word, length)

# Touple properties

# m = ['Hows it', 'Going']
# x,y = m
# print(x)
# print(y)
#
# email = 'mark@facebook.com'
# usrname, domain = email.split('@')
# print(usrname, domain)

# d = {'a':10, 'b':1, 'c':22}
#
# t = list(d.items())
# print(t)
# print(type(t))

# Exercise 10.1
#
# fopen = open('mbox-short.txt')
# count = dict()
# t = list()
# for line in fopen:
#     if line.startswith('From') and len(line.split()) > 3:
#         words = line.split()
#         count[words[1]] = count.get(words[1],0) + 1
# # print(count)
# for k,v in count.items():
#     t.append((v,k))
# t.sort(reverse=True)
# Big_word = None
# Big_count = None
#
# for count, word in t:
#     if Big_word == None or count > Big_count:
#         Big_word = word
#         Big_count = count
# print(Big_word, Big_count)

# Experimenting with regular expressions

# txt = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('([0-9]+):',txt)
# y = re.findall('^From.*\s+(\S+@\S+)', txt)
# y = re.findall('^From\s+\S+\s+\S+\s+\S+\s+\S+\s+([0-9]+):',txt)

# fopen = open('practice.txt')
#
# for line in fopen:
#     if re.search('^From',line):
#         y = re.findall('[0-9]+:',line)
#         print(y)

# Exercise 10.2 using regular expressions - works now
# import re
# fopen = open('mbox-short.txt')
# count = dict()
# a = list()
#
# for line in fopen:
#     numbers = re.findall('^From.*\s([0-9]+):',line)
#     for number in numbers:
#         count[number] = count.get(number,0) + 1
# for (v,k) in count.items():
#     a.append((v,k))
# c = sorted(a)
#
# for hour,number in c:
#     print(hour,number)

# Exercise 10.2 proper

# fopen = open('mbox-short.txt')
# count = dict()
# a = list()
#
# for line in fopen:
#     line = line.rstrip()
#     if line.startswith('From') and len(line.split()) > 3:
#         line = line.split()
#         words = line[5]
#         time = words.split(':')[0]
#         count[time] = count.get(time,0) + 1
# print(count)
#
# for (v,k) in count.items():
#     a.append((v,k))
# c = sorted(a)
#
# for hour,number in c:
#     print(hour,number)

# Exercise 10.3
import re
fopen = open('practice.txt')
a = list()
count = dict()
count_letter = 0

for line in fopen:
    letters = re.findall('[A-z]',line)
    for letter in letters:
        count[letter] = count.get(letter,0) + 1
        count_letter = count_letter + 1

for (v,k) in count.items():
    a.append((k,v))

a = sorted(a,reverse=True)

for freq,letter in a:
    print(letter,freq/count_letter * 100)
print(count_letter)
