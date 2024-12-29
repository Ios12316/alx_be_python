number1 = 20
number2 = 5
operation = "*"
print(f"Choose the operation (+, -, *, /): {operation}")
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
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            result = number1 / number2
            print(f"The result is {result}")