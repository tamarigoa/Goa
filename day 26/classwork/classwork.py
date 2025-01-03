#classwork 1
def greet(name):
    print("გამარჯობა", name)
greet("თამარი")




#classwork 2
def manual_range(start, end, step):
    for i in range(start, end, step):
        if i % 2 == 0: 
            print(i)
manual_range(1, 10, 1)  
manual_range(0, 20, 2)  
manual_range(5, 30, 3)  
manual_range(10, 50, 5) 
manual_range(2, 15, 3)  


#classwork 3
def manual_len(my_list):
    count = 0  
    for item in my_list:  
        count += 1  
    print("სიის სიგრძეა:", count)  
    return count  
example_list = [1, 2, 3, 4, 5]
manual_len(example_list) 