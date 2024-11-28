#homework1
for i in range(50):
    print("GOA BEST!!!")



#homework2
counter=1
while counter<=10:
    print(counter)
    counter+=1



#homework 3
number=1
while number<=20:
    if number%2==0:
        print(number)
    number+=1


#homework 4
countdown=10
while countdown>0:
    print(countdown)
    countdown-=1
print("Blast off")



#homework 5
correct_password="Goa112233"
user_input=""
while user_input !=correct_password:
    user_input=input("Enter the password")
print("Access granted")




#homework 6
correct_username="GOA Best"
correct_password="1234"
entered_username=""
entered_password=""
while entered_username!=correct_username or entered_password! correct_password:
    entered_username=input("enter your username")
    entered_password=input("enter your password")
if entered_username!=correct_username or entered_password!=correct_password:
    print("incorect username or password. Please try agne")



#homework  7
number=int(input("enter a number to calculate the factorial :"))
if number==0:
    print("The factoial of 0 is 1.")
else:
    factorial=1
    counter=number
    while counter>0:
        factorial*=counter
        counter-=1
print("the factional of number is factotial")
