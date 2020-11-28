class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        output = 0
        for x in range(0,len(arr) - 2):
            for y in range(x + 1, len(arr)-1):
                for z in range(y + 1, len(arr)):
                    if x < y and y < z and z < len(arr):
                        if abs(arr[x] - arr[y]) <= a and abs(arr[y] - arr[z]) <= b and abs(arr[x] - arr[z]) <= c:
                            output+=1
        return output
