def reverse_string(s):
    """
    Reverses the input string.
    
    Parameters:
    s (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]

if __name__ == "__main__":
    input_string = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(input_string))