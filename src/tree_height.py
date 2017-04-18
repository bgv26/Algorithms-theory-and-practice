def get_height(tree, index, cache):
    height = 1
    parent = tree[index]
    while parent != -1:
        parent = tree[parent]
        height += 1
        if cache[parent]:
            height += cache[parent]
            break
    cache[index] = height
    return height


def run():
    nodes_count = int(input())
    nodes = list(map(int,input().split()))
    heights = [None] * range(nodes_count)
    return max((get_height(nodes, index, heights) for index in range(nodes_count)))


if __name__ == '__main__':
    print(run())
