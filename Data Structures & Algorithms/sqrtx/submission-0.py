class Solution:
    def mySqrt(self, x: int) -> int:
        # use binary search since its logn instead of O(sqrtn)
        l, r = 0, x
        result = 0
        while l <= r:
            m =(l+r)//2
            if m**2>x:
                r = m-1
            elif m**2<x:
                l=m+1
                result = m
            else: 
                return m
        return result
            

                  


        