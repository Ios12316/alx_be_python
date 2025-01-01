number1 = float(input("Enter your first number:"))
number2 = float(input("Enter your second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        result = number1 +number2
        print(f"The result is {result}")
    case "-":
        result = number1 - number2
        print(f"The result is {result}")
    case "*":
        result = number1 * number2
        print(f"The result is {result}")
    case "/":
        if number2 != 0:
            result = number1 / number2
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed.")