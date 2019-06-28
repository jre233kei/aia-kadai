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


def best_node(nodes):
    best_score = 999999
    for n in nodes:
        cst = cost(n, goal)
        if cst < best_score:
            best_score = cst
            ans = n
    return ans


def search(pos, route):


    if pos[1] < 0 or pos[1] > max_x or pos[0] < 0 or pos[0] > max_y:
        closed.add(pos)
        return -1, route

    if map_txt[pos[0]][pos[1]] == '#':
        closed.add(pos)
        return -1, route

    print(pos)

    if pos == goal:
        closed.add(pos)
        print("goal")
        return 0, route

    open_pos = [
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1])
        ]


    next_pos = best_node(open_pos)

    closed.add(next_pos)

    result = search(next_pos, route + [next_pos])
    return cost(next_pos, goal), result


def main():
    # print(map_txt[start[0]][start[1]])
    print(search(start, [start]))


if __name__ == '__main__':
    main()
