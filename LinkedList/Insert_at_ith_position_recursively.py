from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


def insert(head, i, data):
    if i < 0:
        return head
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    if head is None:
        return None
    smallHead = insert(head.next, i - 1, data)
    head.next = smallHead
    return head


# To print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head_ip = takeInput()
    i_ip = int(input())
    data_ip = int(input())
    new_head = insert(head_ip, i_ip, data_ip)
    printLinkedList(new_head)
    t -= 1
