# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        l1_ptr = l1
        l2_ptr = l2
        new_list = dummy_node
        while l1_ptr and l2_ptr:
            if l1_ptr.val < l2_ptr.val:
                new_list.next = l1_ptr
                l1_ptr = l1_ptr.next
            else:
                new_list.next = l2_ptr
                l2_ptr = l2_ptr.next
            new_list = new_list.next
        if l1_ptr:
            new_list.next = l1_ptr
        if l2_ptr:
            new_list.next = l2_ptr
        return dummy_node.next
      
      
#Test:
def create_nodelist_from_list(node_list) -> Optional[ListNode]:
    def rec(index: int) -> Optional[ListNode]:
        if index == len(node_list):
            return None
        node = ListNode(node_list[index])
        node.next = rec(index + 1)
        return node

    return rec(0)


def nodes_list_to_list(head: ListNode):
    output = []
    list_ptr = head
    while list_ptr:
        output.append(list_ptr.val)
        list_ptr = list_ptr.next
    return output


l11 = create_nodelist_from_list([1, 2, 4])
l22 = create_nodelist_from_list([1, 3, 4])
merged = merge_two_lists(l11, l22)
print(nodes_list_to_list(merged))
