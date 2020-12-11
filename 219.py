class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsDict = {}
        for index in range(0,len(nums)):
            if nums[index] in numsDict:
                numsDict[nums[index]].append(index)
            else:
                numsDict[nums[index]] = [index]
        # print(numsDict)
        for entries in numsDict:
            if len(numsDict[entries]) >= 2:
                for entry in range(0,len(numsDict[entries]) - 1):
                    if numsDict[entries][entry + 1] - numsDict[entries][entry] <= k:
                        return True
        return False
