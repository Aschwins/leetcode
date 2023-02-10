# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "<ListNode: {}>".format(self.val)

def create_linked_list(arr):
    head = ListNode()
    curr = head
    for i in range(len(arr)):
        curr.val = arr[i]
        if i != len(arr) - 1:
            curr.next = ListNode()
            curr = curr.next
    return head
