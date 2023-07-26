
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversed1 = []
        while l1.next != None:
            reversed1.insert(0, l1.val)
            l1 = l1.next
        number1 = "".join(str(x) for x in reversed1)
        number1 = int(number1)

        reversed2 = []
        while l2.next != None:
            reversed2.insert(0, l2.val)
            l2 = l2.next
        number2 = "".join(str(x) for x in reversed2)
        number2 = int(number2)

        sum = number1 + number2
        sumString = str(sum)

        res = []
        for char in sumString:
            res.insert(0, int(char))
        return res
        