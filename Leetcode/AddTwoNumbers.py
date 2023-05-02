# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        nodo = ListNode(None, None)
        guardado = 0
        ahora = nodo
        while l1 or l2 or guardado !=0:
            valor_l1 = l1.val if l1 else 0
            valor_l2 = l2.val if l2 else 0
            actual = valor_l1+valor_l2+guardado
            guardado = actual//10
            ahora.next = ListNode(actual%10,None)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            ahora = ahora.next
        return nodo.next