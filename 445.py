# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        done = False
        # print(l1)
        # print(l1.val)
        # print(l1.next.val)
        tempNum1 = l1
        while not done:
            # print(tempNum1)
            num1 += str(tempNum1.val)
            if tempNum1.next == None:
                done = True
            else:
                tempNum1 = tempNum1.next
        done = False
        tempNum1 = l2
        while not done:
            # print(tempNum1)
            num2 += str(tempNum1.val)
            if tempNum1.next == None:
                done = True
            else:
                tempNum1 = tempNum1.next
        # print(num1)
        # print(num2)
        outputVar = int(num1) + int(num2)
        outputVar = str(outputVar)
        print(outputVar)
        oldNode = ""
        nodeList = []
        for x in outputVar:
            newNode = ListNode(x,None)
            nodeList.append(newNode)
        for x in range(0,len(nodeList)-1):
            nodeList[x].next = nodeList[x+1]
        return nodeList[0]
