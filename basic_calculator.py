num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))
operator = input("Enter the Operator: ")

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    print(f"Result: {num1 / num2}")
else:
    print("Invalid Operator!")