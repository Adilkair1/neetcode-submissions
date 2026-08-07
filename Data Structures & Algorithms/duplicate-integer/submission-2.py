class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashMap = set()
        for i in nums:
            if i in HashMap:
                
                return True
            HashMap.add(i)
        return False

        