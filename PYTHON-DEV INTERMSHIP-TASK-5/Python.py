def add(a, b=0):
    """
    Returns the sum of two numbers.
    Default value of b is 0.
    """
    return a + b


def subtract(a, b=0):
    """
    Returns the difference of two numbers.
    Default value of b is 0.
    """
    return a - b


def multiply(a, b=1):
    """
    Returns the product of two numbers.
    Default value of b is 1.
    """
    return a * b


def divide(a, b):
    """
    Returns the division result of two numbers.
    Handles division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def get_numbers():
    """
    Takes two numbers as input from the user.
    Returns them as floats.
    """
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def calculator():
    """
    Main calculator logic.
    Calls functions based on user choice.
    """
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose an operation (1/2/3/4): ")

    a, b = get_numbers()

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
    else:
        result = "Invalid choice"

    print("Result:", result)


# Program execution starts here
calculator()
