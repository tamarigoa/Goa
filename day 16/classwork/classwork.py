#საკლასო დავალება: მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში მთელი რიცხვის სახით.

#შემდეგ შექმენით დიაპაზონი 0-დან ამ რიცხვამდე და დაბეჭდეთ დიაპაზონის ყველა რიცხვის ჯამი.

#გამოიყენეთ for ციკლი

#number1
first_number=int(input("Enter your first number"))
second_number=int(input("enter your number"))
for number in range(first_number, second_number+1):
    print(number**2)



#number2
correct_password="mypassword123" #ჩაწერეთ ნებისმიერი პაროლი
attempt_count=0#ცვლადის მცდელობის დასატვლელად
  #შემოატანინეთ მომხმარებელს პაროლი
user_input=input("შეიყვანეთ პაროლი")
attempt_count+=1 #მცდელობის რაოდენობის გაზრდა
   #პაროლის შმოწმება
if user_input==correct_password:
    print("Acces granted!")
    break #ციკლის შეწყვეტა
else:
    print("არასწორი პაროლი,სცადეთ თავიდან")
    #მცდელობის დაბეჭდვა
print("პაროლის შეყვანა მოგიწვიათ {attempt_count}ჯერ")



#classwork 3

#რიცხვის გამოცნობის პროგრამა:

#შექმენით my_num ცვლადი და 1-დან 10-მდე ნებისმიერი რიცხვი მიანიჭეთ მნიშვნელობად.

#სანამ მომხმარებლის შემოტანილი რიცხვი არ იქნება my_num-ის ტოლი, ისევ შეეკითხეთ მომხმარებელს ეს რიცხვი.

#საბოლოოდ დაუბეჭდეთ "you guessed" და რამდენი ცდა დაჭირდა```

import random
my_num=random.randint(1,10)
attempt_count=0
user_guess=int(input("გამოიცანიტ 1-10-მდე რიცხვი:"))
attempt_count+=1
if user_guess==my_num:
    print("you guesd")
    break
else:
    print("არასწორია,სცადეთ თავიდან")