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

start = (9, 5)
goal = (0, 5)

closed = set()


def cost(from_, to):
    return abs(from_[0] - to[0]) + abs(from_[1] - to[1])


def order_by_cost(nodes):
    pn = [(n, cost(n, goal)) for n in nodes]
    for i in range(len(pn)-1):
        for ii in range(len(pn)-1):
            if pn[ii][1] > pn[ii+1][1]:
                tmp = pn[ii]
                pn[ii] = pn[ii+1]
                pn[ii+1] = tmp
    print([n[0] for n in pn])
    return [n[0] for n in pn]


def best_node(nodes):
    best_score = 999999
    for n in nodes:
        cst = cost(n, goal)
        if cst < best_score:
            best_score = cst
            ans = n
    print("best is {0}".format(ans))
    return ans


def search(pos, route):

    if pos[1] < 0 or pos[1] > max_x or pos[0] < 0 or pos[0] > max_y:
        return -1, route

    if map_txt[pos[0]][pos[1]] == '#':
        return -1, route

    if pos in closed:
        return -1, route

    print(pos)

    if pos == goal:
        closed.add(pos)
        print("goal")
        return 0, route

    open_pos = order_by_cost([
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1])
    ])

    closed.add(pos)

    for o in open_pos:
        s = search(o, route+[o])
        print("search result of {0} is {1}".format(o, s[0]))
        if s[0] == 0:
            return s


def main():
    print(search(start, [start]))


if __name__ == '__main__':
    main()
