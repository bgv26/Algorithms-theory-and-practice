class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.sum = key

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return self.key


def key_func(x, last_sum):
    return (x + last_sum) % 1000000001


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
    if grandparent:
        if grandparent.left == parent:
            grandparent.left = child
        else:
            grandparent.right = child

    if parent.left == child:
        parent.left, child.right = child.right, parent
    else:
        parent.right, child.left = child.left, parent
    update_sum(parent)
    update_sum(child)
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
        update_sum(root)
        return root, right
    else:
        left, root.left = root.left, None
        set_parent(left, None)
        update_sum(root)
        return left, root


def insert(root, key):
    left, right = split(root, key)
    root = Node(key)
    root.left, root.right = left, right
    keep_parent(root)
    update_sum(root)
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
    left.right = right
    set_parent(right, left)
    update_sum(left)
    return left


def remove(root, key):
    root = find(root, key)
    set_parent(root.left, None)
    set_parent(root.right, None)
    root = merge(root.left, root.right)
    return root


def sum_of_seg(root, l, r):
    left_left, right_left = split(root, l - 1)
    left_right, right_right = split(right_left, r)
    res = 0
    if left_right:
        res = left_right.sum
    return res, merge(left_left, merge(left_right, right_right))


def run():
    number = int(input())
    last_sum = 0
    root = None
    cache = set()
    for _ in range(number):
        parts = input().split()
        if parts[0] == '+':
            val = key_func(int(parts[1]), last_sum)
            if val not in cache:
                cache.add(val)
                root = insert(root, val)
        elif parts[0] == '-':
            val = key_func(int(parts[1]), last_sum)
            if val in cache:
                cache.remove(val)
                root = remove(root, val)
        elif parts[0] == '?':
            val = key_func(int(parts[1]), last_sum)
            root = find(root, val)
            if root and root.key == val:
                print('Found')
            else:
                print('Not found')
        elif parts[0] == 's':
            left = key_func(int(parts[1]), last_sum)
            right = key_func(int(parts[2]), last_sum)
            last_sum, root = sum_of_seg(root, left, right)
            print(last_sum)


if __name__ == '__main__':
    run()
