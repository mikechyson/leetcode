# Given an array of integers arr,
# return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Example 1:
#
# Input: arr = [2,1]
# Output: false
# Example 2:
#
# Input: arr = [3,5,5]
# Output: false
# Example 3:
#
# Input: arr = [0,3,2,1]
# Output: true

# Constraints:
#
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False

        max_index = arr.index(max(arr))

        if max_index == 0 or max_index == length - 1:
            return False

        for i in range(0, max_index):
            if arr[i] >= arr[i + 1]:
                return False

        for i in range(max_index, length - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True


if __name__ == '__main__':
    arr = [0, 3, 2, 1]
    arr = [3, 5, 5]
    # arr = [2, 1]
    # arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sol = Solution()
    result = sol.validMountainArray(arr)
    print(result)
