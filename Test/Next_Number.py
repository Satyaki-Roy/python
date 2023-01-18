## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nextNumber(head):
    num_str = ""
    initial_len = 0
    curr = head
    while curr is not None:
        num_str += str(curr.data)
        initial_len += 1
        curr = curr.next

    num = int(num_str)
    new_num = str(num + 1)
    new_len = len(str(new_num))
    # print(num, initial_len, new_num, new_len)

    if new_len != initial_len:
        new_node = Node(1)
        new_node.next = head
        head = new_node

    curr = head
    i = 0
    while curr is not None:
        curr.data = new_num[i]
        i += 1
        curr = curr.next
    return head


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next
    return


# Main
# Read the link list elements including -1
arr = [int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)
