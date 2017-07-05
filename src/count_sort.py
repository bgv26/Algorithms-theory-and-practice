def count_sort(arr):
    result = [0] * len(arr)
    counts = [0] * 10
    for item in arr:
        counts[item - 1] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    for j in range(len(arr) - 1, -1, -1):
        result[counts[arr[j - 1] - 1] - 1] = arr[j - 1]
        counts[arr[j - 1] - 1] -= 1

    return result


def main():
    _ = int(input())
    array = list(map(int, input().split()))
    print(' '.join(map(str, count_sort(array))))


if __name__ == '__main__':
    main()
