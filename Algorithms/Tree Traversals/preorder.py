class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    ## Root - Left - Right
    if root == None:
        return
    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)
    

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)

    preorder(root)