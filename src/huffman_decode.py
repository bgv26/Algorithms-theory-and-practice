def run():
    num_of_char, _ = map(int, input().split())
    code_map = {v: k for k, v in (input().split(': ') for _ in range(num_of_char))}
    code_string = input()
    result = ''
    while code_string:
        for code in code_map.keys():
            if code_string.startswith(code):
                result += code_map[code]
                code_string = code_string[len(code):]
    print(result)


if __name__ == '__main__':
    run()
