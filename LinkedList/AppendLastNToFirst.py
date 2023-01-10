from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthRecursive(head):
    if head is None:
        return 0
    return 1 + lengthRecursive(head.next)


def tail_pointer(head):
    if head is None:
        return None
    if head.next is None:
        return head
    return tail_pointer(head.next)


def appendLastNToFirst(head, n):
    size = lengthRecursive(head)
    if size == 0 or size == 1:
        return head
    actual_n = n % size
    if actual_n == 0:
        return head
    break_point = size - actual_n
    tail_node = tail_pointer(head)
    curr = head
    # print(size, actual_n, break_point, tail_node.data, curr.data)
    while break_point > 1:
        curr = curr.next
        break_point -= 1
    new_head = curr.next
    curr.next = None
    tail_node.next = head
    return new_head


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


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head_inp = takeInput()
    n_inp = int(stdin.readline().rstrip())

    head_new_new = appendLastNToFirst(head_inp, n_inp)
    printLinkedList(head_new_new)

    t -= 1
