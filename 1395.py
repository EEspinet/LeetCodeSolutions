class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total = 0
        for x in range(0,len(rating)- 2):
            for y in range(x + 1, len(rating)-1):
                for z in range(y + 1, len(rating)):
                    if rating[x] > rating[y] and rating[y] > rating[z]:
                        total += 1
                    if rating[x] < rating[y] and rating[y] < rating[z]:
                        total += 1
        return total
