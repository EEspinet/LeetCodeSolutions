class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        targetHeights = heights.copy()
        targetHeights.sort()
        
        output = 0
        # print(targetHeights)
        # print(heights)
        for x in range(0,len(targetHeights)):
            # print(x)
            if not heights[x] == targetHeights[x]:
                output+=1
        return output1051
