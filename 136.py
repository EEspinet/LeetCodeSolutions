class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictOutput = {}
        for num in nums:
            if not num in dictOutput:
                dictOutput[num] = 1
            else:
                dictOutput[num] = dictOutput[num] + 1
        output = 0
        for outputs in dictOutput:
            if dictOutput[outputs] == 1:
                output = outputs
        return output
