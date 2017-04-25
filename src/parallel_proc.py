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
            if self.heap[parent][1] > self.heap[i][1]:
                self.__swap(i, parent)
                i = parent
            else:
                break

    def sift_down(self, i):
        while self.left(i) < len(self.heap):
            min_index = i
            left = self.left(i)
            if self.heap[left][1] < self.heap[min_index][1]:
                min_index = left
            right = self.right(i)
            if right < len(self.heap) and self.heap[right][1] < self.heap[min_index][1]:
                min_index = right
            if i != min_index:
                self.__swap(i, min_index)
                i = min_index
            else:
                break

    def insert(self, proc_num, start_time, end_time):
        if len(self.heap) == self.size:
            print('Queue is full')
            return
        self.heap.append((proc_num, start_time, end_time))
        self.sift_up(len(self.heap) - 1)

    def extract_min(self):
        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return result

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

    def build_heap(self):
        for i in range((self.size - 1) // 2, -1, -1):
            self.sift_down(i)


def run():
    num_of_proc, num_of_tasks = tuple(map(int, input().split()))
    times = tuple(map(int, input().split()))
    queue = Queue(num_of_proc)
    n = 0
    while n < num_of_proc:
        queue.insert(n, 0, times[n])
        n += 1
    # queue.build_heap()
    while n < num_of_tasks:
        proc, start_time, end_time = queue.extract_min()
        print(proc, start_time)
        queue.insert(proc, end_time, end_time + times[n])
        n += 1
    while queue:
        proc, start_time, end_time = queue.extract_min()
        print(proc, start_time)


if __name__ == '__main__':
    run()
