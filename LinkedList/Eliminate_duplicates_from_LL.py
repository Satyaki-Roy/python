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


def removeDuplicates(head):
    length = lengthRecursive(head)
    if length < 2:
        return head
    previous = head
    curr = previous.next
    while curr is not None:
        if previous.data == curr.data:
            previous.next = curr.next
        else:
            previous = curr
        curr = curr.next
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


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    head_ip = takeInput()

    head_ip = removeDuplicates(head_ip)
    printLinkedList(head_ip)

    t -= 1
