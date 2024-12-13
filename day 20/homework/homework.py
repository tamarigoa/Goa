#homework 1
def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    largest = find_largest(number1, number2, number3)
    print(f"The largest number among {number1}, {number2}, and {number3} is {largest}.")

except ValueError:
    print("Please enter valid numbers.")




#homework 2
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return None  

try:
    score = float(input("Enter the score (0-100): "))
    
    grade = determine_grade(score)
    
    if grade is not None:
        print(f"The grade for the score {score} is: {grade}.")
    else:
        print("Score must be between 0 and 100.")
        
except ValueError:
    print("Please enter a valid numeric score.")






#homework 3
def check_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

try:
    number = float(input("Enter a number: "))

    result = check_number(number)
    print(f"The number {number} is {result}.")

except ValueError:
    print("Please enter a valid number.")







#homework 4
sum_between_numbers=(start,end):
if start > end:
    start, end= end,start
total_sum=0
for num in range(start,end +1):
    return total_sum
start=int(input("enter first integer:"))
end=int(input("enter second integer:"))
result=sum_between_numbers(start, end)
print("sum betveen start and and is:")



#homework 5
def is_prime(number):
    # Handle cases where the number is less than 2
    if number < 2:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#homework 6
numbers=[10, 20, 30, 40, 50]
print("first element" numbers[0])
print("third element" numbers[2])
print("last element" numbers[-1])





#homework 7
my_list=[ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
for i in range (len(my_list)):
    print("elementbat index:")