map_txt = """\
.....G......
............
...#####....
............
............
............
............
............
............
.....S......
............\
""".split()

max_x = 11
max_y = 10


closed = set()


class vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return self.x + self.y


class field:
    field = {}

    def __init__(self, txt):
        for i in range(len(txt)):
            for j in range(len(txt[i])):
                self.field[vector2(j, i)] = map_txt[i][j]

    def get_tile(self, pos):
        return self.field.get(pos)

    def __str__(self):
        return str([str(l) for l in self.field])


start = vector2(5, 9)
goal = vector2(5, 0)

main_field = field(map_txt)


def cost(from_, to):
    return abs(from_.x - to.x) + abs(from_.y - to.y)


def order_by_cost(nodes):
    pn = [(n, cost(n, goal)) for n in nodes]
    for i in range(len(pn)-1):
        for ii in range(len(pn)-1):
            if pn[ii][1] > pn[ii+1][1]:
                tmp = pn[ii]
                pn[ii] = pn[ii+1]
                pn[ii+1] = tmp
    return [n[0] for n in pn]


def search_internal(pos, route):

    if main_field.get_tile(pos) == None:
        return -1, route

    if main_field.get_tile(pos) == '#':
        return -1, route

    if pos in closed:
        return -1, route

    if pos == goal:
        closed.add(pos)
        return 0, route

    open_pos = order_by_cost([
        vector2(pos.x+1, pos.y),
        vector2(pos.x-1, pos.y),
        vector2(pos.x, pos.y+1),
        vector2(pos.x, pos.y-1)
    ])

    closed.add(pos)

    for o in open_pos:
        s = search_internal(o, route+[o])
        if s[0] == 0:
            return s


def search(from_):
    print([str(n) for n in search_internal(from_, [from_])[1]])


def main():
    search(start)


if __name__ == '__main__':
    main()
