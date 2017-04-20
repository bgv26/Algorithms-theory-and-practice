def run():
    num_queries = int(input())
    stack = []
    max_stack = []
    for i in range(num_queries):
        query = input().split()
        if len(query) == 2 and query[0] == 'push':
            value = int(query[1])
            stack.append(value)
            if max_stack:
                max_value = max(value, max_stack[-1])
            else:
                max_value = value
            max_stack.append(max_value)
        elif len(query) == 1 and query[0] == 'pop':
            if stack:
                stack.pop()
            if max_stack:
                max_stack.pop()
        elif len(query) == 1 and query[0] == 'max':
            if max_stack:
                print(max_stack[-1])


if __name__ == '__main__':
    run()
