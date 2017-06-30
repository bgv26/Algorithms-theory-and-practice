def merge(array1, array2, count):
    result = []
    left, right = 0, 0
    while left < len(array1) and right < len(array2):
        first = array1[left]
        second = array2[right]
        if first <= second:
            result.append(first)
            left += 1
        else:
            count += len(array1) - left
            result.append(second)
            right += 1
    if left == len(array1):
        result.extend(array2[right:])
    else:
        result.extend(array1[left:])
    return count, result


def merge_sort(array_list, count):
    if len(array_list) > 1:
        middle = len(array_list) // 2
        count, left_half = merge_sort(array_list[:middle], count)
        count, right_half = merge_sort(array_list[middle:], count)
        count, array_list = merge(left_half, right_half, count)
    return count, array_list


def main():
    _ = int(input())
    array = list(map(int, input().split()))
    count, _ = merge_sort(array, 0)
    print(count)


if __name__ == '__main__':
    main()
