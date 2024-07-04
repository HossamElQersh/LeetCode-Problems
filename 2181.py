# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = pointer2 = head.next
        sum = 0
        while pointer2:
            if pointer2.val != 0 or sum == 0:
                sum += pointer2.val
            else:
                pointer1.next = pointer2
                pointer2.val = sum
                sum = 0
                pointer1 = pointer1.next
            pointer2 = pointer2.next
        return head.next.next


# Input: head = [0,3,1,0,4,5,2,0]
if __name__ == '__main__':
    obj = Solution()
    nodehead = ListNode
    nodehead.next = ListNode(0)
    nodehead.next.next = ListNode(3)
    nodehead.next.next.next = ListNode(0)
    # nodehead.next.next.next.next = ListNode(0)
    # nodehead.next.next.next.next.next = ListNode(4)
    # nodehead.next.next.next.next.next.next = ListNode(5)
    # nodehead.next.next.next.next.next.next.next = ListNode(2)
    # nodehead.next.next.next.next.next.next.next.next = ListNode(0)
    res = obj.mergeNodes(nodehead)
    while res:
        print(res.val)
        res = res.next