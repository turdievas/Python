#OOP
#1.Circle Class

import math 
p=math.pi
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
       return math.pi*(self.radius**2)
    def circumference(self):
        return 2*math.pi*self.radius
c=Circle(15)
print(f"Circle's area is: {c.area()}")
print(f"Circle's circumference is: {c.circumference()}")

#2.Person Class

from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    def Calc_age(self):
        today= date.today()
        age=today.year-self.date_of_birth.year
        if(today.month, today.day)<(self.date_of_birth.month,self.date_of_birth.day):
            age -=1
        return age
odina = Person('Odina', 'Uzbekistan', date(2005,11,18))
print(f"{odina.name} ning  yoshi {odina.Calc_age()}")

#3. #Calculator Class

class Calc:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b
    def subtract(self):
        return self.a-self.b
first_ex=Calc(10,15)
print(first_ex.subtract())

#4. Shape and Subclasses

import math 
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
       return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
class Triangle(Shape):
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a) *(s-self.b)*(s-self.c))
    def perimeter(self):
        return self.a+self.b+self.c
class Square(Shape):
    def __init__(self, x):
        self.x=x
    def area(self):
       return self.x**2
    def perimeter(self):
        return 4*self.x

#5.Binary Search Tree Class
pass

#6.Stack Data Structure

class DataStructure:
    def __init__(self):
        self.stack=[]
    def push(self, item):
        return self.stack.append(item)
    def pop(self):
        return self.stack.pop()
first = DataStructure()
first.push(5)
print(first.pop())

#7. Linked Data Structure
pass

#8.Shopping Cart Class

class Shopping:
    def __init__(self):
        self.items = {}
    def add(self, item, price):
        self.items.update({item:price})
    def remove(self,item):
        return self.items.pop(item,"Not found")
    def total(self):
        total = 0
        for price in self.items.values():
            total+=price
        return total
for_ex= Shopping()
for_ex.add('banan', 30000)
for_ex.add('olma', 25000)
for_ex.add('nok', 15000)
for_ex.add('uzum', 32000)
for_ex.add('shaftoli', 28000)

print(f"Total price of all items: {for_ex.total()}")

#9.Stack with Display 

class Display:
    def __init__(self):
        self.display =[]
    def push(self, item):
        self.display.append(item)
    def pop(self):
        return self.display.pop()
    def displaying(self):
        return f"Items: {self.display}"
ex2 = Display()
ex2.push(5)
ex2.displaying()
print(ex2.display)

#10. Queue Data Structure

class Queue:
    def __init__(self):
        self.data = []
    def enqueueing(self, item):
        self.data.append(item)
    def dequeueing(self):
        try:
            return self.data.pop(0)
        except:
            print("There is no item with this index!")
ex3 = Queue()
ex3.dequeueing()
print(ex3.data)

#11. Bank Class

class Bank:
    def __init__(self):
        self.bank ={}
    def pushing_cust(self,customerID, name, email,phone, address):
        self.bank[customerID]={'info':{'name':name, 'email':email,'phone':phone, 'address':address}, 'transactions':[]}
    def push_transactions(self,customerID, transactionAmount):
        if customerID in self.bank:
            self.bank[customerID]['transactions'].append(transactionAmount)
        else:
            return f"There is no customerID for such transaction"
    def viewInfo(self, customerID):
        return self.bank.get(customerID, "Customer Not Found")
    def removeCustomer(self, customerID):
            return self.bank.pop(customerID)
    def calcBalance(self, customerID):
        if customerID in self.bank:
            totalBalance = 0
            for transactionAmount in self.bank[customerID]['transactions']:
                totalBalance+=transactionAmount 
            return totalBalance
customer1 = Bank()
customer1.pushing_cust(1,'Alex', 'alex345@gmail.com', 781234567,'US, New York City')
customer1.push_transactions(1, 45000)
customer1.viewInfo(1)
customer1.calcBalance(1)
print(customer1.bank)
