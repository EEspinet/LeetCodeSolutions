class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for x in range(0,len(flowerbed)):
            if x == 0:
                if len(flowerbed) > 1:
                    if flowerbed[x] == 0 and flowerbed[x+1] == 0:
                        count+=1
                        flowerbed[x] = 1
                else:
                    if flowerbed[x] == 0:
                        count+=1
                        flowerbed[x] == 1
            elif x == len(flowerbed) - 1:
                if flowerbed[x] == 0 and flowerbed[x-1] == 0:
                    flowerbed[x] = 1
                    count+=1
            else:
                if flowerbed[x] == 0:
                    if flowerbed[x-1] == 0 and flowerbed[x+1] == 0:
                        count+=1
                        flowerbed[x] = 1
        print(count)
        return count >= n
