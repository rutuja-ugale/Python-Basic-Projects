def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

def menu():
    print("====== Calculator ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    menu()
    choice = int(input("Enter Your Choice (1-5): "))

    if choice == 5:
        print("Thank you for using Calculator!")
        break

    if choice not in [1, 2, 3, 4]:
        print("Invalid Choice. Please Select a valid Option (1-5).")
        continue

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    if choice == 1:
        res = addition(a, b)
        print(f"Addition of {a} and {b} is: {res}.")
    elif choice == 2:
        res = subtraction(a, b)
        print(f"Subtraction of {a} and {b} is: {res}.")      
    elif choice == 3:
        res = multiplication(a, b)
        print(f"Multiplication of {a} and {b} is: {res}.")        
    elif choice == 4:
        if b == 0:
            print("Division by zero is not allowed.")
        else:
            res = division(a, b)
            print(f"Division of {a} and {b} is: {res}.")
    else:
        print("Invalid Choice. Please Select a valid Option (1-5).")