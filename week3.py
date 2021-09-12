# Opening files - using 'for' loop to open

# handle = open('mbox.txt', 'r')
# for i in handle:
#     print(i)

# Or put entire file into one string

# handle = open('practice.txt')
# inp = handle.read()
# print(len(inp))
# print(inp)

# Removing whitespaces added by print
# handle = open('mbox.txt')
#
# for i in handle:
#     i = i.rstrip()
#     if i.startswith('From'):
#         print(i)

# Alternatlively

# handle = open('mbox.txt')
#
# for i in handle:
#     i = i.rstrip()
#     if not i.startswith('From'):
#         continue
#     print(i)

# Exercise 8.1

# file = input('Enter file name: ')
# try:
#     handle = open(file)
# except:
#     print('File name not recognised:', handle)
#     quit()
#
# for i in handle:
#     i = i.rstrip()
#     i = i.upper()
#     print(i)

# Exercise 8.2

# fopen = open('mbox-short.txt')
# count = 0
# sum = 0
#
# for i in fopen:
#     i = i.rstrip()
#     if i.startswith('X-DSPAM-Confidence:'):
#         pos= i.find(' ')
#         num = float(i[pos+1 :])
#         sum = sum + num
#         count = count+1
# print('Sum of confidence:', sum)
# print('Average confidence:', sum/count)

# Exercise 8.3

x = input('Enter file name:')
count = 0

try:
    fopen = open(x)
except:
    if x == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    print('File not found:',x)
    quit()

for i in fopen:
     count = count+1
print('Number of lines:',count)
