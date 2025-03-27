# 1) 
try:
    user_input = input("Enter a number: ")
    number = float(user_input) 
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: Please enter a valid number.")

# 2)
my_list = [1, 2, 3]
try:
    print(my_list[5])  
except IndexError:
    print("Error: Index out of range.")

# 3) 
try:
    result = "Hello" + 5  
except TypeError:
    print("Error: Cannot add a string and an integer.")

# 4) საკლასო დავალება დაწერილი მაქვს 

# 5) level 50-ის ყველაფერს გადავხედე
