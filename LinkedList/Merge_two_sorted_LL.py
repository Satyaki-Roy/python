from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeTwoSortedLinkedLists(h1, h2):
    if h1 is None and h2 is None:
        return None
    elif h1 is None:
        return h2
    elif h2 is None:
        return h1
    if h1.data <= h2.data:
        nh = h1
        h1 = h1.next
    else:
        nh = h2
        h2 = h2.next
    nt = nh
    while h1 is not None and h2 is not None:
        if h1.data <= h2.data:
            nt.next = h1
            nt = nt.next
            h1 = h1.next
        else:
            nt.next = h2
            nt = nt.next
            h2 = h2.next
    if h1 is not None:
        nt.next = h1
    if h2 is not None:
        nt.next = h2
    return nh


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1
