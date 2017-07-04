import bisect


def quick_sort(arr):
    from random import choice
    if len(arr) < 2:
        return arr
    else:
        less = []
        more = []
        pivot = choice(arr)
        for i in arr:
            if i < pivot:
                less.append(i)
            if i > pivot:
                more.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + [pivot] * arr.count(pivot) + more


def main():
    n, m = map(int, input().split())
    starts, ends = map(list, zip(*[map(int, input().split()) for _ in range(n)]))
    starts = quick_sort(starts)
    ends = quick_sort(ends)
    points = list(map(int, input().split()))
    result = []
    for point in points:
        result.append(bisect.bisect_right(starts, point) - bisect.bisect_left(ends, point))

    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
