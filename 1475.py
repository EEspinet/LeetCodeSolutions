class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        foundFlag = False
        for i in range(0,len(prices) - 1):
            foundFlag = False
            for j in range(i + 1, len(prices)):
                if j > i and prices[j] <= prices[i]:
                    output.append(prices[i] - prices[j])
                    foundFlag = True
                    break
            if not foundFlag:
                output.append(prices[i])
        output.append(prices[len(prices) - 1])
        return output
