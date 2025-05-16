class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST, ignoring duplicates."""
        if not self.root:
            self.root = Node(value)
            return True
        
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                    return True
                current = current.left
            elif value > current.value:
                if not current.right:
                    current.right = Node(value)
                    return True
                current = current.right
            else:
                return False  # Duplicate value, ignored

    def delete(self, value):
        """Delete a value from the BST, return True if deleted, False if not found."""
        def find_min(node, parent):
            """Helper to find the inorder successor (smallest in right subtree)."""
            while node.left:
                parent = node
                node = node.left
            return node, parent

        # Empty tree
        if not self.root:
            return False

        # Special case: root with no children
        if self.root.value == value and not self.root.left and not self.root.right:
            self.root = None
            return True

        # Find node and its parent
        parent, current = None, self.root
        while current and current.value != value:
            parent = current
            current = current.left if value < current.value else current.right

        if not current:
            return False  # Value not found

        # Case 1: Leaf node
        if not current.left and not current.right:
            if current == self.root:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node with one child
        elif not current.left or not current.right:
            child = current.left or current.right
            if current == self.root:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

        # Case 3: Node with two children
        else:
            successor, succ_parent = find_min(current.right, current)
            current.value = successor.value
            if succ_parent.left == successor:
                succ_parent.left = successor.right
            else:
                succ_parent.right = successor.right

        return True

    # Iterative Traversals to avoid recursion limit
    def inorder(self):
        """Iterative inorder traversal."""
        if not self.root:
            return
        stack, current = [], self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right

    def preorder(self):
        """Iterative preorder traversal."""
        if not self.root:
            return
        stack = [self.root]
        while stack:
            current = stack.pop()
            print(current.value, end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postorder(self):
        """Iterative postorder traversal using two stacks."""
        if not self.root:
            return
        stack1, stack2 = [self.root], []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            print(stack2.pop().value, end=" ")

def main():
    bst = BinarySearchTree()
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert a value")
        print("2. Delete a value")
        print("3. Inorder Traversal")
        print("4. Preorder Traversal")
        print("5. Postorder Traversal")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                value = int(input("Enter value to insert: "))
                if bst.insert(value):
                    print(f"Inserted {value} successfully.")
                else:
                    print(f"Value {value} already exists, ignored.")
            elif choice == 2:
                value = int(input("Enter value to delete: "))
                if bst.delete(value):
                    print(f"Deleted {value} successfully.")
                else:
                    print(f"Value {value} not found.")
            elif choice == 3:
                print("Inorder (sorted):", end=" ")
                bst.inorder()
                print()
            elif choice == 4:
                print("Preorder:", end=" ")
                bst.preorder()
                print()
            elif choice == 5:
                print("Postorder:", end=" ")
                bst.postorder()
                print()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1-6.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()