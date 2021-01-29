import keyword
log = print


a = 2
log(2)

b = 123123123123
log(b)

c = 'A'
log(c)

name = "ducc caao"
log(name)

q = True
log(q)

x = None
log(x)

# 0 = x
log(keyword.kwlist)

_ = "underscore"
# $y # cannot

x = 9
# y = X*9  # not valid

log("type of a ", type(a))


a, b, c = 1, 2, 3
log(a, b, c)


x = y = [1, 2, 3]
x = [12, 12, 12]

log(x, y)

log(y[0])

x = [1, 2, [12, 12, 12], 33]
log(x)
log(x[2][2])
# log(x[2, 2])
