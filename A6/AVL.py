class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class BST:
    def __init__(self):
        self.root = None

    def tree_search(self, word):
        return self._tree_search(self.root, word)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _tree_search(self, node, word):
        if node is None:
            return False
        if word < node.key:
            return self._tree_search(node.left, word)
        elif word > node.key:
            return self._tree_search(node.right, word)
        else:
            return True  # Return True if the word is found

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def tree_insert(self, word):
        self.root = self._tree_insert(self.root, word)

    def _tree_insert(self, node, word):
        if not node:
            return TreeNode(word)

        if word < node.key:
            node.left = self._tree_insert(node.left, word)
        elif word > node.key:
            node.right = self._tree_insert(node.right, word)
        else:
            return node  # Ignore duplicate insertion

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and word < node.left.key:
            return self.right_rotate(node)

        if balance < -1 and word > node.right.key:
            return self.left_rotate(node)

        if balance > 1 and word > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and word < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def tree_delete(self, word):
        self.root = self._tree_delete(self.root, word)

    def _tree_delete(self, node, word):
        if node is None:
            return node

        if word < node.key:
            node.left = self._tree_delete(node.left, word)
        elif word > node.key:
            node.right = self._tree_delete(node.right, word)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.right = self._tree_delete(node.right, min_larger_node.key)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def tree_walk(self):
        self._tree_walk(self.root)

    def _tree_walk(self, node):
        if node is not None:
            self._tree_walk(node.left)
            balance_factor = self.get_balance(node)  # Calculate balance factor
            print(f"{node.key} (Balance Factor: {balance_factor})")
            self._tree_walk(node.right)

    def tree_print(self, node=None, indent="", last=True):
        if node is None:
            node = self.root

        if node is None:
            print("The tree is empty.")
            return

        print(indent, end='')
        if last:
            print("R----", end='')
            indent += "     "
        else:
            print("L----", end='')
            indent += "|    "

        balance_factor = self.get_balance(node)  # Calculate balance factor
        print(f"{node.key} (Balance Factor: {balance_factor})")

        if node.left:
            self.tree_print(node.left, indent, False)
        if node.right:
            self.tree_print(node.right, indent, True)


if __name__ == "__main__":
    bst = BST()
    dictionary = ["apple", "banana", "abdominal", "car", "bag", "house"]
    for word in dictionary:
        bst.tree_insert(word)

    while True:
        print("\nChoose an operation: ")
        print("1. Tree-Search")
        print("2. Tree-Insert")
        print("3. Tree-Delete")
        print("4. Tree-Walk (In-order Traversal)")
        print("5. Tree-Print (Tree Structure)")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_word = input("Enter word to search: ")
            found = bst.tree_search(search_word)
            if found:
                print(f"'{search_word}' found in the tree.")
            else:
                print(f"'{search_word}' not found in the tree.")

        elif choice == "2":
            insert_word = input("Enter word to insert: ")
            bst.tree_insert(insert_word)
            print(f"'{insert_word}' inserted.")

        elif choice == "3":
            delete_word = input("Enter word to delete: ")
            bst.tree_delete(delete_word)
            print(f"'{delete_word}' deleted.")

        elif choice == "4":
            print("Tree-Walk:")
            bst.tree_walk()

        elif choice == "5":
            print("Tree-Print (Tree Structure):")
            bst.tree_print()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
