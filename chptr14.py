# Python Objects
#class is the 'biscuit cutter' while object is the biscuit made from the cutter

# class PartyAnimal:
#     x = 0 # x is an attribute
#
#     def party(self): #Party is a method as it only exists in the class
#         self.x = self.x + 1 #self.x is a variable
#         # This syntax using the dot operator is saying ‘the x within self.
#         print("So far",self.x)
#
# an = PartyAnimal()
# an.party() #'an' is an alias for self in the function
# an.party()
# an.party()
# PartyAnimal.party(an) #short version of syntax above

# Object lifecycle

# class PartyAnimal:
#    x = 0
#
#    def __init__(self):
#      print('I am constructed')
#
#    def party(self) :
#      self.x = self.x + 1
#      print('So far',self.x)
#
#    def __del__(self):
#      print('I am destructed', self.x)
#
# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains',an)

# Multiple uses of an Object

# class PartyAnimal:
#    x = 0
#    name = ''
#    def __init__(self, nam):
#      self.name = nam
#      print(self.name,'constructed')
#
#    def party(self) :
#      self.x = self.x + 1
#      print(self.name,'party count',self.x)
#
# s = PartyAnimal('Sally')
# j = PartyAnimal('Jim')
#
# s.party()
# j.party()
# s.party()

# Experimenting: Class that prints out multiples of any given number
class Number:
    x = 0
    sum = 0
    count = 0

    def __init__(self,num):
        self.num = num
        print('Started',num)

    def mult(self):
        self.x = self.x + 1
        sum = self.x * self.num
        self.count = self.count + 1
        print(self.x,sum)

    def __del__(self1):
        print(self1.count,'multiples of',self1.num, 'shown')

a = Number(5)
a.mult()
a.mult()
a.mult()
a.mult()
