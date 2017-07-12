def main():
    n = int(input())

    """ Заполняем массив со значениями минимального количества операций """
    d = [0] * (n + 1)
    for i in range(2, n + 1):
        d[i] = d[i - 1]
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2])
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3])
        d[i] += 1
    print(d[n])

    """ Восстанавливаем последовательность промежуточных чисел """
    i = n
    ans = [i]
    while i > 1:
        if d[i] == d[i - 1] + 1:
            ans.append(i - 1)
            i -= 1
            continue
        if i % 2 == 0 and d[i] == d[i // 2] + 1:
            ans.append(i // 2)
            i //= 2
            continue
        if i % 3 == 0 and d[i] == d[i // 3] + 1:
            ans.append(i // 3)
            i //= 3
            continue
    print(' '.join(map(str, reversed(ans))))


if __name__ == '__main__':
    main()
