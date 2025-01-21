#UPPER
#HW1
sentence= input("Enter a sentance:")
uppercase_sentence= sentence.upper()
print(" Uppercase version:",)


#HW2
name= input(" Enter your name:")
uppercase_name = name.upper()
print("Your name in uppercase:")



#HW3
def convert_to_uppercase(strings_list):
    return [string.upper() for string in strings_list]



#LOWER
#HW4
sentence=input("Enter a sentence:")
lowercase_sentence=sentence.lower()
print("lowercase version:")


#HW6
email=input("Enter your email address:")
lowercase_email=email.lower()
print("Your email address is in lowercase:")


#HW7
def to_lowercase(mixed_string):
    lowercase_string = mixed_string.lower()
    return lowercase_string

user_input = input("Enter a mixed-case string: ")

result = to_lowercase(user_input)

print("The string in lowercase is:", result)




#CAPITALIZE
#HW8
sentence=input("Enter a sentence:")
capitalized_sentance=sentence.capitalize()
print("capitalized sentence:")


#HW9
lowercase_list=["apple, banana, cherry"]
capitalized_list=[string.capitalize() for string in lowercase_list]
print("capitalized_list:")


#HW10
def capitalize_first_letter(input_string):
    return input_string.capitalize()





#FIND
#HW11
sentence=input("Enter a sentence:")
position=sentence.find("python")
print("the position of python:")


#HW12
main_string= input("enter the main string:")
substring=input("enter the substring to find:")
index= main_string.find(substring)
if index != -1:
    print("substring is correct")
else:
    print("substring is incorrect")


#HW13
def find_char(string, char):
    return string.find(char)




#LEN
#HW14
user_string=input("eenter a string:")
print("lenght of thr string:")


#HW15
def get_lenghts(string_list):
    return[len() for string in string_list]





#COUNT
#HW16
paragraph=input("enter aparagraph:")
count=paragraph.lower().split().count("the")
print("the world 'the' appears {count}times in the patagraph.")


#HW17
input_strig=input("enter a string:")
char=input("enter a character to count its occurrences:")
if len(char) !=1:
    print("please enter only oane character.")
else:
    count=input_strig.count(char)
    print("the char appears {count} times in the string.")


#HW18
def count_word_occurrences(text, word):
    word_count = text.lower().split().count(word.lower())
    return word_count




#INDEX
#HW19
result=find_char("hello","l")
if result != -1:
    print("სიმბოლო (L) გამოიყენება {count}-ჯერ")
else:
    print("სიმბოლო (L) არსად არ გამოიყენება ")


#HW20
input_string = input("Enter a string: ")
input_character = input("Enter a character to find its index: ")

try:
    result = find_char(input_string, input_character)
    if result != -1:
        print("The character '{input_character}' is found at index {result}.")
    else:
        print("The character '{input_character}' is not found in the string.")
except ValueError as e:
    print(e)




#ISLOWER
#HW21
string=input("enter a string:")
if string.islower():
    print("all characters are lowercase")
else:
    print("not all charecters are lowercase")


#HW22
def is_all_lowercase(string):
    return string.islower()


#HW23
string= input("enter a string:")
if string.islower():
    print("the string contains only lowercase  letters.")
else:
    print("not all characters are in the lowercase letters")




#ISUPPER
#HW24
string= input("enter a string:")
if string.isupper():
    print("the string contains only uppercase  letters.")
else:
    print("not all characters are in the uppercase letters")


#HW25
def is_all_uppercase(string):
    return string.isupper()


#HW26
string = input("Enter a string: ")
if string.isupper():
    print("The string is in uppercase.")
else:
    print("The string is not in uppercase.")




#REPLACE
#HW27
sentence = input("Enter a sentence: ")
modified_sentence = sentence.replace("dog", "cat")
print("Modified sentence:", modified_sentence)



#HW28
def replace_spaces_withunderscores(string):
    return string.replace(" ", "")



#SWAPCASE
#HW29
string = input("Enter a string: ")
swapped_string = string.swapcase()
print("Swapped case string:", swapped_string)



#HW30
def swap_case(sentence):
    return sentence.swapcase()

