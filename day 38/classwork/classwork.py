#classwork 1
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in range(len(tuple)):
    print(f"ინდექსი {i}: {tuple[i]}")


#classwork 2
def no_duplicates(user_list):
    return list(set(user_list)) 

list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = ["Anna", "Marcus", "Anna", "Sara", "Anuky"]
list3 = [True, False, True, False, True, True, False]


print(no_duplicates(list1))
print(no_duplicates(list2))
print(no_duplicates(list3))