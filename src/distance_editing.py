def edit_distance(str_a, str_b):
    n = len(str_a) + 1
    m = len(str_b) + 1
    d = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        d[i][0] = i
    for j in range(m):
        d[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            diff = 0 if str_a[i - 1] == str_b[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + diff)
    return d[n - 1][m - 1]


def main():
    str_a = input()
    str_b = input()
    print(edit_distance(str_a, str_b))


if __name__ == '__main__':
    main()
