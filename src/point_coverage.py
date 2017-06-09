class Segment:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __contains__(self, item):
        return self.left <= item <= self.right

    def __repr__(self):
        return "left: {}, right: {}".format(self.left, self.right)


def run():
    segments = [Segment(*map(int, input().split())) for _ in range(int(input()))]
    segments.sort(key=lambda s: s.right)
    result = []
    point = 0
    for segment in segments:
        if not result or (point not in segment):
            point = segment.right
            result.append(point)
    print(len(result))
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    run()
