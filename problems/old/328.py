# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):

        if(not head):return None

        evenHead = head.next

        odd = head
        even = head.next

        node =  even.next if even else None
        evenOdd = 1
        while(node):
            temp = node.next

            if(evenOdd):
                odd.next =node
                odd = node
            else:
                even.next = node
                even = node
            
            node = temp
            evenOdd = 1 - evenOdd
        if(not evenOdd):
            even.next = None
        odd.next = evenHead
        return head



s = Solution()



 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
values =  [2,1,3,5,6,4,7]
# values = [1,2,3,4,5]
head = ListNode(values[0])

node = head
for i in range(1,len(values)):
    newNode = ListNode(values[i])
    node.next = newNode
    node = newNode

print(s.oddEvenList(head))
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
# print(s.oddEvenList([2,1,3,5,6,4,7]))