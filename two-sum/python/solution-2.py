from typing import List

# Time: O(n)
# Space: O(n)
# Video: https://youtu.be/P-StcnuCqJQ
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    numsVisited = {} # num => index
    for i, num in enumerate(nums):
      diff = target - num
      if diff in numsVisited:
        return [numsVisited[diff], i]
      numsVisited[num] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9)) # Output: [0,1]
print(s.twoSum([3,2,4], 6)) # Output: [1,2]
print(s.twoSum([3,3], 6)) # Output: [0,1]