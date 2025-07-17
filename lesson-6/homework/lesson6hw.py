#Homework
#2. Integer Squares Exercise

inp = int(input('Enter a number: '))
if inp>=0:
    inp=list(range(0, inp))
    for x in inp:
        print(x**2)

#Loop based-Exercises
#Exercise 1: Print first 10 natural numbers using a while loop

p=0
while p<10:
    p+=1
    print(p)

#Exercise 2: Print the following pattern

for x in range(1,6):
    for j in range(1, x+1):
        print(j, end=" ")
    print()

#Exercise 3: Calculate sum of all numbers from 1 to a given number

num = list(range(1,int(input('Enter a number: '))+1))
total  = 0
for n in num:
    total+=n
print(f"Sum is {total}")

#Exercise 4: Print multiplication table of a given number

my_numbers =range(1,11)
n = int(input("Enter a number: "))
for m in my_numbers:
    print(m*n)

#Exercise 5: Display numbers from a list using a loop

numberss = [12, 75, 150, 180, 145, 525, 50]
for num in numberss:
        print(num)

#Exercise 6: Count the total number of digits in a number

user_input=list(input("Enter digits: "))
print(len(user_input))

#Exercise 7: Print reverse number pattern

for x in reversed(range(1,6)):
     for j in reversed(range(1, x+1)):
         print(j, end=" ")
     print()

#Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
for l in reversed(list1):
     print(l)

#Exercise 9: Display numbers from -10 to -1 using a for loop

sonlar = range(-10,-1)
for s in sonlar:
    print(s)

#Exercise 10: Display message “Done” after successful loop execution

digits = range(0,5)
for x in digits:
    print(x)
print("Done")

#Exercise 11: Print all prime numbers within a range

for num in range(25,50):
    for i in range(2,num): #we are using 2 because all numbers are divisible by `1`
        if num%i==0:
            break
    else:
        print(num)

#Exercise 12: Display Fibonacci series up to 10 terms

a=0 
b=1
for i in range(1,11):
    print(a, end=" ")
    a,b=b, a+b

#Exercise 13: Find the factorial of a given number

asked =list( range(1,int(input("Enter a num to calculate factorial: "))+1))
factorial=1
for e in asked:
    factorial*=e
print(factorial)


#4. Return Uncommon Elements of Lists


first_list = list(map(int, input("Enter the first list: ").split()))
second_list = list(map(int, input("Enter the second list: ").split()))
result=[]
for f in first_list:
    if f not in second_list:
        result.append(f)
    else:
        second_list.remove(f)
        
result.extend(second_list)
print(result)
