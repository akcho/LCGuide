# hash map
# time: O(n)
# space: O(n)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_record = set()

        while head:
            if head in node_record:
                return True
            node_record.add(head)
            head = head.next
        return False

# Floyd's Cycle Finding Algorithm (adding here bc it's a cool solution, but I'd probably go with the first)
# time: O(n)
# space: O(1)
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True