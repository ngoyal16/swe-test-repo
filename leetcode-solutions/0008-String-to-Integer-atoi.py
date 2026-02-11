def myAtoi(s: str) -> int:
    """
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
    6. Return the integer as the final result.

    Note:
    - Only the space character ' ' is considered a whitespace character.
    - Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    i = 0
    n = len(s)

    # 1. Skip spaces
    while i < n and s[i] == ' ':
        i += 1

    if i == n:
        return 0

    # 2. Check sign
    sign = 1
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1

    # 3. Process digits
    result = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit
        i += 1

    result = sign * result

    # 4. Clamp
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("+1", 1),
        ("+-12", 0),
        ("00000-42a1234", 0),
        ("  +  413", 0),
        ("", 0),
        (" ", 0),
        ("2147483648", 2147483647),
        ("-2147483649", -2147483648),
    ]

    for s, expected in test_cases:
        result = myAtoi(s)
        status = "Pass" if result == expected else "Fail"
        print(f"Input: '{s}', Output: {result}, Expected: {expected}, Status: {status}")
