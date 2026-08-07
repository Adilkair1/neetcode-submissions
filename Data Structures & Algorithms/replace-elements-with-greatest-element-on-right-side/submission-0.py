class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = 0
        for i in range(len(arr)-1, -1, -1):
            current_value = arr[i]
            arr[i] = max_right
            if current_value > max_right:
                max_right = current_value
        arr[-1] = -1

        return arr

        


        