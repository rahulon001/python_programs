'''
reverse linked list
'''

def reverse(head):
    current = head
    previous = None
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
    return previous

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverseLinkedlist(head):
    p1,p2 = None, head
    while p2 is not None:
        p3 = p2.nextnode
        p2.nextnode = p1
        p1 = p2
        p2 = p3
    return p1

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


# create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# set order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverseLinkedlist(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
