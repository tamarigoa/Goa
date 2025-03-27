# 1)
numbers = [x for x in range(1, 11)]
print(numbers)  

# 2) 
squares = [x**2 for x in range(1, 6)]
print(squares)  

# 3) 
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)  

# 4) 
words = ["apple", "banana", "cherry", "date"]
first_letters = [word[0] for word in words]
print(first_letters)

# 5)
uppercase_words = [word.upper() for word in words]
print(uppercase_words) 

# 6) 
div_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(div_by_3)  


# 7) 
words = ["apple", "cat", "banana", "dog", "elephant"]
long_words = [word for word in words if len(word) > 4]
print(long_words)  


# 8) 
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  


# 9)
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)  


# 10) 
sentence = "The quick brown fox jumps over the lazy dog and explores the wilderness"
words = sentence.split()
vowels = {'a', 'e', 'i', 'o', 'u'}
filtered_words = [word for word in words if len(word) > 5 and any(v in word.lower() for v in vowels)]
print(filtered_words)  


# 11) 
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(18)]
print(fibonacci)  
