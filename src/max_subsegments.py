class MaxStack:
    def __init__(self):
        self._stack = []
        self._max_stack = []

    def __len__(self):
        return len(self._stack)

    def push(self, value):
        self._stack.append(value)
        if self._max_stack:
            self._max_stack.append(max(value, self._max_stack[-1]))
        else:
            self._max_stack.append(value)

    def pop(self):
        self._max_stack.pop()
        return self._stack.pop()

    def max(self):
        return self._max_stack[-1]


class MaxQueue:
    def __init__(self):
        self._input = MaxStack()
        self._output = MaxStack()

    def push(self, value):
        self._input.push(value)

    def pop(self):
        if self._output:
            return self._output.pop()
        else:
            while self._input:
                self._output.push(self._input.pop())

    def max(self):
        if len(self._output) and len(self._input):
            return max(self._output.max(), self._input.max())
        elif self._output:
            return self._output.max()
        else:
            return self._input.max()


def run():
    size = int(input())
    array = list(map(int, input().split()))
    window_size = int(input())
    max_queue = MaxQueue()
    i = 0
    while i < window_size:
        max_queue.push(array[i])
        i += 1
    while i < size:
        print(max_queue.max(), end=' ')
        max_queue.pop()
        i += 1


if __name__ == '__main__':
    run()
