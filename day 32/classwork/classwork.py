#CW1
def generate_big_sentence(name,surname,age):
    print("hello my name is {}, my surname is {}, my age is {}".  format(name, surname, age))
user_name=input("enter your name:")
user_surname=input("enter your surname:")
user_age=input("enter your age:")
generate_big_sentence(user_name, user_surname, user_age)
#hello my name is tamari, my surname is naveriani, my age is 13


#CW2
user_name=input("tamari")
user_surname=input("naveriani")
user_age=input("12")
def generate_big_sentence(name,surname,age):
    print(f"hello my name is {name}, my surname is {surname}, my age is {age}".  format(name, surname, age))
generate_big_sentence(user_name, user_surname, user_age)
#hello my name is tamari, my surname is naveriani, my age is 13


#CW3
def my_split(main_string, string_to_split):
    result=main_string.split(string_to_split)
    print(result)

main_string=input("შემოიტანეთ პირველი ტექსტი:")
string_to_split=input("შემოიტანეთ მეორე ტექსტი:")
my_split(main_string, string_to_split)


#CW4
def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)

my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, ]
manual_append=(my_list, 4)
print(my_list)