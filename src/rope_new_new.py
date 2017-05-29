class Node:
    def __init__(self, char=None):
        self.val = char
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


def set_parent(child, parent):
    if child is not None:
        child.parent = parent


def keep_parent(v):
    set_parent(v.left, v)
    set_parent(v.right, v)


def rotate(parent, child):
    grandparent = parent.parent
    if grandparent:
        if grandparent.left == parent:
            grandparent.left = child
        else:
            grandparent.right = child

    if parent.left == child:
        parent.left, child.right = child.right, parent
    else:
        parent.right, child.left = child.left, parent
    update_weight(parent)
    update_weight(child)
    keep_parent(child)
    keep_parent(parent)
    child.parent = grandparent


def splay(v):
    while v.parent:
        parent = v.parent
        grandparent = parent.parent
        if grandparent is None:
            rotate(parent, v)
            break
        else:
            if (grandparent.left == parent) and (parent.left == v) \
                    or (grandparent.right == parent) and (parent.right == v):
                rotate(grandparent, parent)
                rotate(parent, v)
            else:
                rotate(parent, v)
                rotate(grandparent, v)
    return v


def find(v, key):
    while v:
        if key < v.weight and v.left:
            v = v.left
        elif key > v.weight and v.right:
            v = v.right
        else:
            return splay(v)
    return v


def simplify(node):
    if node.left and node.left.weight == node.weight:
        node = node.left
        set_parent(node, None)
    if node.right and node.right.weight == node.weight:
        node = node.right
        set_parent(node, None)
    return node


def split(root, key):
    if root is None:
        return None, None
    root = find(root, key)
    if root.weight <= key:
        val = root.val[:key - root.weight]
        tree1 = Node()
        tree1.right = Node(val)
        tree1.right.weight = len(val)
        tree1.left = root.left
        val = root.val[key - root.weight:]
        tree2 = Node()
        tree2.left = Node(val)
        tree2.left.weight = len(val)
        tree2.right = root.right
        keep_parent(tree1)
        keep_parent(tree2)
        update_weight(tree1)
        update_weight(tree2)
        tree1 = simplify(tree1)
        tree2 = simplify(tree2)
        return tree1, tree2
    else:
        val = root.val[:key]
        tree1 = Node()
        tree1.right = Node(val)
        tree1.right.weight = len(val)
        tree1.left = root.left
        val = root.val[key:]
        tree2 = Node()
        tree2.left = Node(val)
        tree2.left.weight = len(val)
        tree2.right = root.right
        keep_parent(tree1)
        keep_parent(tree2)
        update_weight(tree1)
        update_weight(tree2)
        tree1 = simplify(tree1)
        tree2 = simplify(tree2)
        return tree1, tree2


def insert(root, key, adding_node):
    left, right = split(root, key)
    return merge(merge(left, adding_node), right)


def get_max(root):
    while root.right:
        root = root.right
    return root


def merge(left, right):
    res = Node()
    res.left, res.right = left, right
    keep_parent(res)
    update_weight(res)
    res = simplify(res)
    return res
    # if right is None:
    #     return left
    # if left is None:
    #     return right
    # left = get_max(left)
    # splay(left)
    # left.right = right
    # set_parent(right, left)
    # update_weight(left)
    # return left


def remove(node, start, end):
    tree1, tree2 = split(node, start)
    substring, tree3 = split(tree2, end - start + 1)
    return merge(tree1, tree3), substring


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


def reorder(root, start, end, where):
    rest, substring = remove(root, start, end)
    return insert(rest, where, substring)


def run():
    root = Node(input())
    root.weight = len(root.val)
    print(root)
    number = int(input())
    for _ in range(number):
        start, end, where = map(int, input().split())
        root = reorder(root, start, end, where)
        print(''.join(map(str, in_order_iterative(root))))
    print(''.join(map(str, in_order_iterative(root))))


if __name__ == '__main__':
    run()
