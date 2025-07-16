#1 Determines whether a given year is a leap year.

check_year = input('The year to be checked: ')
if check_year.isdigit():
    check_year = int(check_year)
    if (check_year % 4 == 0 and check_year % 100 != 0) or (check_year % 400 == 0):
        print(True)
    else:
        print(False)
else:
    raise ValueError('Enter a valid integer year.')

#2. Conditional Statements Exercise

n = input('Enter a number between 1 and 100: ')
if n.isdigit():
    n=int(n)
    if 1<=n<=100:
        if n%2!=0:
            print('Weird')
        elif n%2==0 and 2<=n<=5:
            print('Not Weird')
        elif n%2==0 and 6<=n<=20:
            print('Weird')
        elif n%2==0 and n>20:
            print('Not Weird')
    else:
        raise ValueError("The number must be between 1 and 100")

else:
    raise ValueError("Enter a valid integer.")

#3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
#with if-else
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

start = min(a, b)
end = max(a, b)
if start % 2 == 0:
    even_start = start
else:
    even_start = start + 1  
even_numbers = list(range(even_start, end + 1, 2))
print("Even numbers:", even_numbers)
#without if-else
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
start = min(a, b)
end = max(a, b)
even_start = start + start % 2
even_numbers = list(range(even_start, end + 1, 2))
print("Even numbers:", even_numbers)
