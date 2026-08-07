class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        maxT = 0
        for r in range(len(s)):
            char = s[r]
            while char in window:
                window.remove(s[l])
                l += 1
            window.add(char)
            maxT = max(maxT, r - l + 1)
        return maxT
        