#1.creating a virtual environment

#Commands on terminal
#.\venv\Scripts\Activate
#. pip install pandas requests matplotlib

#2.Create custom modules

import math_operations
print(f"add: {math_operations.add(3,4)}")
print(f"subtract: {math_operations.subtract(3,4)}")
print(f"multiply: {math_operations.multiply(3,4)}")
print(f"divide: {math_operations.divide(3,4)}")

import string_utils
any_text="hello my name is Odina"
print(string_utils.reverse_string(any_text))
print(string_utils.count_vowels(any_text))

#3.Create custom packages.
import geometry.circle

print(geometry.circle.calculate_area(15))
print(geometry.circle.calculate_circumference(20))

import file_operations.file_reader, \
file_operations.file_writer
path_file='msg.txt'
content = 'Some text'
print(file_operations.file_reader.read_file(path_file))
file_operations.file_writer.write_to_file(path_file, content)



