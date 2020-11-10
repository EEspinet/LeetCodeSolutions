class Solution:
    def countBits(self, num: int) -> List[int]:
        
        output = []
        for x in range(num + 1):
            count = 0
            # print(x)
            # Decimal to binary number conversion
            binnum = [int(i) for i in list('{0:0b}'.format(x))]
            # print(binnum)
            for y in binnum:
                if y == 1:
                    count+=1
            output.append(count)
        
        return output
