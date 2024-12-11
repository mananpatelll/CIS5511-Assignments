class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf  # True if leaf node, else False
        self.keys = []  # Store keys in node
        self.children = []  # References to children

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            # Insert new key into the node if it is a leaf
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            # Move to child node if it is not a leaf
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(y.t, y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    def display(self, level=0):
        print("Level", level, ":", self.keys)
        for child in self.children:
            child.display(level + 1)

    def delete(self, key):
        idx = self.find_key(key)
        if idx < len(self.keys) and self.keys[idx] == key:
            if self.leaf:
                self.keys.pop(idx)
            else:
                self.delete_internal_node(key, idx)
        elif not self.leaf:
            flag = idx == len(self.keys)
            if len(self.children[idx].keys) < self.t:
                self.fill(idx)
            if flag and idx > len(self.keys):
                self.children[idx - 1].delete(key)
            else:
                self.children[idx].delete(key)

    def find_key(self, key):
        idx = 0
        while idx < len(self.keys) and self.keys[idx] < key:
            idx += 1
        return idx

    def delete_internal_node(self, key, idx):
        if len(self.children[idx].keys) >= self.t:
            pred_key = self.get_pred(idx)
            self.keys[idx] = pred_key
            self.children[idx].delete(pred_key)
        elif len(self.children[idx + 1].keys) >= self.t:
            succ_key = self.get_succ(idx)
            self.keys[idx] = succ_key
            self.children[idx + 1].delete(succ_key)
        else:
            self.merge(idx)
            self.children[idx].delete(key)

    def get_pred(self, idx):
        cur = self.children[idx]
        while not cur.leaf:
            cur = cur.children[len(cur.keys)]
        return cur.keys[-1]

    def get_succ(self, idx):
        cur = self.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def fill(self, idx):
        if idx != 0 and len(self.children[idx - 1].keys) >= self.t:
            self.borrow_from_prev(idx)
        elif idx != len(self.keys) and len(self.children[idx + 1].keys) >= self.t:
            self.borrow_from_next(idx)
        else:
            if idx != len(self.keys):
                self.merge(idx)
            else:
                self.merge(idx - 1)

    def borrow_from_prev(self, idx):
        child = self.children[idx]
        sibling = self.children[idx - 1]
        child.keys.insert(0, self.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        self.keys[idx - 1] = sibling.keys.pop()

    def borrow_from_next(self, idx):
        child = self.children[idx]
        sibling = self.children[idx + 1]
        child.keys.append(self.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        self.keys[idx] = sibling.keys.pop(0)

    def merge(self, idx):
        child = self.children[idx]
        sibling = self.children[idx + 1]
        child.keys.append(self.keys.pop(idx))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        self.children.pop(idx + 1)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, key):
        if len(self.root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.append(self.root)
            new_root.split_child(0)
            self.root = new_root
        self.root.insert_non_full(key)

    def delete(self, key):
        if self.root:
            self.root.delete(key)
            if len(self.root.keys) == 0:
                if len(self.root.children) > 0:
                    self.root = self.root.children[0]
                else:
                    self.root = None

    def display(self):
        if self.root:
            self.root.display()


# Testing for m = 4
print("B-Tree with m = 4")
btree_m4 = BTree(4)
for i in range(1, 21):
    btree_m4.insert(i)
btree_m4.display()

for i in range(2, 21, 2):
    btree_m4.delete(i)
print("\nB-Tree with m = 4 after deleting even numbers:")
btree_m4.display()

# Testing for m = 5
print("\nB-Tree with m = 5")
btree_m5 = BTree(5)
for i in range(1, 21):
    btree_m5.insert(i)
btree_m5.display()

for i in range(2, 21, 2):
    btree_m5.delete(i)
print("\nB-Tree with m = 5 after deleting even numbers:")
btree_m5.display()
