class Solution:
    def reverse(self, x: int) -> int:
        tempVar = str(x)
        finalAnswer = ''
        if tempVar.startswith('-'):
            finalAnswer += '-'
            for x in range(len(tempVar)-1,0,-1):
                finalAnswer += str(tempVar[x])
        else:
            for x in range(len(tempVar)-1,-1,-1):
                finalAnswer += str(tempVar[x])
        if(abs(int(finalAnswer)) > (2 ** 31 - 1)):
            finalAnswer = 0
        return int(finalAnswer)
            
