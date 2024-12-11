class TreeNode:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Tree-Search: Search for a word in the tree and return its count.
    def tree_search(self, word):
        return self._tree_search(self.root, word)

    def _tree_search(self, node, word):
        if node is None:
            return 0
        if word < node.key:
            return self._tree_search(node.left, word)
        elif word > node.key:
            return self._tree_search(node.right, word)
        else:
            return node.count

    # Tree-Insert: Insert a word into the tree and return the count before insertion.
    def tree_insert(self, word):
        count_before = self.tree_search(word)
        self.root = self._tree_insert(self.root, word)
        return count_before

    def _tree_insert(self, node, word):
        if node is None:
            return TreeNode(word)
        if word < node.key:
            node.left = self._tree_insert(node.left, word)
        elif word > node.key:
            node.right = self._tree_insert(node.right, word)
        else:
            node.count += 1
        return node

    # Tree-Delete: Delete an occurrence of a word in the tree and return the count before deletion.
    def tree_delete(self, word):
        count_before = self.tree_search(word)
        if count_before > 0:
            self.root = self._tree_delete(self.root, word)
        return count_before

    def _tree_delete(self, node, word):
        if node is None:
            return None
        if word < node.key:
            node.left = self._tree_delete(node.left, word)
        elif word > node.key:
            node.right = self._tree_delete(node.right, word)
        else:
            if node.count > 1:
                node.count -= 1
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                min_larger_node = self._find_min(node.right)
                node.key = min_larger_node.key
                node.count = min_larger_node.count
                min_larger_node.count = 1
                node.right = self._tree_delete(node.right, min_larger_node.key)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Tree-Walk: Inorder traversal of the tree, prints words and their counts.
    def tree_walk(self):
        self._tree_walk(self.root)

    def _tree_walk(self, node):
        if node is not None:
            self._tree_walk(node.left)
            print(f"{node.key}({node.count})")
            self._tree_walk(node.right)

    # Tree-Print: Display the current content of the tree with proper formatting.
    def tree_print(self, node=None, indent="", last=True):
        # Set the starting node to root if no node is provided
        if node is None:
            node = self.root

        # Base case: If the tree is empty
        if node is None:
            print("The tree is empty.")
            return

        # Print the current node with formatting
        print(indent, end='')
        if last:
            print("R----", end='')  # Marks this node as the right child
            indent += "     "       # Increase indentation for the next level
        else:
            print("L----", end='')  # Marks this node as the left child
            indent += "|    "       # Increase indentation with a separator for the next level
        print(f"{node.key}({node.count})")

        # Recursively print the left and right subtrees
        if node.left:
            self.tree_print(node.left, indent, False)
        if node.right:
            self.tree_print(node.right, indent, True)


# Main program with a simple user interface
if __name__ == "__main__":
    bst = BST()

    # Insert some base dictionary words into the tree
    # dictionary = ["apple", "banana", "abdominal", "car", "bag", "house"]
    # for word in dictionary:
    #    bst.tree_insert(word)

    while True:
        print("\nChoose an operation: ")
        print("1. Tree-Search")
        print("2. Tree-Insert")
        print("3. Tree-Delete")
        print("4. Tree-Walk")
        print("5. Tree-Print")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_word = input("Enter word to search: ")
            count = bst.tree_search(search_word)
            print(f"Occurrences of {search_word}: {count}")

        elif choice == "2":
            insert_word = input("Enter word to insert: ")
            before_insert = bst.tree_insert(insert_word)
            print(
                f"Occurrences of {insert_word} before insertion: {before_insert}")

        elif choice == "3":
            delete_word = input("Enter word to delete: ")
            before_delete = bst.tree_delete(delete_word)
            print(
                f"Occurrences of {delete_word} before deletion: {before_delete}")

        elif choice == "4":
            print("Tree-Walk:")
            bst.tree_walk()

        elif choice == "5":
            print("Tree-Print:")
            bst.tree_print()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
