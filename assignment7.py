name = input("Enter your name: ")

num1 = int(input("Enter your first favorite number: "))

num2 = int(input("Enter your second favorite number: "))

num3 = int(input("Enter your third favorite number: "))

print(f"\nHello, {name}! Let's explore your favorite numbers: ")

numbers = [num1, num2, num3]

even_odd = []
for number in numbers:
    if number % 2 != 0:
        even_odd.append((number, "odd"))
        print(f"The number {number} is odd.")
    else:
        even_odd.append((number, "even"))
        print(f"The number {number} is even.")

# print(even_odd)

square_tuple = ()
sum = 0
for number in numbers:
    square_tuple = (number, number**2)
    print(f"The number {number} and its square: {square_tuple}")
    sum += number
    
print(f"\nAmazing! The sum of your favorite number is: {sum}")

prime = True
if sum > 1:
    for number in range(2, sum):
        if sum % number == 0:
            prime = False
            break
    if prime:
        print(f"Wow, {sum} is a prime number!")