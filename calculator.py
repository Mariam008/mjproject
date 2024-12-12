num_1 = input("ჩაწერეთ პირველი რიცხვი: ")
num_2 = input("ჩაწერეთ მეორე რიცხვი: ")

operation = input("აირჩიეთ ოპერაცია (+, -, *, /): ")

if operation == "+":
    result = int(num_1) + int(num_2)
    print(result)
elif operation == "-":
    result = int(num_1) - int(num_2)
    print(result)
elif operation == "*":
    result = int(num_1) * int(num_2)
    print(result)
elif operation == "/":
    result = int(num_1) / int(num_2)
    print(result)
else:
    print("არასწორი ოპერაცია")