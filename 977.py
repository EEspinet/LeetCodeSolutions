class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = map(lambda x:x**2,nums)
        output = list(output)
        output.sort()
        return output
