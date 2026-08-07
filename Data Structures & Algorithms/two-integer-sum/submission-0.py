class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       HashMap = {}
       for i,n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[n] = i
       return