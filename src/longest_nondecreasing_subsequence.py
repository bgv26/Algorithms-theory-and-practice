def naive():
    n = int(input())
    array = list(map(int, input().split()))
    d = [1] * n
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if array[j] >= array[i]:
                d[i] = max(d[i], d[j] + 1)
                prev[i] = j
    ans = max(d)
    l = []
    k = ans
    for i in range(n, 0, -1):
        if d[i - 1] == k:
            l.append(i)
            k -= 1
        if k < 1:
            break

    print(ans)
    print(' '.join(map(str, l[::-1])))


def main():
    n = int(input())
    array = list(map(int, input().split()))
    array = array[::-1]
    inf = 10 ** 10
    d = [inf] * (n + 1)
    d[0] = -inf
    prev = [None] * n
    up = 0
    for i in range(n):
        left = 1
        right = up
        while left <= right:
            middle = (left + right) // 2
            if d[middle] < array[i]:
                left = middle + 1
            elif d[middle] == array[i]:
                left += 1
            else:
                right = middle - 1
        d[left] = array[i]
        prev[left] = n - i
        if left > up:
            up = left
    d = [item for item in d if item not in (inf, -inf)]
    prev = [item for item in prev if item]
    print(len(d))
    print(' '.join(map(str, reversed(prev))))


if __name__ == '__main__':
    # naive()
    main()
