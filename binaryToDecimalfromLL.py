class ListNode(object):
    pass


def getDecimalValue(head: ListNode) -> int:
    b_list = []
    while head:
        b_list.append(head.val)
        head = head.next
    dec, i = 0, 0
    for j in b_list[::-1]:
        dec += j << i
        i += 1
    return dec