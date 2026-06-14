# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_kth_node(self, node:ListNode, k:int)->ListNode:
        for _ in range(k):
            node=node.next if node else None
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        grp_prev= dummy

        while True:
            kth = self.get_kth_node(grp_prev,k)
            if not kth:
                break
            grp_next = kth.next

            prev, curr = kth.next, grp_prev.next
            while curr!=grp_next:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            tmp = grp_prev.next
            grp_prev.next = kth
            grp_prev = tmp

        return dummy.next