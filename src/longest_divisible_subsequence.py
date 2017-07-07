def main():
    n = int(input())
    array = list(map(int, input().split()))
    d = [1] * n
    for i in range(n):
        for j in range(i):
            if not array[i] % array[j]:
                d[i] = max(d[i], d[j] + 1)
    print(max(d))


if __name__ == '__main__':
    main()
