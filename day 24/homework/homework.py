#homework1
my_list = [10, 20, 30, 40]
first_element = my_list[0]
print(first_element)



#homework2
my_list = [10, 20, 30, 40]
last_element = my_list[-1]
print(last_element)



#homework3
my_list = [10, 20, 30, 40, 50]
first_three_elements = my_list[:3]
print(first_three_elements)


#homework4
my_string = "Hello, world!"
last_five_chars = my_string[-5:]
print(last_five_chars)



#homework5
my_string = "Hello, world!"
reversed_string = my_string[::-1]
print(reversed_string)



#homework6
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
every_third_element = my_list[::3]
print(every_third_element)




#homework7
my_list = [10, 20, 30, 40, 50, 60]
mid_index = len(my_list) // 2  # Get the middle index

first_half = my_list[:mid_index]
second_half = my_list[mid_index:]

print("First half:", first_half)
print("Second half:", second_half)





#bosslewel
def draw_square(x_cordinate, y_cordinate):
    penup()
    goto(x_cordinate, y_cordinate)
    pendown()
    for i in range (4):
        forward(200)
        left(90)
draw_square(100,100)
draw_square(-300,100)
draw_square(-300,1300)
draw_square(100,-300)