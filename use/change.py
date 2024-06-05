class Change:
    a = "grin"
    b = "blue"
    c = "white"

    d = "rad"
    e = "yellow"
    f = "black"

    color = {
        a: d,
        b: e,
        c: f,

        d: a,
        e: b,
        f: c,
    }

    def change(self, item):
        match item:
            case Change.a:
                return Change.d
            case Change.b:
                return Change.e
            case Change.c:
                return Change.f

    def change_2(self, item):
        return Change.color[item]


if __name__ == '__main__':
    c = Change()
    print(c.change("grin"))
    print(c.change_2("blue"))
