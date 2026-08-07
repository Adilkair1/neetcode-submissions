class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        res = sorted(count, key=lambda x: count[x], reverse=True)
        return res[:k]

            