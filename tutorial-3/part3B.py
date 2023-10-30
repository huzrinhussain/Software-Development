print('Welcome to my boring calculatorr!!')
while True:
    # Input from the user
    expression = input("Enter an arithmetic expression (or 'exit' to quit): ")

    # Check if the user wants to exit
    if expression == 'exit':
        break

    try:
        # Evaluate the expression
        result = eval(expression)
        print(f"Result: {result}")
    except (SyntaxError, NameError, TypeError):
        print("Invalid input. Please enter a valid arithmetic expression.")