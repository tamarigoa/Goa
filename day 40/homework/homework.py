# Codewars



# 1) Function 1 - hello world
def greet():
    # აბრუნებს სტრიქონს "hello world!"
    return "hello world!"


# 2) Counting sheep...
def count_sheeps(sheep):
    # ითვლის True მნიშვნელობების რაოდენობას სიის 
    return sheep.count(True)


# 3) Remove String Spaces
def no_space(x):
    # შლის ყველა ცარიელ ადგილს (space) სტრიქონიდან
    return x.replace(" ", "")


# 4) You Can't Code Under Pressure #1
def double_integer(i):
    # აბრუნებს რიცხვს გაორმაგებულად
    return i * 2


# 5) Returning Strings
def greet(name):
    # აბრუნებს მისალმებას, სადაც სახელის მნიშვნელობა ჩასმულია
    return f"Hello, {name} how are you doing today?"


# 6) Convert a Boolean to a String
def boolean_to_string(b):
    # გარდაქმნის Boolean მნიშვნელობას (True/False) სტრიქონად ("True"/"False")
    return str(b)


# 7) Basic Mathematical Operations
def basic_op(operator, value1, value2):
    # ასრულებს მათემატიკურ ოპერაციებს შესაბამისი ოპერატორის მიხედვით
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2  # "/" გაყოფას ნიშნავს


# 8) Keep Hydrated!
def litres(time):
    # აბრუნებს საათების რაოდენობის ნახევარს, რადგან სვამს 0.5 ლ წყალს საათში
    return time // 2  # მთელ რიცხვზე გაყოფა (floor division)
# 9) Century From Year
def century(year): 
    # თუ წელი ზუსტად იყოფა 100-ზე, მაშინ ის უკვე იმ საუკუნეშია
    if year % 100 == 0:
        return year // 100
    else:
        # წინააღმდეგ შემთხვევაში, საუკუნე +1
        return year // 100 + 1


# 10) Convert number to reversed array of digits
def digitize(n):
    # გარდაქმნის რიცხვს სტრიქონად
    starting_str = str(n)
    # აბრუნებს შებრუნებულ სტრიქონს
    reversed_str = starting_str[::-1]

    res_list = []
    # თითოეული ციფრი გადაყავს მთლიან რიცხვად და ამატებს სიაში
    for i in reversed_str:
        res_list.append(int(i))

    return res_list


# 11) Beginner - Lost Without a Map
def maps(a):
    saver = []
    # თითოეულ ელემენტს სიაში ორმაგავს
    for i in a:
        saver.append(i * 2)
    return saver


# 12) Opposites Attract
def lovefunc(flower1, flower2):
    # აბრუნებს True-ს, თუ ერთის ფურცლების რაოდენობა კენტია, ხოლო მეორესი ლუწი (ან პირიქით)
    return (flower1 + flower2) % 2 == 1


# 13) Sum Arrays
def sum_array(a):
    # აბრუნებს სიის ელემენტების ჯამს
    return sum(a)

# 14) Beginner Series #1 School Paperwork
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0


# 15) MakeUpperCase
def make_upper_case(s):
    return s.upper()


# 16) Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


# 17) Abbreviate a Two Word Name
def abbrev_name(name):
    parts = name.split()  
    return f"{parts[0][0].upper()}.{parts[1][0].upper()}" 





