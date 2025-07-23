#Python Exception Handling: Exercises, Solutions, and Practice
#1.
try:
    print(1/0)
except ZeroDivisionError:
    print("You are dividing the number by zero")
# #2.
try:
    enter_int =int(input("Enter digit: "))
    print("You entered: ",enter_int)
except ValueError:
    print('Enter a valid digit')
# #3. 
import os
file_path = 'spotify_cleaned.csv'
try:
    with open(file_path, 'r') as file:
        print("File opened succesfully")
except FileNotFoundError:
    print("File doesn't exist")
#4.
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if not (num1.replace(' ', '', 1).isdigit() and num2.replace(' ', '', 1).isdigit()):
        raise TypeError("Inputs must be numeric")
    print("You entered:", num1, "and", num2)
except TypeError:
    print("Enter a valid digit!")
#5.
try:
    with open("readonly_file.txt", "w") as f:
        f.write("Trying to write to a read-only file")
except PermissionError:
    print("Permission denied: You can't write to this file.")
#6.
try:
    my_list = [1,2,3,4,5,6,7]
    print(my_list[8])
except IndexError:
    print("Choose the valid index")
#7.
try:
    while True:
        print("Running... Press Ctrl+C to stop.")
except KeyboardInterrupt:
    print("\nProgram interrupted by user!")
# #8.
try:
    result = 1 / 0
except ArithmeticError as e:
    print("Arithmetic error occurred:", e)
#9.
try:
    with open("spotify_cleaned.csv", encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError as e:
    print("Unicode decode error:", e)
#10.
try:
    print('hello'.upperr())
except AttributeError:
    print("Check the function or method")
    
#Python File Input Output: Exercises, Practice, Solution
#File Input/Output Exercises
#1.
path_file= 'spotify_cleaned.csv'
with open (path_file, 'r',encoding='utf-8' ) as f:
    data = f.read()
print(data)
#2.
def first_n_line(path_file, n):
    lines = []
    with open(path_file,'r', encoding='utf-8') as f:
        for i , line in enumerate(f):
            if i<n:
                lines.append(line.strip())
            else:
                break
    return lines
print(first_n_line(path_file, 5))
3.
with open (path_file, 'a') as f:
    f.write("here is the new record")
#4.
def last_n_line(path_file, n):
    with open(path_file,'r', encoding='utf-8') as f:
        all_lines=f.readlines()
        return [line.strip() for line in all_lines[-n:]]
print(last_n_line(path_file, 5))
#5.
def stores_into_lst(path_file):
    all_lines=[]
    with open(path_file, 'r',encoding='utf-8') as f:
        data =f.readlines()
        all_lines.extend(data)
    return all_lines
print(stores_into_lst(path_file))
#6.
def stores_into_var(path_file):
    with open(path_file, 'r',encoding='utf-8') as f:
        lines=f.readlines()
    return lines
print(stores_into_var(path_file))
#7.
def stores_into_array(path_file):
    all_lines=[]
    with open(path_file, 'r',encoding='utf-8') as f:
        data =f.readlines()
        all_lines.extend(data)
    return all_lines
print(stores_into_array(path_file))
#8.
def find_max(path_file):
    longest=''
    with open(path_file, 'r', encoding='utf-8') as f:
       for line in f:
           words=line.split()
           for word in words:
            if len(word)>len(longest):
                longest=word
    return longest
print(find_max(path_file))
#9.
line_count=0
with open(path_file, 'r',encoding='utf-8') as f:
   for line in f:
      line_count+=1
print(f"The number of lines in the file is {line_count}")
#10.
def word_frequency(path_file):
    freq = {}
    with open(path_file, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                word = word.lower().strip(".,!?\"'()[]{}:;")  # clean punctuation
                if word:
                    freq[word] = freq.get(word, 0) + 1
    return freq
print(word_frequency('spotify_cleaned.csv'))

#11.
import os
path_file= 'spotify_cleaned.csv'
try:
    file_size = os.path.getsize(path_file)
    print(f"The size of {path_file} is {file_size} bytes")
except OSError:
    print(f"Error accessing file {path_file}")
#12.
path_file= 'spotify_cleaned.csv'
my_list =[1,2,3,4,5]
with open(path_file, 'a', encoding='utf-8') as f:
   for item in my_list:
      f.write(str(item)+'\n')
#13.
destination_file='destination_file.csv'
path_file= 'spotify_cleaned.csv'
def copy_file_to_another(path_file, destination_file):
    with open(path_file, 'r',encoding='utf-8') as f:
        data =f.readlines()
    with open(destination_file, 'a', encoding='utf-8') as target:
        target.writelines(data)
copy_file_to_another(path_file, destination_file)
    
#14.
destination_file='destination_file.csv'
path_file= 'spotify_cleaned.csv'
combined= 'combined.csv'
with open(path_file, 'r', encoding='utf-8') as f1, open(destination_file, encoding='utf-8') as f2,\
open(combined, 'a',encoding='utf-8') as outfile:
    for line1,line2 in zip(f1, f2):
        combined_line=line1.strip()+ ','+line2.strip()+'\n'
        outfile.write(combined_line)
#15.
import random
path_file= 'spotify_cleaned.csv'
def random_line(path_file):
    with open(path_file,'r', encoding='utf-8') as f:
        lines=f.readlines()
        return random.choice(lines).strip()
print(random_line(path_file))
#16.
path = 'sample.txt'

f = open(path, 'r')
print("File closed?", f.closed)  # ➜ False
f.close()
print("File closed?", f.closed)  # ➜ True
#17.
def remove_newlines(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\n', '')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

remove_newlines('sample.txt')
#18.
def count_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        cleaned = text.replace(',', ' ')  # replaces commas with space
        words = cleaned.split()
        return len(words)

print(count_words('sample.txt'))
#19.
import os

def extract_characters_from_files(folder_path):
    char_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                char_list.extend(list(f.read()))
    return char_list

print(extract_characters_from_files('./texts'))
#20.
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w', encoding='utf-8') as f:
        f.write(f"This is file {letter}.txt\n")
#21
def write_alphabet_per_line(filename, letters_per_line):
    import string
    alphabet = string.ascii_lowercase
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(0, len(alphabet), letters_per_line):
            f.write(alphabet[i:i+letters_per_line] + '\n')

write_alphabet_per_line('alphabet_lines.txt', 5)
