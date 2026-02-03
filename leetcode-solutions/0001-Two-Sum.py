def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    prevMap = {}  # val -> index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

if __name__ == "__main__":
    # Test cases
    print(twoSum([2, 7, 11, 15], 9))  # Expected output: [0, 1]
    print(twoSum([3, 2, 4], 6))       # Expected output: [1, 2]
    print(twoSum([3, 3], 6))          # Expected output: [0, 1]