class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    ## Left - root - right
    if root == None:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)
    

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)

    inorder(root)