class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minTime = 0
        firstTime = True
        for point in points:
            if firstTime == True:
                x = point[0]
                y = point[1]
                firstTime = False
            else:
                timeX = abs(x - point[0])
                timeY = abs(y - point[1])
                x = point[0]
                y = point[1]
                if timeX > timeY:
                    minTime += timeX
                else:
                    minTime += timeY
                
        return minTime
