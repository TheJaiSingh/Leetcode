# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        current=head
        answer=0
        while current is not None:
            answer=answer*2+current.val
            current=current.next
        return answer

        