
age = input('How old are you:')

try:
    age = int(age)
except:
    age = -1

if age == -1:
    print('Input not recognised')
else:
    print('You are alive')

# Graded exercise 1
hrs = input("Enter Hours:")
h = float(hrs)
rate = 10.5

if h <= 40:
    pay = rate * h

elif h >40:
    pay = (rate*40) + (h-40)*rate*1.5

else :
    print('Input not recognised')

print(pay)

# Exercise 2
hrs = input('Enter the number of hours:')
rate = input('Enter the rate:')

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error! Enter numerical data')
    quit()

if h <= 40:
    pay = r * h

elif h >40:
    pay = (r*40) + (h-40)*r*1.5
print(pay)

# Exercise 3
grade = input('Enter a grade between 0 and 1:')
try:
    g = float(grade)
except:
    print('Error! Input not recognised')
    quit()
if g >= 0.9:
    print('A')
elif g>=0.8:
    print('B')
elif g>=0.7:
    print('C')
elif g>=0.6:
    print('D')
elif g<0.6:
    print('F')
