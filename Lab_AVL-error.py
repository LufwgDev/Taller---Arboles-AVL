import sys 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def display_tree(node, level=0):
    if not node:
        return
    display_tree(node.right, level + 1)

    print('    ' * level + str(node.value))

    display_tree(node.left, level + 1)

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)

        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node) 
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node) 
        elif balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node) 
        
        return node 
    
    def delete(self, value):
        """Elimina un valor del árbol y rebalancea."""
        self.root = self._delete_recursive(self.root, value)
    def _delete_recursive(self, node, value):

        if not node:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:

            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            succ = node.right
            while succ.left:
                succ = succ.left
            node.value = succ.value
            node.right = self._delete_recursive(node.right, succ.value)


        updateHeight(node)
        balance = getBalance(node)
        if balance > 1 and getBalance(node.left) >= 0:
            node = rotate_right(node)
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            node = rotate_right(node)
        elif balance < -1 and getBalance(node.right) <= 0:
            node = rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            node = rotate_left(node)
        return node

    def inorder(self):
        """Retorna lista de valores en recorrido in-order."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if not node:
            return
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    
avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")

avl = AVLTree()
for v in [10,20,30,40,50,25]:
    avl.insert(v)

print("In-order tras inserciones:", avl.inorder())
print("\nÁrbol tras inserciones:")
display_tree(avl.root)

avl.delete(20)
avl.delete(30)

print("\nIn-order tras eliminaciones:", avl.inorder())
print("\nÁrbol tras eliminaciones:")
display_tree(avl.root)
