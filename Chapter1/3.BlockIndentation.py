log = print


def hi():
    a = 2
    b = 3
    if a > b:
        log(a)
    else:
        log(b)
    return a


def will_be_implemented_later():
    pass


log(hi())
