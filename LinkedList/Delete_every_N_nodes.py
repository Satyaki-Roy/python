from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_of_ll(head):
    if head is None:
        return 0
    return 1 + length_of_ll(head.next)


def skipMdeleteN(head, M, N):
    if head is None:
        return head
    if M == 0:
        return None
    if N == 0:
        return head
    curr = head
    m_tail = None
    count = 1
    while curr.next is not None:
        if count % (M + N) == 0:
            m_tail.next = curr.next
            m_tail = None
            count = 0
        elif count % M == 0 and m_tail is None:
            m_tail = curr
        count += 1
        curr = curr.next
    if m_tail is not None:
        m_tail.next = None
    return head


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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1
