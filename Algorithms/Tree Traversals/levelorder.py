class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    ## Using BFS approach
    queue = [root]
    while queue:
        curr = queue.pop(0)
        print(curr.val, end=' ')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)

    levelOrder(root)