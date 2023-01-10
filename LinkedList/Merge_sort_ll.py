from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_of_LL(head):
    if head is None:
        return 0
    return 1 + length_of_LL(head.next)


def midPoint(head):
    if head is None:
        return head
    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


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


def mergeSort(head):
    if head is None or head.next is None:
        return head

    mid_node_of_ll = midPoint(head)

    head1 = head
    head2 = mid_node_of_ll.next

    mid_node_of_ll.next = None

    head1 = mergeSort(head1)
    head2 = mergeSort(head2)

    return mergeTwoSortedLinkedLists(head1, head2)


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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
