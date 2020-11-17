class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        outputList = []
        seenSet = set()
        for x in arr2:
            for y in arr1:
                if y == x:
                    if y not in seenSet:
                        seenSet.add(y)
                    outputList.append(y)
        secondOutput = []
        for z in arr1:
            if z not in seenSet:
                secondOutput.append(z)
        secondOutput.sort()
        for w in secondOutput:
            outputList.append(w)
        return outputList
