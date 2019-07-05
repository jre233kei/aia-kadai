import vector2 as vec2
import field as fld


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

start = vec2.vector2(5, 9)
goal = vec2.vector2(5, 0)

main_field = fld.field(map_txt)


def cost(from_, to):
    return math.sqrt(abs(from_.x - to.x) + abs(from_.y - to.y))


def order_by_cost(nodes):
    pn = [(n, cost(n, goal)) for n in nodes]
    for i in range(len(pn)-1):
        for ii in range(len(pn)-1):
            if pn[ii][1] > pn[ii+1][1]:
                tmp = pn[ii]
                pn[ii] = pn[ii+1]
                pn[ii+1] = tmp
    return [n[0] for n in pn]


def search_internal(pos, route, gcost):

    if main_field.get_tile(pos) == None:
        return -1, route, gcost

    if main_field.get_tile(pos) == '#':
        return -1, route, gcost

    if pos in closed:
        return -1, route, gcost

    if pos == goal:
        closed.add(pos)
        return 0, route, gcost

    open_pos = order_by_cost([
        vec2.vector2(pos.x+1, pos.y),
        vec2.vector2(pos.x-1, pos.y),
        vec2.vector2(pos.x, pos.y+1),
        vec2.vector2(pos.x, pos.y-1)
    ])

    closed.add(pos)

    cands = []

    for o in open_pos:
        s = search_internal(o, route+[o], gcost + 1)
        if s[0] == 0:
            cands.append((s, cost(o, goal) + s[2]))

    if cands:
        return sorted(cands)[0][0]
    return -1, route, gcost


def search(from_):
    print([str(n) for n in search_internal(from_, [from_], 0)[1]])


def main():
    search(start)


if __name__ == '__main__':
    main()
