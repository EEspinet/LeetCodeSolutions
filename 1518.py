class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        fullBottles = numBottles
        count = 0
        
        
        while fullBottles >= 1:
            
            count += fullBottles
            
            # Bottles consumed
            emptyBottles += fullBottles
            
            fullBottles = int(emptyBottles/numExchange)
            emptyBottles = int(emptyBottles%numExchange)
            # print(count)
            # print(fullBottles)
            # print(emptyBottles)
        return int(count)
