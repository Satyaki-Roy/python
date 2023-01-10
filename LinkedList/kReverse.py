from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLL(head):
    if head is None:
        return head
    if head.next is None:
        return head
    tail = head.next
    smallHead = reverseLL(head.next)
    tail.next = head
    head.next = None
    return smallHead


def tail_of_ll(head):
    if head.next is None:
        return head
    return tail_of_ll(head.next)


def length_ll(head):
    if head is None:
        return 0
    return 1 + length_ll(head.next)


def kReverse(head, k):
    if head is None or head.next is None:
        return head
    if k == 0:
        return head

    nh = None

    length_of_LL = length_ll(head)
    count_1 = length_of_LL // k
    count_2 = 0

    previous = None
    curr = head
    reverse_tail = None
    reverse_head = head
    while count_1 > 0:
        while curr is not None:
            if count_2 == k:
                break
            count_2 += 1
            previous = curr
            curr = curr.next
        not_changeable_head = curr
        changeable_tail = previous
        changeable_tail.next = None

        head_of_reversed_ll = reverseLL(reverse_head)

        if reverse_tail is not None:
            reverse_tail.next = head_of_reversed_ll

        tail_of_reversed_ll = tail_of_ll(head_of_reversed_ll)

        tail_of_reversed_ll.next = not_changeable_head

        if nh is None:
            nh = head_of_reversed_ll

        curr = not_changeable_head
        reverse_head = curr
        reverse_tail = tail_of_reversed_ll
        count_2 = 0
        count_1 -= 1

    head_of_reversed_ll = reverseLL(reverse_head)
    reverse_tail.next = head_of_reversed_ll

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
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1
