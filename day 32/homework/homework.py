#1.

def greet(name, age):
    return f"Hello {name}, you are {age} years old!"

# 2.
def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"

# 3. 
def reverse_string(s):
    return f"Reversed string: {s[::-1]}"

# 4. 
def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return " ".join(words)

# 5. 
def sentence_to_words(sentence):
    return sentence.split()

# 6. 
def csv_to_list(csv_string):
    return csv_string.split(",")

# 7. 
def paragraph_to_sentences(paragraph):
    return paragraph.split(".")

# 8. 
def append_to_list(lst, item):
    lst.append(item)
    return lst

# 9. 
def extend_list(lst, items):
    lst.extend(items)
    return lst

# 10. 
def merge_lists(list1, list2):
    list1.extend(list2)
    return list1

# 11. 
def insert_at_index(lst, index, item):
    lst.insert(index, item)
    return lst

# 12. 
def insert_at_start(lst, item):
    return [item] + lst

# 13. 
def insert_at_end(lst, item):
    lst.insert(len(lst), item)
    return lst