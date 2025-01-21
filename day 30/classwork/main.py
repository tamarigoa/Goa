#classwork.1
name=input("Enter your name:")
choice= input("select case:u/l -")

if choice == "u": 
    print(name.upper())
elif choice== "l":
    print(name.lower)
else:print(" Wrong information ")




#classwork.2
def manual_find(main_string, str_to_find):
    for char in range (len(main_string)):
        if main_string[char] == str_to_find:
            print(char)
            






#classwork.3
main_str=int(input("Enter your main string:"))
str_to_count=int(input("Enter your main string to count:"))
print(str_to_count)





#classwork.4
def manual_swapcase(main_str):
    res= ""
for char in main_str:
    if char.islower(): res += char.upper()
    else: res += char.lower()
    print(res)