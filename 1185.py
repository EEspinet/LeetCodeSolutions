class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        lookupDate = datetime.datetime(year,month,day)
        return str(lookupDate.strftime("%A"))
