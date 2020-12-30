class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            for i in range(0,len(arr)-2):
                if (not arr[i] % 2 == 0) and (not arr[i+1] % 2 == 0) and (not arr[i+2] % 2 == 0):
                    return True
        return False
