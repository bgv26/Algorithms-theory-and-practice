class Table:
    def __init__(self, table_num, table_size):
        self._table_num = table_num
        self._table_size = table_size
        self._parent = table_num

    def __lt__(self, other):
        return self.table_size < other.table_size

    def __eq__(self, other):
        return self.table_size == other.table_size

    def __repr__(self):
        return 'num: {}, records: {}'.format(self.table_num, self.table_size)

    def __str__(self):
        return str(self.table_size)

    def __int__(self):
        return self.table_size

    @property
    def table_num(self):
        return self._table_num

    @table_num.setter
    def table_num(self, value):
        self._table_num = value

    @property
    def table_size(self):
        return self._table_size

    @table_size.setter
    def table_size(self, value):
        self._table_size = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value


def join(src, dest, tables):
    src_table = tables[src - 1]
    dest_table = tables[dest - 1]
    if src_table.parent != dest_table.parent:
        while src_table.table_num != src_table.parent:
            src_table = tables[src_table.parent - 1]
        tables[src - 1].parent = src_table.parent
        while dest_table.table_num != dest_table.parent:
            dest_table = tables[dest_table.parent - 1]
        tables[dest - 1].parent = dest_table.parent
        if src_table.table_num != dest_table.table_num:
            src_table.parent = dest_table.table_num
            dest_table.table_size += src_table.table_size
            src_table.table_size = 0
        else:
            tables[src - 1].parent = tables[dest - 1].parent = dest_table.table_num
    return dest_table.table_size


# def join(dest, src, parents, sizes):
#     orig_dest = dest
#     orig_src = src
#     while dest != parents[dest]:
#         dest = parents[dest]
#     parents[orig_dest] = dest
#     while src != parents[src]:
#         src = parents[src]
#     parents[orig_src] = src
#     if dest != src:
#         parents[src] = dest
#         sizes[dest] += sizes[src]
#         sizes[src] = 0
#     else:
#         parents[orig_dest] = parents[orig_src] = dest
#     return sizes[dest]


def run():
    num_tables, num_queries = tuple(map(int, input().split()))
    # parents = list(range(num_tables))
    # sizes = list(map(int, input().split()))
    tables = [Table(i, int(size)) for i, size in enumerate(input().split(), start=1)]
    # max_size = max(sizes)
    max_size = int(max(tables))
    # max_size = max_size.table_size

    for i in range(num_queries):
        dest, src = tuple(map(int, input().split()))
        # new_size = join(dest - 1, src - 1, parents, sizes)
        new_size = join(src, dest, tables)
        max_size = max(max_size, new_size)
        print(max_size)


if __name__ == '__main__':
    run()
