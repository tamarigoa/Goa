#homework 1
def sum_of_two_numbers(num1, num2):
    return num1 + num2
result = sum_of_two_numbers(5, 3)
print(result)  


#homework 2
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = is_even_or_odd(7)
print(result)  


#homework 3
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))  



#homework 4
def find_maximum(numbers):
    return max(numbers)
numbers = [3, 7, 2, 8, 5]
print(find_maximum(numbers))  
def find_maximum(numbers):
    max_value = numbers[0]  
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value




#homework 5
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
print(f"The factorial of {num} is: {factorial(num)}")
