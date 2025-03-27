#code wars
# 1)Beginner Series #2 Clock
def past(h, m, s):
    sum_of_seconds = 0
    
    # hour -> second
    sum_of_seconds += h * 3600
    
    # minute -> second
    sum_of_seconds += m * 60
    
    # second
    sum_of_seconds += s
    
    # result
    result = sum_of_seconds * 1000
    return result


# 2)A Needle in the Haystack
def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}"


# 3) Invert values
def invert(lst):
    new_list=[]
    for i in lst:
        new_list.append(i * -1)
    return new_list


# 4) Calculate average
def find_average(numbers):
    if not numbers: return 0
    return sum(numbers) / len(numbers)


# 5) Sentence Smash
def grow(arr):
    product = 1

    for i in arr:
        product *= i

    return product


# 6) Is he gonna survive?
def hero(bullets, dragons):
    return bullets >= dragons * 2


# 7) How good are you really?
def better_than_average(class_points, your_points):
    other_avg = sum(class_points) / len(class_points)

    if your_points > other_avg: return True
    return False


# 8) Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if arr == []:
        return []

    counter = 0
    sum_negative = 0
    for i in arr:
        if i > 0:
            counter += 1 
        elif i < 0:
            sum_negative += i
    result = [counter,sum_negative]
    if result != [0,0]:
        return result
    return [0,0]


# 9) DNA to RNA Conversion
def dna_to_rna(dna):
    return dna.replace("T", "U")


# 10) Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    return False


# 11) Calculate BMI
def bmi(weight, height):
    bmi_value = weight / height ** 2
        
    if bmi_value <= 18.5: return "Underweight"
    elif bmi_value <= 25.0: return "Normal"
    elif bmi_value <= 30.0: return "Overweight"
    return "Obese"


# 12) Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


# 13) Fake Binary
def fake_bin(x):
    final=""
    for i in x:
        if int(i) < 5:
            final+="0"
        else: final+="1"
    return final


# 14) You only need one - Beginner
def check(seq, elem):
    return elem in seq


# 15) Count by X
def count_by(x, n):
    result = []

    for i in range(1, n+1):
        result.append(x*i)

    return result

