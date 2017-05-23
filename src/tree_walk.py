class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)


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

    def walk(self):
        root = self.tree[0]
        self.in_order(root)
        print(' '.join(map(str, self.path)))
        self.path = []
        self.pre_order_iterative(root)
        print(' '.join(map(str, self.path)))
        self.path = []
        self.post_order(root)
        print(' '.join(map(str, self.path)))
        self.path = []

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            self.path.append(node)
            self.in_order(node.right)

    def pre_order(self, node):
        if node is not None:
            self.path.append(node)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def pre_order_iterative(self, root):
        stack = [root]
        while len(stack):
            node = stack.pop()
            self.path.append(node)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

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
    tree.walk()


if __name__ == '__main__':
    run()
