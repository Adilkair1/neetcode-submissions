class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total = 0
        count = 0

        for w in weight:
            if total + w > 5000:
                break
            total += w
            count +=1
        return count


        