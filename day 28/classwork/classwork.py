def manual_index(main_string, search_string):
    for i in range(len(main_string) - len(search_string) + 1):
        if main_string[i:i + len(search_string)] == search_string:
            return i
    return -1


print(manual_index("hello world", "world"))  
print(manual_index("hello world", "hello"))  
print(manual_index("hello world", "Python"))  