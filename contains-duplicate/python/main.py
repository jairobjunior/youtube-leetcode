from typing import List

# Time: O(n)
# Space: O(n)
# Video: https://youtu.be/0EA465_yMzc
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,1])) # Output: true
print(s.containsDuplicate([1,2,3,4])) # Output: false
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # Output: true