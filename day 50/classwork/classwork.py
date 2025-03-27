# Task 1: 
try:
    num = 10 
    result = num + "hello"  
except TypeError as e:
    print(f"An error occurred: {e}")

# Task 2: 
try:
    user_input = input("Enter your name: ") 

    if not user_input.strip():
        raise ValueError("Input cannot be empty.")

    num_value = int(user_input)  

except ValueError as e:
    print(f"ValueError occurred: {e}")

except KeyboardInterrupt:
    print("\nProcess interrupted by user.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print(f"Your name is: {user_input}")

finally:
    print("Execution finished.")