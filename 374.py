# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        found = False
        lowerBound = 1
        higherBound = n
        while not found:
            tempNum = int((higherBound+lowerBound)/2)
            tempGuess = guess(tempNum)
            if tempGuess == -1:
                higherBound = tempNum-1
            elif tempGuess == 1:
                lowerBound = tempNum+1
            else:
                return tempNum