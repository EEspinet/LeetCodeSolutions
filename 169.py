class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sizeToBeat = (len(nums) / 2)
        tempDict = {}
        for x in nums:
            if x in tempDict:
                tempDict[x] = tempDict[x] + 1
            else:
                tempDict[x] = 1
        print(tempDict)
        for y in tempDict:
            if tempDict[y] > sizeToBeat:
                return y
        return 0
