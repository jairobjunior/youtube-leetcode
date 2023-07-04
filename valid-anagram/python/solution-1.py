# Time: O(NlogN)
# Space: O(1)
# Video: https://youtu.be/b9phzUBfwRs
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        return sorted(s) == sorted(t)

s = Solution()
print(s.isAnagram("anagram", "nagaram")) # Output: True
print(s.isAnagram("rat", "cat")) # Output: False
print(s.isAnagram("jogo", "jogador")) # Output: False