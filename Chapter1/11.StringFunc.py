import datetime
log = print
s = """w'o'w """
log(str(s))
log(repr(s))
# log(eval(str(s)))

today = datetime.datetime.now()

log(today)
log(str(today))
log(repr(today))


class Represent(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)

    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)


a = Represent(2, 3)
log(a.__repr__())
log(a.__str__())
