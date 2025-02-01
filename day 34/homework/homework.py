# 1) 
def hello_world():
    print("Hello, World!")

# 2) 
def sum_numbers(a, b):
    print(a + b)

# 3) 
def multiply_by_ten(num):
    return num * 10

# 4) 
def greet(name="Guest"):
    print(f"Hello, {name}!")

# 5) Boss Level
def outer_function():
    def inner_function():
        print("This is the inner function")
    inner_function()

# 6) 
def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

# 7) 
def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# 8) 
def filter_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

# 9) 
def sum_divisible_by_three(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            total_sum += sum
    return total_sum