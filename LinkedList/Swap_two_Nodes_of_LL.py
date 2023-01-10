from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swapNodes(head, i, j):
    nh = head
    count = 0
    pih, ih, pjh, jh = None, None, None, None
    previous = None
    curr = head

    while curr.next is not None:
        if count == i:
            pih = previous
            ih = curr
        if count == j:
            pjh = previous
            jh = curr
        count += 1
        previous = curr
        curr = curr.next

    if jh is None:
        pjh = previous
        jh = curr
        count += 1

    aih = ih.next
    ajh = jh.next if jh is not None else None

    if i == j - 1:
        if i == 0:
            jh.next = ih
            ih.next = ajh
            nh = jh
        else:
            pih.next = jh
            jh.next = ih
            ih.next = ajh
    else:
        if i == 0:
            jh.next = aih
            pjh.next = ih
            ih.next = ajh
            nh = jh
        else:
            pih.next = jh
            jh.next = aih
            pjh.next = ih
            ih.next = ajh

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


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
