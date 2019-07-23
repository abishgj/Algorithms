class Node:

    def __init__(self, key, left_child=None, right_child=None):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def _in_order_traversal(self, node):
        if node.left_child is not None:
            self._in_order_traversal(node=node.left_child)
        print(node.key, end=" ")
        if node.right_child is not None:
            self._in_order_traversal(node=node.right_child)

    def _pre_order_traversal(self, node):
        print(node.key, end=" ")
        if node.left_child is not None:
            self._pre_order_traversal(node=node.left_child)
        if node.right_child is not None:
            self._pre_order_traversal(node=node.right_child)

    def _post_order_traversal(self, node):
        if node.left_child is not None:
            self._post_order_traversal(node=node.left_child)
        if node.right_child is not None:
            self._post_order_traversal(node=node.right_child)
        print(node.key, end=" ")

    def _insert_as_child_to_node(self, node: Node, key):
        if key < node.key:
            if node.left_child is None:
                node.left_child = Node(key=key)
                return
            else:
                return self._insert_as_child_to_node(node.left_child, key)
        elif key > node.key:
            if node.right_child is None:
                node.right_child = Node(key=key)
                return
            else:
                return self._insert_as_child_to_node(node.right_child, key)

    def insert(self, key):
        self._insert_as_child_to_node(node=self.root, key=key)

    @staticmethod
    def get_in_order_successor(node):
        while node.left_child is not None:
            node = node.left_child
        key = node.data
        del node
        return key

    def find_and_delete_node(self, node, key):
        if node is None:
            return
        if node.data == key:
            if node.right is not None:
                new_key = BinarySearchTree.get_in_order_successor(node=node.right)
                node.data = new_key
            else:
                node = node.left_child
            print("Item {} deleted".format(key))
        elif key < node.data:
            return self.find_and_delete_node(node.left_child, key)
        else:
            return self.find_and_delete_node(node.right_child, key)

    def delete(self, key):
        self.find_and_delete_node(node=self.root, key=key)

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            if key < node.key:
                node = node.left_child
            else:
                node = node.right_child
        return False


if __name__ == '__main__':
    bst = BinarySearchTree(root=Node(key=50))
