# AVL tree implementation in Python

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class Data(object):
    def __init__(self, term, sentence, score):
        self.term = term
        self.sentence = sentence
        self.score = score

    def __str__(self):
        return f"{self.term}: {self.sentence} ({self.score:.2f})"

    def __eq__(self, other):
        return self.term == other.term

    def __lt__(self, other):
        return self.term < other.term

    def __le__(self, other):
        return self.term <= other.term

    def __gt__(self, other):
        return self.term > other.term

    def __ge__(self, other):
        return self.term >= other.term


class AVLTree(object):

    def __init__(self):
        self.count_insert = 0
        self.count_search = 0

    # Utility function to search a key in a BST
    def search(self, root, key):
        # Base Cases: root is null or key is present at root
        self.count_search += 1
        if root is None or root.key == key:
            return root

        # Key is greater than root's key
        self.count_search += 1
        if root.key < key:
            return self.search(root.right, key)

        # Key is smaller than root's key
        return self.search(root.left, key)

    # Function to insert a node
    def insert_node(self, root, key):
        # Find the correct location and insert the node
        self.count_insert += 1
        if not root:
            return TreeNode(key)
        elif key < root.key:
            self.count_insert += 1
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        # self.count_insert += 1
        if balanceFactor > 1:
            # self.count_insert += 1
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        # self.count_insert += 1
        if balanceFactor < -1:
            # self.count_insert += 1
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

        # Function to delete a node

    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        # self.count_insert += 1
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        # self.count_insert += 1
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.left) + 1 + self.size(node.right)

    def get_insert_count(self):
        count = self.count_insert
        self.count_insert = 0
        return count

    def get_search_count(self):
        count = self.count_search
        self.count_search = 0
        return count

    def clear_count(self):
        self.count_insert = 0
        self.count_search = 0

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

"""

    

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


"""
