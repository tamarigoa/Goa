#homework1
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for element in elements:
    print(element)

#homework2
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num1 = int(input("შეიტანეთ პირველი რიცხვი (num1): "))
num2 = int(input("შეიტანეთ მეორე რიცხვი (num2): "))

if num1 > num2:
    new_list = elements[num1:num2]
    print("ახალი სია:", new_list)
elif num2 > num1:
    new_list = elements[num2:num1]
    print("ახალი სია:", new_list)
else:
    print("ცარიელი სია:", [])



#homework3
numbers = [10, 20, 30, 40, 50]

first_element = numbers[0]        
third_element = numbers[2]       
last_element = numbers[-1]        

print("First element:", first_element)
print("Third element:", third_element)
print("Last element:", last_element)






#homework4
strings_list = ["apple", "banana", "cherry", "date"]

print(strings_list[::-1])





#homework5
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
result = words[::2]  # This selects every second element starting from the first
print(result)







#homework6
numbers = [10, 20, 30, 40, 50]  
numbers[3] = 100  
print(numbers)