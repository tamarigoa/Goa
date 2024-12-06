#homework1
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>num2:
    print("num1")
elif num1<num2:
    print("num2")
else:
    print("both numbers are right")


#homework2
number=int(input("Enter a  number:"))
if number % 2 ==0:
    print("the number is even")
else:
    print("the number is odd")



#homework3
number=int(input("enter a number:"))
if number>0:
    print("the number is positive")
elif number<0:
    print("the number is negetive")




#homework4
number=int(input("enter a number:"))
if number % 5 == 0:
    print("the number is divisible by 5:")
else:
    print("the number isnt divisable by5:")




#homework5
for i in range (5):
    number=int(input("Enter number:"))
    if number % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")



#homework5
correct_password="Goa best"
incorrect_count=0
while True:
    password=input("Enter the password:")
if password == correct_password:
    print("Access granted!")
else:
    incorrect_count+=1
    print("incorrect password please try aagain")
    print("number of incorect attempts:")




#homework6
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operator=input("Enter an operator (+,-,*,/)")
if operator == "+":
    print("num1+num2")
if operatot == "-":
     print("num1-num2")
if operatot == "*":
     print("num1*num2")
if operatot == "/":
     print("num1/num2")
