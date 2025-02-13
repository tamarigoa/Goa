#1
my_tuple = (10, 20, 30, 40, 50)
second_element = my_tuple[1]
last_element = my_tuple[-1]
middle_slice = my_tuple[1:4]

print("Second Element:", second_element)
print("Last Element:", last_element)
print("Middle Three Elements:", middle_slice)

#2
try:
    my_tuple[1] = 100  
except TypeError as e:
    print("Error:", e)  

#3
packed_tuple = ("Alice", 25, "Engineer")
name, age, profession = packed_tuple

print("Name:", name)
print("Age:", age)
print("Profession:", profession)

#4
repeated_tuple = (1, 2, 3, 2, 2, 4, 5)
count_of_twos = repeated_tuple.count(2)
index_of_three = repeated_tuple.index(3)

print("Count of 2:", count_of_twos)
print("Index of 3:", index_of_three)

#5
my_set = {10, 20, 30, 40, 50}
my_set.add(60)  
my_set.remove(30) 
is_present = 20 in my_set 

print("Updated Set:", my_set)
print("Is 20 in the set?", is_present)

#6
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2 
intersection_set = set1 & set2  
difference_set = set1 - set2  

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

#7
duplicate_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_set = set(duplicate_list)  
unique_list = list(unique_set)  

print("List after removing duplicates:", unique_list)