import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        dateVar = date.split('-')
        
        x = datetime.datetime(int(dateVar[0]),int(dateVar[1]),int(dateVar[2]))
        return int(x.strftime("%j"))
