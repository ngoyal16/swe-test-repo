def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the subtraction of b from a."""
    return a - b

def main():
    """Main function to take inputs and print the sum and subtraction."""
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The sum of {a} and {b} is {add(a, b)}.")
        print(f"The subtraction of {b} from {a} is {subtract(a, b)}.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
