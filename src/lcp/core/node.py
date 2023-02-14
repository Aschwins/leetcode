from typing import Iterable, Any

class Node:
    """
    Definition for a Tree Node.
    """
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return "<Node: {}>".format(self.val)

class ListNode:
    """
    Definition for a List Noce.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "<ListNode: {}>".format(self.val)


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "<TreeNode: {}>".format(self.val)


def create_linked_list(arr: Iterable[Any]) -> ListNode:
    """Util function to create a linked list from an array.

    Args:
        arr (Iterable[Any]): Iterable of values to be used as values for the nodes

    Returns:
        ListNode: Head of the linked list
    """
    head = ListNode()
    curr = head
    for i in range(len(arr)):
        curr.val = arr[i]
        if i != len(arr) - 1:
            curr.next = ListNode()
            curr = curr.next
    return head
