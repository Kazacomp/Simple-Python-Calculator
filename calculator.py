def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def divided_by(a, b):
    if b == 0:
        return "Cannot be divided by 0!"
    return a / b


print("=== SIMPLE CALCULATOR ===")

while True:
    print("\nSelect operation:")
    print("1. Plus")
    print("2. Minus")
    print("3. Times")
    print("4. Divided by")
    print("5. Exit")

    choice = input("Enter options (1-5): ")

    if choice == "5":
        print("Program completed.")
        break

    if choice in ["1", "2", "3", "4"]:
        value1 = float(input("Input first number: "))
        value2 = float(input("Input second number: "))

        if choice == "1":
            print("Result:", plus(value1, value2))

        elif choice == "2":
            print("Result:", minus(value1, value2))

        elif choice == "3":
            print("Result:", times(value1, value2))

        elif choice == "4":
            print("Result:", divided_by(value1, value2))

    else:
        print("Option Invalid!")
