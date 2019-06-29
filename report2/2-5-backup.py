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

START = (9, 5)
GOAL = (0, 5)

closed = set()

LIMIT = 100


class node:
    def __init__(self, route, cost):
        self.route = route
        self.cost = cost


def cost(from_, to):
    return abs(from_[0] - to[0]) + abs(from_[1] - to[1])


def best_node1(nodes):
    best_score = 999999
    for n in nodes:
        cst = cost(n, GOAL)
        print("{0} , {1}".format(cst, n))
        if cst < best_score:
            best_score = cst
            ans = n
    return ans


def search(pos, route, cost):
    if cost > LIMIT:
        return -1, route, cost1+

    if pos in closed:
        return -1, route, cost+1

    if pos[1] < 0 or pos[1] > max_x or pos[0] < 0 or pos[0] > max_y:
        closed.add(pos)
        return -1, route, cost + 1

    if map_txt[pos[0]][pos[1]] == '#':
        closed.add(pos)
        return -1, route, cost+1

    print(pos)

    if pos == GOAL:
        closed.add(pos)
        print("GOAL")
        return -1, route + [pos], cost+1

    open_pos = [
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1])
    ]

    open_node = []

    closed.add(pos)

    for o in open_pos:
        r = search(o, route + [o], cost+1)
        if r[0] < 0:
            continue
        if r[0] == 0:
            open_node.append(r)

    if len(open_node) > 0:
        best_cost = 9999999
        for o in open_node:
            print(best_cost)
            if o[2] < best_cost:
                best_cost = o[0]
            else:
                open_node.pop(o)

        return 0, o[1] + [pos], cost+1

    return cost, route, cost+1

    # return cost(next_pos, GOAL), result[1]


def main():
    print(search(START, [START], 0))


if __name__ == '__main__':
    main()
