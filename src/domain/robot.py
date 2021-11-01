from src.domain.layout import Point


class Robot:
    def __init__(self, name: str, r_id: int, v: int, a: int, start: Point, chg: int):
        self.name = name
        self.r_id = r_id
        self.v = v
        self.a = a
        self.start = start
        self.chg = chg

    def get_constructor(self):
        return "{} = Robot({}, {}, {}, {:.2f}, {:.2f});\n{} = Battery({}, {});\n".format(self.name, self.r_id, self.v,
                                                                                         self.a, self.start.x,
                                                                                         self.start.y,
                                                                                         "b_{}".format(self.name),
                                                                                         self.r_id, self.chg)
