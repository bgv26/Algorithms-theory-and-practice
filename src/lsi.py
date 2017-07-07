def longest_subseq():
    # Прочитаем исходные данные из консоли
    n = int(input())
    x = [int(i) for i in input().split(' ')]
    P = [0]*n
    M = [0]*(n + 1)
    L = 0
    x = x[::-1]
    for i in range(n):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if x[M[mid]] < x[i]:
                lo = mid + 1
            elif x[M[mid]] == x[i]:
                lo += 1
            else:
                hi = mid - 1
        newL = lo
        P[i] = M[newL - 1]
        if newL > L:
            M[newL] = i
            L = newL
        elif x[i] < x[M[newL]]:
            M[newL] = i

    # Восстановим решение по рассчитанным данным
    re = [0]*L
    k = M[L]
    for i in range(L-1, -1, -1):
        re[i] = n - k
        k = P[k]
    print(len(re))
    print(' '.join(map(str,re[::-1])))

if __name__ == "__main__":
    longest_subseq()