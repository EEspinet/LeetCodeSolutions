class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        output = 0
        count = 0
        while len(sandwiches) > 0:
            if count == len(sandwiches):
                output = len(sandwiches)
                break
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                tempVar = students.pop(0)
                students.append(tempVar)
                count += 1
        return output
