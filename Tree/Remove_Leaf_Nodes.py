from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def remove_leaf_nodes(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = remove_leaf_nodes(root.left)
    root.right = remove_leaf_nodes(root.right)
    return root


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


def preOrder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)


# Main
root = takeInput()
remove_leaf_nodes(root)
preOrder(root)
