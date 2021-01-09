class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak = -1
        position = - 1
        peakPosition = 0
        for nums in arr:
            position+=1
            if nums > peak:
                peak = nums
                peakPosition = position
        return peakPosition
