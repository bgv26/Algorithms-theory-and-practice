def binary_search(array, right_border, seek):
    left, right = 0, right_border
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == seek:
            return middle + 1
        elif array[middle] > seek:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def main():
    n, *data = map(int, input().split())
    _, *seeks = map(int, input().split())
    for seek in seeks:
        print(binary_search(data, n - 1, seek), end=' ')


if __name__ == '__main__':
    main()
