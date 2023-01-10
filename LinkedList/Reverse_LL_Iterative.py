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


# To print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


def length_of_ll(head):
    curr = head
    count = 0
    while curr is not None:
        count += 1
        curr = curr.next
    return count


def give_tail(head):
    previous = head
    curr = head.next
    while curr is not None:
        if curr.next is None:
            return previous, curr
        previous = curr
        curr = curr.next
    return head, None


# def reverse(head):
#     length = length_of_ll(head)
#     if length == 0 or length == 1:
#         return head
#     old_ll_tail, newHead = give_tail(head)
#     old_ll_tail.next = None
#     curr_of_reverse_ll = newHead
#     for i in range(length - 1):
#         previous_of_tail_in_old_ll, tail_of_old_ll = give_tail(head)
#         if tail_of_old_ll is None:
#             curr_of_reverse_ll.next = previous_of_tail_in_old_ll
#         else:
#             previous_of_tail_in_old_ll.next = None
#             curr_of_reverse_ll.next = tail_of_old_ll
#             curr_of_reverse_ll = tail_of_old_ll
#     return newHead


def reverse(head):
    length = length_of_ll(head)
    if length == 0 or length == 1:
        return head
    new_ll_tail = None
    curr_of_old_ll = head
    for i in range(length):
        next_of_curr_in_old_ll = curr_of_old_ll.next
        curr_of_old_ll.next = new_ll_tail
        new_ll_tail = curr_of_old_ll
        curr_of_old_ll = next_of_curr_in_old_ll
    return new_ll_tail


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()

    ans = reverse(head)
    printLinkedList(ans)

    t -= 1
