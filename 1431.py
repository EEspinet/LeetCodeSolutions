class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = 0
        for candy in candies:
            if candy > maxCandy:
                maxCandy = candy
        output = []
        print("MaxCandy: " + str(maxCandy))
        for candy in candies:
            # print(candy + extraCandies)
            newTotal = candy + extraCandies
            if newTotal >= maxCandy:
                # print(newTotal)
                output.append(True)
            elif maxCandy > newTotal:
                # print("Hellloo")
                output.append(False)
        return output
