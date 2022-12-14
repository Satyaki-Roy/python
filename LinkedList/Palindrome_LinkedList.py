from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def generate_forward_string(head):
    if head.next is None:
        return str(head.data)
    return str(head.data) + ' ' + generate_forward_string(head.next)


def generate_reverse_string(head):
    if head.next is None:
        return str(head.data)
    return generate_reverse_string(head.next) + ' ' + str(head.data)


def lengthRecursive(head):
    if head is None:
        return 0
    return 1 + lengthRecursive(head.next)


def isPalindrome(head):
    if lengthRecursive(head) < 1:
        return True
    forward = generate_forward_string(head)
    reverse = generate_reverse_string(head)
    # print(forward)
    # print(reverse)
    return forward == reverse


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

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1
