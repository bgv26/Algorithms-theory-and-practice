def merge(result, array1, array2):
    left, right, master, count = 0, 0, 0, 0
    while left < len(array1) and right < len(array2):
        first = array1[left]
        second = array2[right]
        if first <= second:
            result[master] = first
            left += 1
        else:
            count += len(array1) - left
            result[master] = second
            right += 1
        master += 1
    while left < len(array1):
        result[master] = array1[left]
        left += 1
        master += 1
    while right < len(array2):
        result[master] = array2[right]
        right += 1
        master += 1
    return count


def merge_sort(array_list):
    if len(array_list) > 1:
        middle = len(array_list) // 2
        left_half = array_list[:middle]
        right_half = array_list[middle:]
        count = merge_sort(left_half)
        count += merge_sort(right_half)
        count += merge(array_list, left_half, right_half)
        return count
    return 0


def main():
    _ = int(input())
    array = list(map(int, input().split()))
    count = merge_sort(array)
    print(count)


if __name__ == '__main__':
    main()
