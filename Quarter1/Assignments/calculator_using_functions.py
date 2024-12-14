def add(num1, num2):
    sum = num1+num2
    return sum

def sub(num1, num2):
    sub = num1-num2
    return sub

def mul(num1, num2):
    prod = num1*num2
    return prod

def div(num1, num2):
    div = num1/num2
    return div

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("Enter the operation you want to perform: ")

result = 0

if operator == "+":
    result = add(first_number, second_number)
    print(f"The result of {first_number} {operator} {second_number} is: {result}")
elif operator == "-":
    result = sub(first_number, second_number)
    print(f"The result of {first_number} {operator} {second_number} is: {result}")
elif operator == "*":
    result = mul(first_number, second_number)
    print(f"The result of {first_number} {operator} {second_number} is: {result}")
elif operator == "/":
    result = div(first_number, second_number)
    print(f"The result of {first_number} {operator} {second_number} is: {result}")