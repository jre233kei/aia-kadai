import vector2 as vec2
import field as fld
import math

# 過去のノードを保存する

map_txt = """\
.....G....
..........
...#####..
..........
..........
..........
.....S....
..........\
""".split()


max_x = len(map_txt[0]) - 1
max_y = len(map_txt) - 1

closed = set()
open_prev = set()
open_next = set()

start = vec2.vector2(5, 6)
goal = vec2.vector2(5, 0)

main_field = fld.field(map_txt)

cnt = 0


def cost(from_, to):
    return math.sqrt(abs(from_.x - to.x) + abs(from_.y - to.y))


def order_by_cost(nodes):
    pn = [(n, cost(n, goal)) for n in nodes]
    for i in range(len(pn) - 1):
        for ii in range(len(pn) - 1):
            if pn[ii][1] > pn[ii + 1][1]:
                tmp = pn[ii]
                pn[ii] = pn[ii + 1]
                pn[ii + 1] = tmp
    return [n[0] for n in pn]


def traverse(n):
    global closed

    for c in closed:
        if c[0] == n:
            print("AA")
            return [n] + traverse(c[1])
    return []


def search_internal():
    global cnt
    cnt += 1

    global open_prev
    global open_next
    global closed

    if cnt == 3:
        print([(str(o[0]), str(o[1])) for o in open_prev])
        print([(str(o[0]), str(o[1])) for o in open_next])
        print([(str(o[0]), str(o[1])) for o in closed])
    for o in open_prev:

        open_pos = [
            vec2.vector2(o[0].x + 1, o[0].y),
            vec2.vector2(o[0].x - 1, o[0].y),
            vec2.vector2(o[0].x, o[0].y + 1),
            vec2.vector2(o[0].x, o[0].y - 1)
        ]

        for op in open_pos:
            if op == goal:
                print("GOALL")
                closed.add((op, o[0]))
                return traverse(op)

            if not main_field.get_tile(op):
                continue

            if main_field.get_tile(op) == '#':
                continue

            for c in closed:
                # print("c is "+ str (c))
                if op == c[0]:
                    continue

            open_next.add((op, o[0]))

        closed.add(o)
        # print((str(o[0]), str(o[1])))
    open_prev.clear()
    for on in open_next:
        open_prev.add(on)
    open_next.clear()
    # print("XX")
    search_internal()


def search(from_):
    open_prev.add((from_, None))
    print(search_internal())


def main():
    search(start)


if __name__ == '__main__':
    main()
