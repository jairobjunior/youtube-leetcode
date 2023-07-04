# Time: O(n)
# Space: O(1)
# Video: https://youtu.be/b9phzUBfwRs
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        
        sCount = {} # char => count
        tCount = {} # char => count
        
        for index in range(len(s)):
            sCount[s[index]] = 1 + sCount.get(s[index], 0)
            tCount[t[index]] = 1 + tCount.get(t[index], 0)

        for char, count in sCount.items():            
            if count != tCount.get(char, 0): return False
        
        return True

s = Solution()
print(s.isAnagram("anagram", "nagaram")) # Output: True
print(s.isAnagram("rat", "cat")) # Output: False
print(s.isAnagram("jogo", "jogador")) # Output: False