class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #Var used to check if it just worked on a '0' var
        justDone = False
        
        # Iterate through the list through its indexes
        for x in range(len(arr)):
            # If the value is 0, proceed
            if arr[x] == 0:
                # If the previous iteration was a 0, that means this is result of that process, skip this.
                if justDone:
                    # Reset the justDone flag
                    justDone = False
                # Proceed as this is a real '0' to dup
                else:
                    # Change flag to True
                    justDone = True
                    # Iterate from last position to current x position backwards by 1
                    for y in range(len(arr) - 1,x,-1):
                        # Replace the value of the index by the previous index
                        # print(y)
                        arr[y] = arr[y-1]
                        # print(arr)
        # print(arr)
