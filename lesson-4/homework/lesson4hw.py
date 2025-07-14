# # #Python Dictionary Exercises

# # #1. Sort a Dictionary by Value
my_dict = {'banana': 1, \
'apple' : 3, 'orange': 2,
'pineapple': 4}
#sorting in asc  order 
sorted_by_val_asc = sorted(my_dict.items(), key=lambda item: item[1])
print(sorted_by_val_asc)
#sorting in desc order
sorted_by_val_desc = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_by_val_desc)

# # #2. Add a Key to a Dictionary
sample_dict  = {0:10, 1:20}
sample_dict.update([(2,30)])
sample_dict.update([(3,40)])
print(sample_dict)

# # #3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# #4. Generate a Dictionary with Squares
n=5
ranged  = range(1, n+1)
mapped = map(lambda x: x*x, ranged)
all = zip(ranged, mapped)
print(dict(all))

# #5. Dictionary of Squares (1 to 15)
p = 15
ranging = range(1, p+1)
mapping = map(lambda x: x*x, ranging)
zipping = zip(ranging, mapping)
print(dict(zipping))

#Set exercises
#1. Create a Set
r= range(15)
print(set(r))

#2. Iterate Over a Set
my_set = {3,5,6,7,8,9,10,11,12,3}
for s in my_set:
    print(s)

#3. Add Member(s) to a Set
another_set = {1,2,3,4,5,6,7,8,9,10}
another_set.update(['apple', 11,12,13,14])
print(another_set)

#4. Remove Item(s) from a Set
your_set = {3,5,6,7,8,9,10,11,12,3}
your_set.pop() #removes ant set member
print(your_set)

#5. Remove an Item if Present in the Set
her_set = {3,5,6,7,8,9,10,11,12,3}
if 8 in her_set:
        her_set.discard(8)
if 8 not in her_set:
        print('there is no such thing in the set')
print(her_set)
