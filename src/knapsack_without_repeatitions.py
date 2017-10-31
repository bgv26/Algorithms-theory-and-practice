def main():
    capacity, n = map(int, input().split())
    weights = list(map(int, input().split()))
    d = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            d[i][w] = d[i - 1][w]
            if weights[i - 1] <= w:
                d[i][w] = max(d[i][w], d[i - 1][w - weights[i - 1]] + weights[i - 1])
    return d[n][capacity]


if __name__ == '__main__':
    print(main())
