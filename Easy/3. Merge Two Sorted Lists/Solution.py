# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Linked lists store two things: Value and the pointer to next location
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      #Let's create a dummy linked list to return the newly combined result
      dummy = ListNode()
      tail = dummy # This points to the tail of our dummy linked list

      while list1 and list2:
        if list1.val < list2.val:
          #Here we're not assiging it to list.val because dummy should point to next node and
          #not just store it's value (That's the idea of linked list- It has both val and next pointer)
          tail.next = list1
          list1 = list1.next
        else:
          tail.next = list2
          list2 = list2.next
        tail = tail.next

      if list1:
        tail.next = list1
      elif list2:
        tail.next = list2

      return dummy.next
      #We are returning dummy and not tail because it points to the head of the Linked list(first node)
        
