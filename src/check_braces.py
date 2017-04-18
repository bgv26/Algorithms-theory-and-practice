def run(string):
    braces = {')': '(', '}': '{', ']': '['}
    stack = []
    for i, c in enumerate(string, start=1):
        if c in braces.values():
            stack.append((c, i))
        if c in braces and (not stack or braces[c] != stack.pop()[0]):
            return i
    return stack.pop()[1] if stack else 'Success'


if __name__ == '__main__':
    print(run(input()))
