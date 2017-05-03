def run():
    def get_hash(string):
        p = 1000000007
        x = 263
        result = 0
        for (index, s) in enumerate(string):
            result += (ord(s) * (x ** index)) % p
        return (result % p) % m

    def add(string):
        string_hash = get_hash(string)
        if string not in chain[string_hash]:
            chain[string_hash].insert(0, string)

    def delete(string):
        string_hash = get_hash(string)
        if string in chain[string_hash]:
            chain[string_hash].remove(string)

    def find(string):
        string_hash = get_hash(string)
        if string in chain[string_hash]:
            return 'yes'
        return 'no'

    def check(index):
        return chain[index]

    m = int(input())
    n = int(input())
    chain = [list() for _ in range(m)]
    for i in range(n):
        query = input().split()
        if query[0] == 'add':
            add(query[1])
        elif query[0] == 'del':
            delete(query[1])
        elif query[0] == 'find':
            print(find(query[1]))
        elif query[0] == 'check':
            print(*check(int(query[1])))


if __name__ == '__main__':
    run()
