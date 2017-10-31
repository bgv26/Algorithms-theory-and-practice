import bisect
import time


def main():
    n = int(input())
    array = list(map(int, input().split()))
    array = array[::-1]
    inf = 10 ** 10
    d = [inf] * (n + 1)
    d[0] = -inf
    pos = [0] * (n + 1)
    prev = [0] * n
    for i in range(n):
        right = bisect.bisect_right(d, array[i])
        if d[right - 1] <= array[i] <= d[right]:
            d[right] = array[i]
            pos[right] = i
            prev[i] = pos[right - 1]
    d = [item for item in d if item not in (inf, -inf)]
    print(len(d))
    answer = [0] * len(d)
    p = pos[len(d)]
    for j in range(len(d)):
        answer[j] = n - p
        p = prev[p]
    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('--- {} seconds ----'.format(time.time() - start_time))
