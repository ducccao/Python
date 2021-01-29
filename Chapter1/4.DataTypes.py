log = print

# 1: bool
x = True
y = False

log(x or y)
log(x and y)
log(not x)
log(x)

isinstance(bool, int)

# 2: number
a = 2
b = 312312
c = 3.12323
d = 100+10j
log(a, b, c, d)

# 3: string
a = reversed("hello")
log(a)

# tuple
a = (1, 2, 3)
log(a)
b = ('a', 1, "py", (1, 2))
log(b)
log(b[2])


# list
a = [1, 2, 3]
b = ['a', 1, [1, 2, 3], (1, 2)]
log(a, b)


# set
a = {1, 2, 'a'}
log(a)
b = {
    'name': "caheo",
    'age': [1, 2, 3]
}

log(b)
log(b)

a = None
log(type(a))

if a is None:
    log("A is none")
a = "Hello"
log(list(a)[0])
log(set(a))

log(tuple(a))


def f(m):
    m.append(3)


x = [1, 2]
f(x)
log(x)
