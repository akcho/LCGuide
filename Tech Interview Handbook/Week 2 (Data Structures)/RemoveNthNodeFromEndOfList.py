# Two Pointers
# time: O(L)
# space: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        '''
        Here, we separate first and second pointers by exactly n nodes. 
        By doing this, we know that the second pointer is n nodes away 
        from the end when the first pointer reaches the end of the LL.       
        '''

        # move first pointer n nodes ahead of second pointer
        for i in range(n + 1):
            first = first.next

        # 1. Move first pointer to the end of the LL.
        # 2. Increment second pointer at the same time (it's always n nodes away).
        while first:
            first = first.next
            second = second.next

        # Cut off the node that's n nodes away from the end of the LL.
        second.next = second.next.next
        return dummy.next