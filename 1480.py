class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        output = []
        for i in range(0,len(nums)):
            total += nums[i]
            output.append(total)
        return output
