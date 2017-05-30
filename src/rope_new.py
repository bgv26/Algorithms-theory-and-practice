class Node:
    def __init__(self, string=None):
        self._val = string
        self.left = None
        self.right = None
        self.parent = None
        self.weight = 0

    def is_leaf(self):
        if self.left:
            return False
        if self.right:
            return False
        return True

    def __str__(self):
        return self.val

    @property
    def val(self):
        return self.val

    @val.getter
    def val(self):
        left_val, right_val = '', ''
        if self.left:
            left_val = self.left.val or left_val
        if self.right:
            right_val = self.right.val or right_val
        return self._val or left_val + right_val

    @val.setter
    def val(self, value):
        self._val = value


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


def update_weight(node):
    weight_left = weight_right = 0
    if node:
        if node.left:
            weight_left = node.left.weight
        if node.right:
            weight_right = node.right.weight
        node.weight = weight_left + weight_right


def find(node, i):
    while not node.is_leaf():
        if node.left.weight >= i:
            node = node.left
        else:
            i -= node.left.weight
            node = node.right
    return splay(node)


def split(node, i):
    if i == 0:
        tree1 = Node()
        tree2 = node
        return tree1, tree2
    if i == node.weight:
        tree1 = node
        tree2 = Node()
        return tree1, tree2
    node = find(node, i)
    if node.is_leaf():
        val = node.val[:i]
        tree1 = Node(val)
        tree1.weight = len(val)
        val = node.val[i:]
        tree2 = Node(val)
        tree2.weight = len(val)
    else:
        i -= node.left.weight

        val = node.val[:i]
        if node.left.is_leaf():
            tree1 = Node()
            tree1.left = node.left
            tree1.right = Node(val)
            tree1.right.weight = len(tree1.right.val)
            keep_parent(tree1)
            update_weight(tree1)
        else:
            tree1 = Node(val)
            tree1.weight = len(tree1.val)

        val = node.val[i:]
        if node.right.is_leaf():
            tree2 = Node()
            tree2.left = Node(val)
            tree2.left.weight = len(tree2.left.val)
            tree2.right = node.right
            keep_parent(tree2)
            update_weight(tree2)
        else:
            tree2 = Node(val)
            tree2.weight = len(tree2.val)

    # if node.left:
    #     if node.left.weight >= i:
    #         tree2 = Node()
    #         tree1, tree2.left = split(node.left, i)
    #         tree2.right = node.right
    #         update_weight(tree2)
    #     else:
    #         tree1 = Node()
    #         tree1.left = node.left
    #         tree1.right, tree2 = split(node.right, i - node.left.weight)
    #         update_weight(tree1)
    # else:
    #     val = node.val[:i]
    #     tree1 = Node(val)
    #     tree1.weight = len(val)
    #     val = node.val[i:]
    #     tree2 = Node(val)
    #     tree2.weight = len(val)
    return tree1, tree2


def merge(tree1, tree2):
    if not tree1.val:
        return tree2
    if not tree2.val:
        return tree1
    res = Node()
    res.left, res.right = tree1, tree2
    keep_parent(res)
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
    while len(stack) or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.is_leaf():
                path.append(node)
            node = node.right
    return path


def run():
    root = Node(input())
    root.weight = len(root.val)
    number = int(input())
    for _ in range(number):
        start, end, where = map(int, input().split())
        rest, substring = delete(root, start, end)
        root = insert(rest, where, substring)
    print(''.join(map(str, in_order_iterative(root))))


if __name__ == '__main__':
    run()
