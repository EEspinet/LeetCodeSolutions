class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dictTemp = {}
        for x in range(len(nums)):
            if nums[x] in dictTemp:
                dictTemp[nums[x]] += 1
            else:
                dictTemp[nums[x]] = 1
        output = []
        for y in dictTemp:
            if dictTemp[y] == 2:
                output.append(y)
        return output
