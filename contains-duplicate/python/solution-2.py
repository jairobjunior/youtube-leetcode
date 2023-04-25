from typing import List

# Time: O(n log n)
# Space: O(1)
# Video: https://youtu.be/0EA465_yMzc
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,1])) # Output: true
print(s.containsDuplicate([1,2,3,4])) # Output: false
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # Output: true