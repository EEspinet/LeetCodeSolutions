class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candySet = set()
        for x in candyType:
            if x not in candySet:
                candySet.add(x)
        candylength = int(len(candyType) / 2)
        setLength = int(len(candySet))
        
        if setLength >= candylength:
            return candylength
        else:
            return setLength
