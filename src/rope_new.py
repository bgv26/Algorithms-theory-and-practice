class Node:
    def __init__(self, string=None):
        self.val = string
        self.left = None
        self.right = None
        self.parent = None
        self.weight = None

    def __str__(self):
        return self.val

    def __repr__(self):
        return "%s: %d" % (self.val, self.weight)


def update_weight(node):
    weight_left = weight_right = 0
    if node:
        if node.left:
            weight_left = node.left.weight
        if node.right:
            weight_right = node.right.weight
        node.weight = weight_left + weight_right


def split(node, i):
    # while node.left and node.weight >= i:
    #     node = node.left
    # tree1, tree2 = Node(), Node()
    # if node.left and node.left.weight >= i:
    #     val = node.left.val[:i]
    #     tree1.val = val
    #     tree1.weight = len(val)
    #     val = node.left.val[i:]
    #     tree2.left = Node(val)
    #     tree2.left.weight = len(val)
    #     tree2.right = node.right
    #     update_weight(tree2)
    # elif node.right and node.left.weight < i:
    #     index = i-node.left.weight
    #     val = node.right.val[:index]
    #     tree1.left = node.left
    #     tree1.right = Node(val)
    #     tree1.right.weight = len(val)
    #     val = node.right.val[index:]
    #     tree2.left = Node(val)
    #     tree2.left.weight = len(val)
    #     tree2.right = node.right
    #     update_weight(tree1)
    #     update_weight(tree2)
    # else:
    #     val = node.val[:i]
    #     tree1 = Node(val)
    #     tree1.weight = len(val)
    #     val = node.val[i:]
    #     tree2 = Node(val)
    #     tree2.weight = len(val)
    # return tree1, tree2
    while node.left:
        if node.left.weight >= i:
            tree2 = Node()
            tree1, tree2.left = split(node.left, i)
            tree2.right = node.right
            tree2.weight = tree2.left.weight + tree2.right.weight
        else:
            tree1 = Node()
            tree1.left = node.left
            tree1.right, tree2 = split(node.right, i - node.left.weight)
            tree1.weight = tree1.left.weight + tree1.right.weight
    if node.left:
        if node.left.weight >= i:
            tree2 = Node()
            tree1, tree2.left = split(node.left, i)
            tree2.right = node.right
            tree2.weight = tree2.left.weight + tree2.right.weight
        else:
            tree1 = Node()
            tree1.left = node.left
            tree1.right, tree2 = split(node.right, i - node.left.weight)
            tree1.weight = tree1.left.weight + tree1.right.weight
    else:
        val = node.val[:i]
        tree1 = Node(val)
        tree1.weight = len(val)
        val = node.val[i:]
        tree2 = Node(val)
        tree2.weight = len(val)
    return tree1, tree2


def merge(tree1, tree2):
    res = Node()
    res.left, res.right = tree1, tree2
    update_weight(res)
    return res


def delete(node, start, end):
    tree1, tree2 = split(node, start)
    substring, tree3 = split(tree2, end - start + 1)
    return merge(tree1, tree3), substring


def insert(node, where, add_node):
    tree1, tree2 = split(node, where)
    return merge(merge(tree1, add_node), tree2)


def in_order_iterative(root):
    stack = []
    path = []
    node = root
    while len(stack) or (node is not None):
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.val:
                path.append(node)
            node = node.right
    return path


def run():
    root = Node(input())
    root.weight = len(root.val)
    # print(root)
    number = int(input())
    for _ in range(number):
        start, end, where = map(int, input().split())
        rest, substring = delete(root, start, end)
        root = insert(rest, where, substring)
        # print(''.join(map(str, in_order_iterative(root))))
    print(''.join(map(str, in_order_iterative(root))))


if __name__ == '__main__':
    run()
