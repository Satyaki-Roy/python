from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_ll(head):
    if head is None:
        return 0
    return 1 + length_ll(head.next)


def bubbleSort(head):
    nh = head
    length = length_ll(head)
    while length != 0:
        previous_previous = None
        previous = None
        curr = nh
        count = length

        while curr is not None and count != 0:
            if previous is not None:
                if previous.data <= curr.data:
                    pass
                else:
                    if count == length - 1:
                        nh = curr
                    after_curr = curr.next
                    if previous_previous is None:
                        pass
                    else:
                        previous_previous.next = curr
                    curr.next = previous
                    previous.next = after_curr

                    temp = curr
                    curr = previous
                    previous = temp
            previous_previous = previous
            previous = curr
            curr = curr.next
            count -= 1

        length -= 1
    return nh


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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
