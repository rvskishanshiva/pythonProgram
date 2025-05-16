class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left==None:
                    current.left = new_node
                    break
                current = current.left
            elif value > current.value:
                if current.right==None:
                    current.right = new_node
                    break
                current = current.right
            else:
                break 

   
    def delete(self, value):
        if not self.root:
            return
        
        if self.root.value == value and self.root.left==None and self.root.right==None:
            self.root = None
            return

        parent = None
        current = self.root
        
        # Find the node to delete and its parent
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        
        if not current:  # Value not found
            return

        # Case 1: Leaf node
        if not current.left and not current.right:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        
        # Case 2: Node with one child
        elif not current.left or not current.right:
            child = current.left if current.left else current.right
            if current != self.root:
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
        
        # Case 3: Node with two children
        else:
            # Find inorder successor (smallest in right subtree)
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            current.value = successor.value
            # Delete the successor (it has at most one right child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    # Traversals (unchanged)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

# Main function to demonstrate the BST
def main():
    bst = BinarySearchTree()
    
    # Insert some values
    values = [5, 3, 7, 1, 4, 6, 8]
    print("Inserting values:", values)
    for value in values:
        bst.insert(value)
    
    # Demonstrate traversals
    print("\nInitial BST Traversals:")
    print("Inorder (sorted):", end=' ')
    bst.inorder(bst.root)
    print("\nPreorder:", end=' ')
    bst.preorder(bst.root)
    print("\nPostorder:", end=' ')
    bst.postorder(bst.root)

    # Delete a value
    delete_value = 3
    print(f"\n\nDeleting value: {delete_value}")
    bst.delete(delete_value)

    # Show traversals after deletion
    print("BST Traversals after deletion:")
    print("Inorder (sorted):", end=' ')
    bst.inorder(bst.root)
    print("\nPreorder:", end=' ')
    bst.preorder(bst.root)
    print("\nPostorder:", end=' ')
    bst.postorder(bst.root)

if __name__ == "__main__":
    main()