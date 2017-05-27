class Node:
    def __init__(self, key, char):
        self.key = key
        self.val = char
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return self.val

    def __repr__(self):
        return "%d: %s" % (self.key, self.val)


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
        if key < v.key and v.left:
            v = v.left
        elif key > v.key and v.right:
            v = v.right
        else:
            return splay(v)
    return v


def split(root, key):
    if root is None:
        return None, None
    root = find(root, key)
    if root.key <= key:
        right, root.right = root.right, None
        set_parent(right, None)
        return root, right
    else:
        left, root.left = root.left, None
        set_parent(left, None)
        return left, root


def insert(root, key, char):
    left, right = split(root, key)
    root = Node(key, char)
    root.left, root.right = left, right
    keep_parent(root)
    return root


def get_min(root):
    while root.left:
        root = root.left
    return root


def get_max(root):
    while root.right:
        root = root.right
    return root


def merge(left, right):
    if right is None:
        return left
    if left is None:
        return right
    left = get_max(left)
    splay(left)
    right = get_min(right)
    splay(right)
    if left.key <= right.key:
        left.right = right
        set_parent(right, left)
        return left
    else:
        right.left = left
        set_parent(left, right)
        return right


def remove(root, key):
    root = find(root, key)
    set_parent(root.left, None)
    set_parent(root.right, None)
    root = merge(root.left, root.right)
    return root


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
            path.append(node)
            node = node.right
    return path


def reorder(root, start, end, where):
    left_left, right = split(root, start - 1)
    sub, right_right = split(right, end)
    if where == 0:
        return merge(sub, merge(left_left, right_right))
    else:
        if where > start:
            where += end - start
        left, right = split(merge(left_left, right_right), where)
        return merge(left, merge(sub, right))


def renumber(root):
    for i, node in enumerate(in_order_iterative(root)):
        node.key = i
    return root


def run():
    root = None
    for i, char in enumerate(input()):
        root = insert(root, i, char)
    print(''.join(map(str, in_order_iterative(root))))
    number = int(input())
    for _ in range(number):
        start, end, where = map(int, input().split())
        root = reorder(root, start, end, where)
        root = renumber(root)
        print(''.join(map(str, in_order_iterative(root))))
    print(''.join(map(str, in_order_iterative(root))))


if __name__ == '__main__':
    run()
