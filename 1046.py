class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        outputList = []
        done = False
        while len(stones) > 1:
            stones.sort()
            firstVar = stones[-2]
            secondVar = stones[-1]
            if firstVar == secondVar:
                stones.pop()
                stones.pop()
            else:
                if firstVar > secondVar:
                    stones.pop()
                    stones.pop()
                    stones.append(firstVar-secondVar)
                else:
                    stones.pop()
                    stones.pop()
                    stones.append(secondVar-firstVar)
        print(stones)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
