from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteAlternateNodes(head):
    i = 1
    previous = None
    curr = head
    while curr.next is not None:
        if i % 2 != 0 or i == 1:
            previous = curr
            curr = curr.next
        else:
            previous.next = curr.next
            previous = curr.next
            curr = curr.next
        i += 1

    if i % 2 == 0:
        previous.next = None

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
head = takeInput()
printLinkedList(deleteAlternateNodes(head))
