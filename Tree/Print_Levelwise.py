from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_without_space(data):
    print(data, end="")


def printLevelWise(root):
    if root is None:
        return None

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        take_out_element_from_queue = q.get()
        print_without_space(take_out_element_from_queue.data)
        print_without_space(':')
        print_without_space('L:')

        if take_out_element_from_queue.left is not None:
            left = take_out_element_from_queue.left
            q.put(left)
            print_without_space(left.data)
        else:
            print_without_space('-1')

        print_without_space(',R:')

        if take_out_element_from_queue.right is not None:
            right = take_out_element_from_queue.right
            q.put(right)
            print_without_space(right.data)
        else:
            print_without_space('-1')

        print()


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main
root = takeInput()
printLevelWise(root)