class Tree:
    def __init__(self, value=0, left=None, right=None):
        self.value = None
        self.left = left
        self.right = right
    
    def insert(self, root, key):
        if root is None:
            return Tree(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root
    
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

