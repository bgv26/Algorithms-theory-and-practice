class Variable:
    def __init__(self, i):
        self.i = i
        self.parent = None
        self.rank = 0

    def __repr__(self):
        return 'value: {}, parent: {}, rank:{}'.format(self.i, self.parent, self.rank)

    def find(self):
        if self.parent:
            self.parent = self.parent.find()
            return self.parent
        return self

    def union(self, other):
        self_parent = self.find()
        other_parent = other.find()
        if self_parent == other_parent:
            return
        if self_parent.rank > other_parent.rank:
            other_parent.parent = self_parent
        else:
            self_parent.parent = other_parent
            if self_parent.rank == other_parent.rank:
                other_parent.rank += 1


def run():
    num_of_vars, num_of_equality, num_of_disparity = map(int, input().split())
    if num_of_disparity == 0:
        return 1
    else:
        variables = [Variable(i) for i in range(num_of_vars)]
        for i in range(num_of_equality):
            left, right = map(int, input().split())
            left -= 1
            right -= 1
            variables[left].union(variables[right])

        for i in range(num_of_disparity):
            left, right = map(int, input().split())
            left -= 1
            right -= 1
            left_id = variables[left].find()
            right_id = variables[right].find()
            if left_id == right_id:
                return 0
        return 1


if __name__ == '__main__':
    print(run())
