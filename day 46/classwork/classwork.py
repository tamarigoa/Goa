# 1)
def manual_list(start, end, step, user_num):
    return [num for num in range(start, end, step) if num > user_num]

# ფუნქცა სხვადასხვა არგუმენტებით
print(manual_list(1, 20, 2, 5)) 
print(manual_list(10, 50, 5, 25))  
print(manual_list(-10, 10, 3, -2)) 


# 2)
numbers = [n for n in range(1, 101) if (n % 3 == 0) ]
print(numbers)



# 3)
list1 = [n for n in range(10, 201) if str(n) == str(n)[::-1]]
print(list1)

