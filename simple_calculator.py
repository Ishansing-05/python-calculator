print("--- Beginner's Calculator ---")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")

choice = input("Enter your choice (1/2/3/4/5): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    # Addition
    print(num1, "+", num2, "=", (num1 + num2))
elif choice == '2':
    # Subtraction
    print(num1, "-", num2, "=", (num1 - num2))
elif choice == '3':
    # Multiplication
    print(num1, "*", num2, "=", (num1 * num2))
elif choice == '4':
    # Division
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(num1, "/", num2, "=", (num1 / num2))
elif choice == '5':
    # Remainder
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(num1, "%", num2, "=", (num1 % num2))
else:
    print("Invalid choice. Please run the program again.")
