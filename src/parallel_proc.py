class Pair:
    def __init__(self, cpu_number, start_time):
        self.cpu_number = cpu_number
        self.start_time = start_time

    def __lt__(self, other):
        return (self.start_time < other.start_time) or \
               (self.start_time == other.start_time and self.cpu_number < other.cpu_number)

    def __eq__(self, other):
        return self.start_time == other.start_time and self.cpu_number == other.cpu_number

    def __repr__(self):
        return 'cpu: {}, time: {}'.format(self.cpu_number, self.start_time)

    def get(self):
        return self.cpu_number, self.start_time


class Queue:
    def __init__(self, size):
        self.size = size
        self.heap = []

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def __len__(self):
        return len(self.heap)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sift_up(self, i):
        while i > 0:
            parent = self.parent(i)
            if self.heap[parent] > self.heap[i]:
                self.__swap(i, parent)
                i = parent
            else:
                break

    def sift_down(self, i):
        while self.left(i) < len(self.heap):
            min_index = i
            left = self.left(i)
            if self.heap[left] < self.heap[min_index]:
                min_index = left
            right = self.right(i)
            if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
                min_index = right
            if i != min_index:
                self.__swap(i, min_index)
                i = min_index
            else:
                break

    def insert(self, pair):
        if len(self.heap) == self.size:
            print('Queue is full')
            return
        self.heap.append(pair)
        self.sift_up(len(self.heap) - 1)

    def extract_min(self):
        result = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.sift_down(0)
        else:
            self.heap.pop()
        return result.get()

    def remove(self, i):
        self.heap[i] = self.heap[0] - 1
        self.sift_up(i)
        self.extract_min()

    def change_priority(self, i, p):
        old_priority = self.heap[i]
        self.heap[i] = p
        if p > old_priority:
            self.sift_down(i)
        else:
            self.sift_up(i)

    @classmethod
    def build_heap(cls, size, array):
        self = cls(size, array)

        for i in range((self.size - 1) // 2, -1, -1):
            self.sift_down(i)

        return self


def run():
    num_of_proc, num_of_tasks = tuple(map(int, input().split()))
    times = list(map(int, input().split()))
    queue = Queue(num_of_proc)
    if num_of_proc < num_of_tasks:
        n = 0
        while n < num_of_proc:
            queue.insert(Pair(n, 0))
            n += 1
        while n < num_of_tasks + num_of_proc:
            proc, start_time = queue.extract_min()
            print(proc, start_time)
            queue.insert(Pair(proc, start_time + times.pop(0)))
            n += 1
    else:
        for i in range(num_of_tasks):
            print(i, 0)


if __name__ == '__main__':
    run()
