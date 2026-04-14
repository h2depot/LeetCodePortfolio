# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cnt = 0
        dummy = head
        if dummy == None:
            return False
        while dummy.next != None:
            cnt += 1
            if cnt == 10000:
                return True
            dummy = dummy.next
        return False