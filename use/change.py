class Change:
    a = "grin"
    b = "blue"
    c = "white"

    d = "black"
    e = "yellow"
    f = "rad"

    color = {
        "a": d,
        "b": e,
        "c": f,

        "d": a,
        "e": b,
        "f": c,
    }

    def change(self, item):
        match item:
            case "a":
                return Change.d
            case "b":
                return Change.e
            case "c":
                return Change.f

    def change_2(self, item):
        return Change.color[item]


if __name__ == '__main__':
    c = Change()
    print(c.change("b"))
    print(c.change_2("a"))
