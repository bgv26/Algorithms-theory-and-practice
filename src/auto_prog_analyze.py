# class Variable:
#     def __init__(self, i):
#         self.i = i
#         self.parent = None
#         self.rank = 0
#
#     def __repr__(self):
#         return 'value: {}, parent: {}, rank:{}'.format(self.i, self.parent, self.rank)
#
#     def find(self):
#         while self.parent:
#             self.parent = self.parent.find()
#         return self.parent
#
#     def union(self, other):
#         self_parent = self.find()
#         other_parent = other.find()
#         if self_parent == other_parent:
#             return
#         if self_parent.rank > other_parent.rank:
#             other_parent.parent = self_parent
#         else:
#             self_parent.parent = other_parent
#             if self_parent.rank == other_parent.rank:
#                 other_parent.rank += 1
#
#     def set_parent(self, other):
#         if self.parent and other.parent:
#             self.parent.parent = other.parent
#             self.parent = other.parent
#         elif other.parent:
#             self.parent = other.parent
#         elif self.parent:
#             other.parent = self.parent
#         else:
#             self.parent = other
#
#     def is_in_set(self, other):
#         return self.parent == other.parent
#
#
# def run():
#     num_of_vars, num_of_equality, num_of_disparity = map(int, input().split())
#     if num_of_disparity == 0:
#         return 1
#     else:
#         variables = [None for _ in range(num_of_vars)]
#         for i in range(num_of_equality):
#             left, right = map(int, input().split())
#             left -= 1
#             right -= 1
#             if not variables[left]:
#                 variables[left] = Variable(left)
#             if not variables[right]:
#                 variables[right] = Variable(right)
#             variables[left].union(variables[right])
#
#         for i in range(num_of_disparity):
#             left, right = map(int, input().split())
#             left -= 1
#             right -= 1
#             if variables[left]:
#                 left_id = variables[left].find()
#             else:
#                 left_id = None
#             if variables[right]:
#                 right_id = variables[right].find()
#             else:
#                 right_id = None
#             if left_id != right_id:
#                 return 0
#         return 1


def run():
    def find(index):
        if index != parent[index]:
            parent[index] = find(parent[index])
        return parent[index]

    def union(first, second):
        i_id = find(first)
        j_id = find(second)
        if i_id == j_id:
            return
        if rank[i_id] > rank[j_id]:
            parent[j_id] = i_id
        else:
            parent[i_id] = j_id
            if rank[i_id] == rank[j_id]:
                rank[j_id] += 1

    num_of_vars, num_of_equality, num_of_disparity = map(int, input().split())
    if num_of_disparity == 0:
        return 1
    else:
        parent = list(range(num_of_vars))
        rank = [0 for _ in range(num_of_vars)]
        for i in range(num_of_equality):
            left, right = map(int, input().split())
            left -= 1
            right -= 1
            union(left, right)

        for i in range(num_of_disparity):
            left, right = map(int, input().split())
            left -= 1
            right -= 1
            left_id = find(left)
            right_id = find(right)
            if left_id == right_id:
                return 0
        return 1


if __name__ == '__main__':
    print(run())
