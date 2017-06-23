class Node:
    """ Класс для представления узла дерева Хаффмана """
    def __init__(self, key, value=0):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.value.__eq__(other.value)

    def __lt__(self, other):
        if not isinstance(other, Node):
            return False
        return self.value.__lt__(other.value)

    def __repr__(self):
        return 'key: {}, value: {}, left: {}, right: {}'.format(self.key, self.value, self.left, self.right)


def build_tree(freq):
    """ Постоение двоичного дерева Хаффмана """
    from heapq import heappush, heappop
    heap = []
    for k, v in freq.items():
        heappush(heap, Node(k, v))
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        parent = Node(None, left.value + right.value)
        parent.left = left
        parent.right = right
        heappush(heap, parent)
    return heappop(heap)


def build_code_map(root):
    """ In-order обход дерева для построения кодов символов"""
    code_map = {}
    stack = []
    path = ''
    node = root
    while len(stack) or node:
        if node:
            stack.append((node, path))
            node = node.left
            path += '0'
        else:
            node, path = stack.pop()
            if node.key:
                code_map[node.key] = path or '0'
            node = node.right
            path += '1'
    return code_map


def run():
    freq = {}
    source = input()
    for c in source:
        freq[c] = freq.get(c, 0) + 1
    root = build_tree(freq)
    code_map = build_code_map(root)
    result = ''.join((code_map[c] for c in source))
    print(len(code_map), len(result))
    for c in sorted(code_map.keys()):
        print(c, code_map[c])
    print(result)


if __name__ == '__main__':
    run()
