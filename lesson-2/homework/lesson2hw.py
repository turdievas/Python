 #1. Age calculator

name = input('Your name?')
year_of_birth = int(input('Year of birth'))
result = 2025-year_of_birth
print ('Your age is:' , result)

#2. Extract Car Names

txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])

#3. Extract Car Names

txt = 'MsaatmiazD'
print(txt[::2])
rev_txt =  (txt[::-1])
print(rev_txt[::2])

#4. Extract Residence Area

txt = "I'am John. I am from London"
residence = txt.split('from')
print (residence[1].lstrip())

#5. Reverse String

user_data  = input('Your hometown')
reversed_data  = user_data[::-1]
print (reversed_data)

#6.Count Vowels

my_str = 'My name is odina and my surname is \
    turdiyeva'
count = 0
for char in my_str:
    if char  in ['a', 'e', 'i', 'o', 'u']:
        count +=1
print (count)

#7. Find Max Value

your_nums = input('Enter a list of numbers')
int_list = [int(x) for x in your_nums.split()]
print (int_list)
max_value=int_list[0]
for num in int_list:
    if max_value<num:
        max_value=num
print (max_value)

#8. Check Palindrome 

check_pal = 'kiyik'
if check_pal == check_pal[::-1]:
    print ('true')
else:
    print ('false')

#9. Extract email domain

email = input('Enter your email address')
result = email.split('@')
print(result[1].lstrip())

#10. Generate random password
import random
import string

letters = string.ascii_letters
digits = string.digits
specials = string.punctuation
all_chars = letters+digits+specials
password = ''.join(random.choice(all_chars) for _ in range(12))
print(password)
