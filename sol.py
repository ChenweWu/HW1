

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        CS197 HW1 Q2.
        LC https://leetcode.com/problems/merge-k-sorted-lists/solution/

        brute force iteration
        """
        all_list_val = []
        head = results = ListNode(0)
        for i in range(len(lists)):
            while lists[i] is not None:
                all_list_val.append(lists[i].val)
                lists[i] = lists[i].next
        
        for val in sorted(all_list_val):
            results.next = ListNode(val)
            results = results.next
        return head.next
