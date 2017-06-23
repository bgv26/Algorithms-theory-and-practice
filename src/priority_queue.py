class PriorityQueue:
    def __init__(self):
        self.heap = []

    def sift_down(self, index):
        while 2 * index + 1 < len(self.heap):
            left, right = 2 * index + 1, 2 * index + 2
            child_index = left
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                child_index = right
            if self.heap[index] >= self.heap[child_index]:
                break
            self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
            index = child_index

    def sift_up(self, index):
        parent = (index - 1) // 2
        while parent >= 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index, parent = parent, (parent - 1) // 2

    def extract_max(self):
        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return res

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)


def run():
    queue = PriorityQueue()
    for _ in range(int(input())):
        command = input()
        if command == 'ExtractMax':
            print(queue.extract_max())
        if command.startswith('Insert'):
            value = int(command.split()[1])
            queue.insert(value)


if __name__ == '__main__':
    run()
