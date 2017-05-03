def run():
    p = 1000000007
    x = 263

    def get_hash(string):
        result = 0
        for index in range(len(string)):
            result = (result * x + ord(string[index])) % p
        return result % p

    pattern = input()
    text = input()
    m = len(pattern)
    n = len(text)
    pattern_hash = get_hash(pattern)
    x_power = (x ** (m - 1)) % p
    current_hash = get_hash(text[:m])
    for i in range(n - m):
        if current_hash == pattern_hash and pattern == text[i:i + m]:
            print(i, end=' ')
        current_hash = ((current_hash - ord(text[i]) * x_power) * x + ord(text[i + m])) % p
    if current_hash == pattern_hash and pattern == text[n - m:]:
        print(n - m)


if __name__ == '__main__':
    run()
