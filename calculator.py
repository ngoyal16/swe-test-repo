def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the subtraction of b from a."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

def main():
    """Main function to take inputs and print the results based on operation choice."""
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        op = input("Choose the operation (add, subtract, multiply, divide): ").lower()
        if op == 'add':
            print(f"The sum of {a} and {b} is {add(a, b)}.")
        elif op == 'subtract':
            print(f"The subtraction of {b} from {a} is {subtract(a, b)}.")
        elif op == 'multiply':
            print(f"The product of {a} and {b} is {multiply(a, b)}.")
        elif op == 'divide':
            print(f"The division of {a} by {b} is {divide(a, b)}.")
        else:
            print("Invalid operation selected.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
