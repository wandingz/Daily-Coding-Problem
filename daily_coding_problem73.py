'''
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseLinkedList(self, head):
        pre = None
        # 1 -> 2 -> 3 -> 4 -> 5
        # None <- 1 <- 2 <- 3 <- 4 <- 5
        while head:
            head.next, head, pre = pre, head.next, head
        return pre

def string2LinkedList(inputt):
    if not inputt:
        return

    nums = [int(x.strip()) for x in inputt.split(',')]
    dummy = head = ListNode(0)
    for x in nums:
        head.next = ListNode(x)
        head = head.next
    return dummy.next

def linkedList2String(node):
    if not node:
        return ''

    res = ''
    while node:
        res += str(node.val) + ', '
        node = node.next
    return res.strip(', ')


head = string2LinkedList('1,2,3,4,5')
res = Solution().reverseLinkedList(head)
linkedList2String(res)
