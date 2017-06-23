from collections import namedtuple

Item = namedtuple('Item', 'cost size')


def run():
    number_of_items, capacity = map(int, input().split())
    items = [Item(*map(int, input().split())) for _ in range(number_of_items)]
    items.sort(key=lambda i: i.cost / i.size, reverse=True)
    max_cost = 0
    for item in items:
        if item.size <= capacity:
            max_cost += item.cost
            capacity -= item.size
        else:
            max_cost += (item.cost / item.size) * capacity
            break
    print('{:.3f}'.format(max_cost))


if __name__ == '__main__':
    run()
