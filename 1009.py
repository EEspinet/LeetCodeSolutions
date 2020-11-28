class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binaryRaw = str(bin(N))
        
        binaryRaw = binaryRaw[2:]
        # print(binaryRaw)
        output = ""
        for x in binaryRaw:
            if x == "0":
                output += "1"
            else:
                output += "0"
        # print(output)
        return int(output,2)
