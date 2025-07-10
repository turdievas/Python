#1. Create and access elements
my_fruits = ['apple', 'orange', 'banana', 'pineapple', 'peach']
print(my_fruits[2])

#2. Concatenate Two Lists
first_nums = [1, 2, 3, 4, 5]
second_nums = [6,7,8,9,10]
first_nums +=second_nums
print (first_nums)

#3. Extract Elements from a List
list_of_nums = [2,4,6,8,10,12,14]
first = list_of_nums[0]
middle = list_of_nums[len(list_of_nums)//2]
last = list_of_nums[-1]
extracted = [first, middle, last]
print (extracted)

#4. Convert List to Tuple
fav_movies = ['Harry Potter','Gifted Hands', 'The Pursuit of Happiness',\
 'Women','Taxi']
tuple_of_movies= tuple(fav_movies)
print (tuple_of_movies)

#5. Check Element in a List
cities = ['London', 'Istanbul', 'Tashkent', 'Paris' ]

if 'Paris' in cities:
    print(f"Paris is found in {cities.index('Paris')} index")
else:
    print('Not found')

#6. Duplicate a List Without Using Loops
numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20]
new_numbers_list = numbers[:]
print (new_numbers_list)

#7. Swap First and Last Elements of a List
nums = [1, 2, 3, 4 ,5, 6, 7, 8, 9,10]
[first, *others, last] = nums
print ([last]+others+[first])

#8. Slice a Tuple
tuple_of_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_of_numbers[3:7])

#9. Count Occurrences in a List
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'blue']
print(colors.count('blue'))

#10. Find the Index of an Element in a Tuple
tuple_of_animals = ('zebra', 'panda', 'horse', 'lion', 'fox', 'wolf')
print(tuple_of_animals.index('lion'))


#11. Merge Two Tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2= (6, 7, 8, 9, 10)
all_tuple = tuple1+tuple2
print(all_tuple)

#12. Find the Length of a List and Tuple
tuple_of_names = ('Ali', 'Vali', 'Halid', 'Muhammad', 'Nilufar')
list_of_surnames = ['Baxtiyorov', 'Hamidov', 'To''lqinov', 'Maqsudov', 'Bahromov']
print(f"length of tuple: {len(tuple_of_names)}, \
length of list: {len(list_of_surnames)}")

#13. Convert Tuple to List
num_tuple = (1, 2, 3, 4, 5)
num_list = list(num_tuple)
print(num_list)

#14. Find Maximum and Minimum in a Tuple
numbers_of_tuple = (1, 2, 3, 4, 5, 6, 10, 45)
max_val = numbers_of_tuple[0]
min_val=numbers_of_tuple[0]
for n in numbers_of_tuple:
    if max_val<n:
        max_val=n
    if min_val>n:
        min_val=n
print (f"MAX value: {max_val}. MIN value: {min_val}")

#15. Reverse a Tuple
tuple_of_words = ('hello', 'salom', 'merhaba', 'privet', 'bonjour')
reversed_tuple = tuple_of_words[::-1]
print(reversed_tuple)
