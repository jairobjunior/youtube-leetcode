from typing import List

# Time: O(n^2)
# Space: O(1)
# Brute Force (Time Limit Exceeded)
# Video: https://youtu.be/0EA465_yMzc
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,1])) # Output: true
print(s.containsDuplicate([1,2,3,4])) # Output: false
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # Output: true