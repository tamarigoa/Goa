
#Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)

#Credit Card Mask
def maskify(cc): 
    return "#" * (len(cc) - 4) + cc[-4:] if len(cc) > 4 else cc 

#You're a square!
import math

def is_square(n):
    if n < 0:
        return False
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n

#Find The Parity Outlier
def find_outlier(numbers):
    parity = [num % 2 for num in numbers[:3]]
    majority_even = parity.count(0) > 1

    for num in numbers:
        if (num % 2 == 0) != majority_even:
            return num
        
#Highest and Lowest
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))  
    return f"{max(num_list)} {min(num_list)}"  

#Friend or Foe?   
def summation(num):
    return sum(range(1, num+1))
    

#Convert a String to a Number!
def string_to_number(s):
    return int(s)


#Grasshopper - Summation
def summation(num):
    return sum(range(1, num+1))


#Regex validate PIN code
def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)


#Growth of a Population
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 = int(p0 + p0 * (percent / 100) + aug)  # Ensure population is updated correctly
        years += 1
    return years


#Vowel Count
def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for char in sentence if char in vowels)

