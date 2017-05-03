phone_book = {}


def add(number, name):
    phone_book[number] = name


def delete(number):
    if number in phone_book:
        del phone_book[number]


def find(number):
    if number in phone_book:
        return phone_book[number]
    else:
        return 'not found'


def run():
    num_of_queries = int(input())
    for i in range(num_of_queries):
        query = input().split()
        if query[0] == 'add':
            if len(query) == 3:
                add(query[1], query[2])
        elif query[0] == 'del':
            delete(query[1])
        elif query[0] == 'find':
            print(find(query[1]))


if __name__ == '__main__':
    run()
