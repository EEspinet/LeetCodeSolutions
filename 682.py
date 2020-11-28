class Solution:
    def calPoints(self, ops: List[str]) -> int:
        output = []
        print(ops)
        for x in range(0,len(ops)):
            print(output)
            if 'C' in ops[x]:
                output.pop()
            elif 'D' in ops[x]:
                output.append(output[-1] * 2)
            elif '+' in ops[x]:
                output.append(output[-1] + output[-2])
            else:
                output.append(int(ops[x]))
        totalSum = 0
        # print(output)
        for y in output:
            totalSum += int(y)
        return totalSum
