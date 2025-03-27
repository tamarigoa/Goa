# 1)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi", "salary": "programist"}
print(my_dict.keys())

# 2)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
print(my_dict.values())

# 3)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
print(my_dict.items())

# 4)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 5)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
if "age" in my_dict:
    print("key exists!")
else:
    print("key doesnt exist!")

# 6)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
print(my_dict.get("age" "key not found"))
print(my_dict.get("name" "key not found"))

# 7)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
my_dict["salary"]=100
print(my_dict)

# 8)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
my_dict.pop("age")
print(my_dict)

# 9)
new_data={"country":"georgia","language":"georgian"}
my_dict.update(new_data)
print(my_dict)

# 10)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
print(len(my_dict))

# 11)
def sum_numeric_values(d):
    return sum(value for value in d.values() if isinstance(value, (int, float)))

numeric_dict={"a": "10","b": "20","c": "hello", "d": "30,5"}
print(sum_numeric_values(numeric_dict))

# 12)
my_dict={"name": "tamari", "age": "12", "city": "Tbilisi"}
my_dict.clear()
print(my_dict)

# 13)
my_info={
    "name"="tamari",
    "surname"="naveriani",
    "age"=13,
    "hight"=1,60,
    "country"="georgia",
    "language"="georgian",
    "pet"="dog",
    "GOA student"="true",
    "city"="tbilisi",
    "fav color"="baby-pink",
}
print(my_info)