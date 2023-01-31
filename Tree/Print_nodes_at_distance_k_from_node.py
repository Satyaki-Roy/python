from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Count:
    def __init__(self):
        self.data = 0


class Found:
    def __init__(self):
        self.data = False


def nodesAtDistanceK(root, node, k, found=Found(), count=Count()):
    if root is None:
        return None

    if root.data == node:
        found.data = True

    if count.data == k:
        print(root.data)

    if not found.data:
        print('not found', root.data)
        print('count', count.data)
        nodesAtDistanceK(root.left, node, k, found, count)
        nodesAtDistanceK(root.right, node, k, found, count)
    else:
        print('found', root.data)
        print('count', count.data)
        count.data += 1
        nodesAtDistanceK(root.left, node, k, found, count)
        nodesAtDistanceK(root.right, node, k, found, count)
        if count.data == 0:
            pass
        count.data -= 1


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


def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left is not None:
                outputQ.put(curr.left)
            if curr.right is not None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k)
