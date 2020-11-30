class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        letterDict = {}
        for letters in text:
            if letters in letterDict:
                letterDict[letters] += 1
            else:
                letterDict[letters] = 1
        
        done = False
        while not done:
            if 'b' in letterDict and 'a' in letterDict and 'l' in letterDict and 'o' in letterDict and 'n' in letterDict:
                if letterDict['b'] >= 1 and letterDict['a'] >= 1 and letterDict['l']>= 2 and letterDict['o'] >= 2 and letterDict['n'] >= 1:
                    count+=1
                    letterDict['b'] -= 1
                    letterDict['a'] -= 1
                    letterDict['l'] -= 2
                    letterDict['o'] -= 2
                    letterDict['n'] -= 1
                else:
                    done = True
            else:
                done = True
        return count
