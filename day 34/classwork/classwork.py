#1.
def remove_by_indexes(main_list, indexes_list):

    indexes_list = sorted(indexes_list, reverse=True)

    
    for index in indexes_list:
        if 0 <= index < len(main_list): 
            main_list.pop(index)

    return main_list


main_list = ["a", "b", "c", "d", "e", "f"]
indexes_list = [1, 3, 4]

result = remove_by_indexes(main_list, indexes_list)
print(result)  




#2.
def remove_one_element(lst, index):
    if 0 <= index < len(lst):  
        lst.pop(index)
    print(lst)


my_list = ["a", "b", "c", "d", "e"]
remove_one_element(my_list, 2)  