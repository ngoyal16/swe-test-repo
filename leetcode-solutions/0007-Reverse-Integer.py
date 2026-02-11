def reverse(x: int) -> int:
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
    """
    if x >= 0:
        reversed_x = int(str(x)[::-1])
    else:
        reversed_x = -int(str(-x)[::-1])

    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0

    return reversed_x

if __name__ == "__main__":
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # Overflow case, reverse is 9646324351 > 2147483647
    ]

    for x, expected in test_cases:
        result = reverse(x)
        print(f"reverse({x}) = {result}, expected: {expected}")
        assert result == expected
