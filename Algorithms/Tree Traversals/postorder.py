class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(root):
    ## Left-Right-Root
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end =' ')
    

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)

    postorder(root)