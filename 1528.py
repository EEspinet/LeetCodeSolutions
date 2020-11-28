class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        positionNum = 0
        tempList = list(range(len(indices)))
        for x in range(0,len(indices)):
            tempList[int(indices[x])] = s[x]
        resultString = ''
        for y in tempList:
            resultString+=y
        return resultString
