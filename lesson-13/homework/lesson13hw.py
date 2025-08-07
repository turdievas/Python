
#1.Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import date, datetime, timedelta
y = int(input("Enter birth year: "))
m = int(input("Enter birth month: "))
d = int(input("Enter birth day: "))
birth = date(y, m, d)
today = date.today()
years = today.year - birth.year
months = today.month - birth.month
days = today.day - birth.day
if days < 0:
    months -= 1
    days += 30 
if months < 0:
    years -= 1
    months += 12

print(f"{years} years, {months} months, {days} days")
#2. 
enter_month= int(input('Your birth month: '))
enter_day = int(input("Enter your birthday: "))
today = date.today()
b_day_this_year = date(today.year, enter_month, enter_day)

if b_day_this_year>= today:
    next_bday = b_day_this_year
else:
    next_bday=date(today.year+1, enter_month, enter_day)
days_remaining = next_bday-today
print(f"{days_remaining} left till your birthday!")

#3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
enter_current_year =int(input("Enter current year: "))
enter_current_month =int(input("Enter current month: "))
enter_current_day =int(input("Enter current day: "))
enter_current_hour =int(input("Enter current hour: "))
enter_current_minute = int(input("Enter current minute: "))
duration_of_meeting_hours = int(input("Enter duration of meeting in hours: "))
duration_of_meeting_minutes = int(input("Enter duration of meeting in minutes: "))

obj = datetime(enter_current_year, enter_current_month, enter_current_day, enter_current_hour, enter_current_minute)
time =timedelta(hours=duration_of_meeting_hours, minutes=duration_of_meeting_minutes)

added = obj+time
print(f"{added.strftime('%d/%m/%Y, %H:%M:%S')}")
#4. 
from datetime import datetime
import pytz

from_zone_str = input('Enter your timezone: Asia/Tashkent : ')
from_zone =pytz.timezone(from_zone_str)
curr_year = int(input("Enter current year: "))
curr_month = int(input("Enter current month: "))
curr_day = int(input("Enter current day: "))
curr_hour = int(input('Enter current hour: '))
curr_min = int(input("Enter current minute: "))
to_which_str = input("Enter another timezone of your choice: (F/ex: America/New_York):  ")
to_which= pytz.timezone(to_which_str)
all_in = datetime(curr_year, curr_month, curr_day, curr_hour, curr_min)
localized_time = from_zone.localize(all_in)
converted = localized_time.astimezone(to_which)
print(f"You converted to {to_which} and here is the result: {converted}")


# #5. 
from datetime import datetime
import time

year = int(input("Enter the future year: "))
month = int(input("Enter the future month: "))
day = int(input("Enter the future day: "))
hour = int(input("Enter the future hour: "))
minute = int(input("Enter the future minute: "))
second = int(input("Enter the future second: "))
future_time =datetime(year, month, day,hour,minute, second)
while True:
    current_time = datetime.now()
    remaining_time = future_time-current_time
    if remaining_time.total_seconds()<=0:
        print("Time's up!")
        break
    total_seconds = int(remaining_time.total_seconds())
    hrs = total_seconds//3600
    mins = (total_seconds%3600)//60
    secs = total_seconds%60
    print(f"Time remaining: {hrs:02}:{mins:02}:{secs:02}", end='\r')
    time.sleep(1)


#6.
import re
while True:
    email = input("Emailingizni kiriting: ")
    sm = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if  re.fullmatch(sm, email) :
        print("Siz kiritgan email yaroqli")
        break

    else:
        print("Email yaroqsiz qayta kiriting.")

#7.
import re

# Ask user to enter a phone number
raw_input = input("Telefon raqamingizni kiriting (faqat raqamlar): ")

# Remove all non-digit characters
digits = re.sub(r'\D', '', raw_input)

# Ensure it's exactly 9 digits (excluding +998)
if len(digits) == 9:
    formatted = f"+998 ({digits[0:2]}) {digits[2:5]}-{digits[5:7]}-{digits[7:9]}"
    print("Formatlangan raqam:", formatted)
else:
    print("Noto'g'ri raqam uzunligi. 9 ta raqam kiriting, masalan: 901234567")
#8.
#Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
import re
while True:
    pasw = input("Istalgan passwordni kiriting: ")
    if len(pasw)>=8 and re.findall('[a-z]',pasw) and re.findall('[A-Z]',pasw) and re.findall('[0-9]',pasw) and\
    re.findall('\\W',pasw):
        print("Siz kiritgan kod yaroqli")
        break

    else:
        print("Kod yaroqsiz qayta kiriting.")
#9.Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
import re

sample_text = """
Python is powerful. Python is easy to learn. Many developers love Python.
This word finder will help find words like Python in a sentence.
"""

word = input("Enter a word to be searched: ").strip()

# Use word boundaries \b to match whole words
matches = re.findall(rf'\b{re.escape(word)}\b', sample_text, re.IGNORECASE)

if matches:
    print(f"Found '{word}' {len(matches)} time(s).")
    for match in matches:
        print("→", match)
else:
    print(f"No matches found for '{word}'.")
#10.
import re

# Common date formats: DD/MM/YYYY, MM-DD-YYYY, YYYY.MM.DD, etc.
date_pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[./-]\d{1,2}[./-]\d{1,2})\b'

# Get user input
text = input("Enter a text that may contain dates: ")

# Find all matches
dates = re.findall(date_pattern, text)

# Display results
if dates:
    print("Found the following date(s):")
    for d in dates:
        print("→", d)
else:
    print("No dates found in the text.")
