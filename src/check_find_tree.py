class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is not None:
            return self.key == other.key
        return False

    def __ne__(self, other):
        if other is not None:
            return self.key != other.key
        return False

    def __lt__(self, other):
        if other is not None:
            return self.key < other.key
        return False

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return self.key


class BinTree:
    def __init__(self, ):
        self.tree = []
        self.path = []

    def append(self, node):
        self.tree.append(node)

    def build_tree(self):
        for node in self.tree:
            left = node.left
            node.left = None if left == -1 else self.tree[left]
            right = node.right
            node.right = None if right == -1 else self.tree[right]

    def check_correct(self):

        if len(self.tree) == 0 or self.is_correct(self.tree[0]):
            print('CORRECT')
        else:
            print('INCORRECT')

    def is_correct(self, root):
        stack = []
        node = root
        prev = None
        while len(stack) or (node is not None):
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node < prev or node == node.left:
                    return False
                prev = node
                node = node.right
        return True

    def in_order_iterative(self, root):
        stack = []
        node = root
        while len(stack) or (node is not None):
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                self.path.append(node)
                node = node.right

    def pre_order_iterative(self, root):
        stack = [root]
        while len(stack):
            node = stack.pop()
            self.path.append(node)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def walk(self):
        root = self.tree[0]
        self.in_order_iterative(root)
        print(' '.join(map(str, self.path)))
        self.path = []
        self.pre_order_iterative(root)
        print(' '.join(map(str, self.path)))
        self.path = []
        self.post_order(root)
        print(' '.join(map(str, self.path)))
        self.path = []

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            self.path.append(node)


def run():
    number = int(input())
    tree = BinTree()
    for _ in range(number):
        key, left, right = map(int, input().split())
        tree.append(Node(key, left, right))
    tree.build_tree()
    # tree.walk()
    tree.check_correct()


if __name__ == '__main__':
    run()
