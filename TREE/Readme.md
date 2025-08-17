### TREE Data Structure

- Tree is a Data Structure has the balanced and unbalanced trees
- When we Called the Balanced and Unbalanced tree? think once 🤔
- if the difference between left height of the tree and right side of the tree is less than or equal to 1 then it is called as balanced tree else unbalanced
- if tree is balanced the height of the tree is logN base 2 
#### Why do we need binary tree
- To lookup faster
- Huffman trees compression of data
- Routing trees for the `Network Traffic`

** Different types of the Traversal IMPORTANT **
- DFS(Depth First Search)
    - PreOrder
    - InOrder
    - PostOrder
- BFS
    - Level order traversal

** Preorder Traversal **
- Root -> Left -> right

```
            A
        /       \
       B          c
    A -> B -> c
```

```
def preorder(root):
    if not root: return
    print(root.value)
    preorder(root.left)
    preorder(root.right)
```

** Inorder Traversal **
- Left -> Root -> Right
```
        A
       / \
      B   c
      B -> A -> c
```

```
def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
```


** Postorder Traversal **
- Left -> Right -> Root
```
        A
       / \
      B   c
    B -> c -> A
```

```
def postorder(root):
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.value)
```
