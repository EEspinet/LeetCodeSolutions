class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        for i in range(0,len(nums)-1):
            for j in range(i + 1,len(nums)):
                var1 = nums[i] - 1
                var2 = nums[j] - 1
                # print(str(i) + ' ' + str(j) )
                if (var1 * var2) > max:
                    max = var1 * var2
        return max
