
# def arithematic_arranger(str,state):
import re
str = '5 + 16'
str = str.rstrip()
# y = re.search()
y = re.findall('[0-9]+',str)
x = str.split()
print(y[0])
print(x[1],y[1])
sum = int(x[0]) + int(x[2])
print(sum)
