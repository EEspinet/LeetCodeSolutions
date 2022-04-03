class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        fullSet = []
        intersectionSet = []
        for i in range(1,arr[-1] + k + 1):
            fullSet.append(i)
        for i in fullSet:
            if i not in arr:
                intersectionSet.append(i)
        return intersectionSet[k-1]