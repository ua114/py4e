# 5.1
# sum = 0.0
# count = 0
#
# while True:
#     num = input('Enter a number:')
#     if num == 'Done':
#         break
#     else:
#         try:
#             num = float(num)
#         except:
#             print('Input not recognised')
#             continue
#         sum = sum + num
#         count = count + 1
#         average = sum/count
# print('The sum is:', sum)
# print('The average is:', average)
# print('Done')

# Ex 5.2
smallest = None
largest = None

while True:
    num = input('Enter a number:')
    if num == 'Done':
        break
    try :
        num = int(num)
    except:
        print('Input not recognised! Try again!')
        continue
    if smallest == None:
        smallest = num
    if smallest > num:
        smallest = num
    if largest == None:
        largest = num
    if largest < num:
        largest = num
    print('Smallest so far:', smallest)
    print('Largest so far:', largest)

print('Smallest number:', smallest)
print('Largest number:', largest)
print('Done')
