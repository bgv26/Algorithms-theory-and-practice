class Heap:
    def __init__(self, size, heap):
        self.size = size
        self.heap = heap
        self.swaps = []

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.swaps.append((i, j))

    def sift_up(self, i):
        while i > 0:
            parent = self.parent(i)
            if self.heap[parent] > self.heap[i]:
                self.__swap(i, parent)
                i = parent
            else:
                break

    def sift_down(self, i):
        while self.left(i) < self.size:
            min_index = i
            left = self.left(i)
            if self.heap[left] < self.heap[min_index]:
                min_index = left
            right = self.right(i)
            if right < self.size and self.heap[right] < self.heap[min_index]:
                min_index = right
            if i != min_index:
                self.__swap(i, min_index)
                i = min_index
            else:
                break

    def build_heap(self):
        for i in range((self.size - 1) // 2, -1, -1):
            self.sift_down(i)

        self.__print_result()

    def __print_result(self):
        print(len(self.swaps))
        for pair in self.swaps:
            print(*pair)


def run():
    size = int(input())
    array = list(map(int, input().split()))
    heap = Heap(size, array)
    heap.build_heap()


if __name__ == '__main__':
    run()
