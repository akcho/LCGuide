# let's just stick to hash map, bc two pointers seems too specific
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
