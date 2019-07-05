import vector2 as vec2


class field:
    field = {}

    def __init__(self, txt):
        for i in range(len(txt)):
            for j in range(len(txt[i])):
                self.field[vec2.vector2(j, i)] = txt[i][j]

    def get_tile(self, pos):
        return self.field.get(pos)

    def __str__(self):
        return str([str(l) for l in self.field])
