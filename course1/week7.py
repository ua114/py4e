# Using loops

# n = 5
#
# while n>0:
#     print(n)
#     n = n - 1
# print('Happy new year')

# def new_year(n):
#     while n>0:
#         print(n)
#         n = n -1
#     print('Happy new year')
#
# x = input('Enter a number:')
# x = int(x)
# new_year(x)

# while True:
#     n = input('>')
#     if n == 'skip':
#         continue
#     if n == 'done':
#         break
#     print(n)
# print("Finished")

# for i in [1, 2, 3, 4, 5]:
#     print(i)

# Finfing the maximum, min, average and sum in a list
# n = 0
# m = 100
# sum = 0
# count = 0
#
# for i in [2, 4, 10, 6, 8, 15, 7, 9]:
#     if i > n:
#         n = i
#     if i < m:
#         m = i
#     print(i)
#     sum = sum + i
#     count = count + 1
# print('Largest number is:',n)
# print('The smallest number is:',m)
# print('The sum is:',sum)
# print('The average is',sum/count)

# Finding an item present in a list

# found = False
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if i==7:
#         found = True
#     if i != 7:
#         found = False
#     print(found, i)
# print('Done')

# Using 'None' to find the smallest

smallest = None

for i in [1, -5, 7, 0, 10, -10]:
    if smallest == None:
        smallest = i
    elif i < smallest:
        smallest = i
    print('Smallest so far:', smallest)
print('Smallest number is:',smallest)
