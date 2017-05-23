class Node:
    def __init__(self, char, key):
        self.val = char
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return self.val

    def __repr__(self):
        return "%s: %d" % (self.val, self.key)


def update_sum(node):
    sum_left = sum_right = 0
    if node is not None:
        if node.left is not None:
            sum_left = node.left.sum
        if node.right is not None:
            sum_right = node.right.sum
        node.sum = node.key + sum_left + sum_right


def set_parent(child, parent):
    if child is not None:
        child.parent = parent


def keep_parent(v):
    set_parent(v.left, v)
    set_parent(v.right, v)


def rotate(parent, child):
    grandparent = parent.parent
    if grandparent is not None:
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
    while v.parent is not None:
        parent = v.parent
        grandparent = parent.parent
        if grandparent is None:
            rotate(parent, v)
            # update_sum(parent)
            # update_sum(v)
            break
        else:
            zigzig = (grandparent.left == parent) == (parent.left == v)
        if zigzig:
            rotate(grandparent, parent)
            rotate(parent, v)
        else:
            rotate(parent, v)
            rotate(grandparent, v)
            # update_sum(grandparent)
            # update_sum(parent)
            # update_sum(v)
    return v


def find(v, key):
    if v is None:
        return None
    while v is not None:
        last = v
        if key < v.key and v.left is not None:
            v = v.left
        elif key > v.key and v.right is not None:
            v = v.right
        else:
            break
    return splay(last)


def split(root, key):
    if root is None:
        return None, None
    root = find(root, key)
    if root.key <= key:
        right, root.right = root.right, None
        set_parent(right, None)
        # update_sum(right)
        # update_sum(root)
        return root, right
    else:
        left, root.left = root.left, None
        set_parent(left, None)
        # update_sum(left)
        # update_sum(root)
        return left, root


def insert(root, char, key):
    left, right = split(root, key)
    root = Node(char, key)
    root.left, root.right = left, right
    keep_parent(root)
    # update_sum(root)
    return root


def merge(left, right):
    if right is None:
        return left
    if left is None:
        return right
    while left.right is not None:
        left = left.right
    splay(left)
    left.right = right
    set_parent(right, left)
    # update_sum(left)
    return left


def remove(root, key):
    root = find(root, key)
    if root and root.key == key:
        set_parent(root.left, None)
        set_parent(root.right, None)
        root = merge(root.left, root.right)
    return root


def reorder(root, start, end, where):
    left_left, right_left = split(root, start - 1)
    left_right, right_right = split(right_left, end)
    if left_right:
        tmp = merge(left_left, right_right)
        tmp_left, tmp_right = split(tmp, where - 1)
        res = merge(tmp_left, left_right)
        root = merge(res, tmp_right)
    return root


def run():
    root = None
    for char in input():
        root = insert(root, char, ord(char))
    number = int(input())
    for _ in range(number):
        start, end, where = map(int, input().split())
        reorder(root, start, end, where)

if __name__ == '__main__':
    run()
