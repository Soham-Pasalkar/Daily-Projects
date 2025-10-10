history_file = "historyCalculator.txt"

def load_history():
    file = open(history_file,'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found.")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(history_file,'w')
    file.write("")
    file.close()
    print("History cleared.")

def save_history(equation,result):
    file = open(history_file,'a')
    file.write(equation + " = " + result + "\n")
    file.close()

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        return num1 % num2
    elif operation == '**':
        return num1 ** num2
    elif operation == '//':
        if num2 != 0:
            return num1 // num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
    
while True:
    choice = input("Enter Calculation (+, -, *, /, %, **, //) OR Command (history, clear, exit): ")
    if choice in ['+', '-', '*', '/', '%', '**', '//']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculate(num1, num2, choice)
        print(f"Result: {result}")
        save_history(f"{num1} {choice} {num2} = ", str(result))
    elif choice.lower() == 'history':
        load_history()
    elif choice.lower() == 'clear':
        clear_history() 
    elif choice.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")








