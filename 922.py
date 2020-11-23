class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        evenArr = []
        oddArr = []
        
        for digits in A:
            if digits % 2 == 0:
                evenArr.append(digits)
            else:
                oddArr.append(digits)
        # print(evenArr)
        # print(oddArr)
        output = []
        evenCount = 0
        oddCount = 0
        for evens in evenArr:
            output.insert(evenCount * 2,evens)
            evenCount+=1
        for odds in oddArr:
            output.insert(oddCount * 2 + 1, odds)
            oddCount+=1
        return output
