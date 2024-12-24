#classwork 1
my_list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = int(input("შეიტანეთ მთელი რიცხვი: "))
if 0 <= index < len(my_list):
    print("{index}: {my_list[index]}")
elif len(my_list) - 1 <= index <= -1:
    print(" {index}: {my_list[index]}")
else:
    print("შესაბამისი ინდექსი არ არსებობს")




#classwork 2
list1=[2,4,6,8,10,12,14,16,18,20]
for element in list1:
    multiplied=element*2
    devided=element/2
    print("ელემენტი გამრავლეული 2-ზე გაყოფილი 2-ზე")