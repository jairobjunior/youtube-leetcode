from typing import List

# Time: O(n^2)
# Space: O(1)
# Video: https://youtu.be/P-StcnuCqJQ
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i,j]

s = Solution()
print(s.twoSum([2,7,11,15], 9)) # Output: [0,1]
print(s.twoSum([3,2,4], 6)) # Output: [1,2]
print(s.twoSum([3,3], 6)) # Output: [0,1]