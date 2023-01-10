from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def give_tail(head):
    curr = head
    while curr is not None:
        if curr.next is None:
            return curr
        curr = curr.next


def reverseLinkedListRec(head):
    if head is None:
        return head
    if head.next is None:
        return head
    tail = head.next
    smallHead = reverseLinkedListRec(head.next)
    # tail = give_tail(smallHead)
    tail.next = head
    head.next = None
    return smallHead


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


# def kReverse_1(head, k):
#     if head is None or head.next is None:
#         return head
#     if k == 0:
#         return head
#     count = 0
#     previous = None
#     curr = head
#     while curr is not None:
#         if count == k:
#             break
#         count += 1
#         previous = curr
#         curr = curr.next
#
#     not_changeable_head = curr
#     changeable_tail = previous
#     changeable_tail.next = None
#
#     head_of_reversed_ll = reverseLL(head)
#
#     tail_of_reversed_ll = tail_of_ll(head_of_reversed_ll)
#
#     tail_of_reversed_ll.next = not_changeable_head
#
#     return head_of_reversed_ll


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()

    newHead = reverseLinkedListRec(head)
    printLinkedList(newHead)

    t -= 1
