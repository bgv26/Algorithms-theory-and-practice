def main():
    _ = int(input())
    stairs = [0] + list(map(int, input().split()))
    for i in range(2, len(stairs)):
        stairs[i] += max(stairs[i - 1], stairs[i - 2])
    return stairs[-1]


if __name__ == '__main__':
    print(main())
