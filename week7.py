# Regular expressions
# re.findall returns a list of matched substrings, but the method
# re.search returns a match object, you can recover the full matched substring
# using re.group()

# Experimenting with re
# txt = 'From zqian@umich.edu Fri Jan  4 16:10:39 2008'
# # y = re.findall('^From.*@(\S+)\.',txt) extracts umich
# # y = re.findall('^From.*[0-9][0-9]:([0-9][0-9]):',txt) extracts 10
# # print(y)

# Exercise 11.1 - solution provided may be wrong

# import re
# fopen = open('mbox.txt')
# count = 0
# # inp = input('Enter a regular expression:')
# inp = '^Author'
#
# for line in fopen:
#     if re.search(inp,line):
#         count = count + 1
#         # print(line,count)
# print('mbox has',count,'lines that matched',inp)
# import re
# fopen = open('mbox.txt')
# count = 0
# count_re = 0
#
# for line in fopen:
#     line = line.rstrip()
#     if line.startswith('Author'):
#         count = count + 1
#     if re.search('^Author',line):
#         count_re = count_re + 1
# print('Count is: ',count)
# print('Re count is:',count_re)

# Exercise 11.2
# import re
# fopen = open('mbox-short.txt')
# sum = 0
# count = 0
#
# for line in fopen:
#     numbers = re.findall('^New Revision:\s+([0-9]+)',line)
#     for number in numbers:
#         sum += int(number)
#         count += 1
# print(int(sum/count))

# Exercise 11.2 and 11.3 Alternative method

import re
fopen = open('mbox.txt')
numbers = list()

for line in fopen:
    number = re.search('^New Revision:\s+([0-9]+)',line)
    if number:
        numbers.append( int( number.group(1) ) )
print(int(sum(numbers)/len(numbers)))
