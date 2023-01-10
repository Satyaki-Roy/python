from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthOfLL(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count


def insertAtIthNode(head, i, data):
    newNode = Node(data)

    if i < 0:
        print('negative position not allowed')
        return head

    if i == 0:
        newNode.next = head
        head = newNode
        return head

    prevNode = head
    currentNode = head.next
    count = 1

    while currentNode is not None:
        if i == count:
            prevNode.next = newNode
            newNode.next = currentNode
            return head
        count += 1
        prevNode = currentNode
        currentNode = currentNode.next

    if count == i:
        prevNode.next = newNode
        return head

    print('i is greater than the length of LL')
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
t = int(stdin.readline().rstrip())

while t > 0:
    head_ip = takeInput()
    i_ip = int(stdin.readline().rstrip())
    data_ip = int(input())
    new_head = insertAtIthNode(head_ip, i_ip, data_ip)
    printLinkedList(new_head)
    t -= 1
