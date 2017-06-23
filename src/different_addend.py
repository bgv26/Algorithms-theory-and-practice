def run():
    number = int(input())
    addends = []
    total = 0

    for i in range(1, number + 1):
        if total + 2 * i >= number:
            addends.append(number - total)
            break
        addends.append(i)
        total += i

    print(len(addends))
    print(' '.join(map(str, addends)))


if __name__ == '__main__':
    run()
