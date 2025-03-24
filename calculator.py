def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator! Please enter +, -, *, or /")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

        # Ask user if they want to continue
        choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()


print("Calculator ran successfully !")