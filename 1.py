class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listSize = len(nums)
        answerList = []
        for i in range(listSize - 1):
            for j in range(i + 1, listSize):
                if nums[i] + nums[j] == target:
                    answerList.append(i)
                    answerList.append(j)
        
        return answerList
