from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def evenAfterOdd(head):
    if head is None or head.next is None:
        return head
    nh = None
    previous = None
    curr = head
    after = head.next
    coh = None
    count = 0
    while curr is not None and curr.next is not None:
        if curr.data % 2 != 0:
            if count == 0:
                if coh is None:
                    coh = curr
                    nh = curr
                else:
                    coh = curr
            else:
                if coh is None:
                    nh = curr
                    coh = curr
                    previous.next = after
                    curr.next = None
                    curr.next = head
                    curr = previous
                else:
                    previous.next = after
                    curr.next = None
                    acoh = coh.next
                    coh.next = curr
                    curr.next = acoh
                    coh = curr
                    curr = previous
        elif curr.data % 2 == 0:
            count += 1
        previous = curr
        curr = curr.next
        after = curr.next
    # print(previous.data, curr.data, after)
    if nh is None:
        if curr.data % 2 != 0:
            previous.next = None
            curr.next = head
            return curr
        return head
    if count != 0 and curr.data % 2 != 0:
        previous.next = after
        curr.next = None
        acoh = coh.next
        coh.next = curr
        curr.next = acoh
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


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    newHead = evenAfterOdd(head)
    # evenAfterOdd(head)
    printLinkedList(newHead)

    t -= 1
