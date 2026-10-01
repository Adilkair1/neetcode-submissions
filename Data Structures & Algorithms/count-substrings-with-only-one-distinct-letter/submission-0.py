class Solution:
    def countLetters(self, s: str) -> int:
        run = 0
        total = 0
        for i in range (len(s)):
            if i>0 and s[i]==s[i-1]:
                run += 1
            else:
                run = 1
            total +=run
        return total

        