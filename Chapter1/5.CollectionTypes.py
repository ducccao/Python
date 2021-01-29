log = print

# List

int_list = [1, 2, 3]
string_list = ['asd', 'b', 'c']
empty_list = []
mixed_list = [1, 2, 'abc', [2, 3, 4], None, True, {}, (1, 2, 3)]
nested_list = [[1, 2, 3], [4, 5, 6]]
log(mixed_list)
log(mixed_list[0])
log(mixed_list[-1])
log(mixed_list[-2])  # can do with negative indices
name = ['a', 'b', 'c']
name.insert(4, 'd')
log(name)
name.remove('d')
# name.remove('e')

log(name)
log(name.index('b'))
log(name.count('a'))
name.insert(5, "a")
log(name)
log(name.count('a'))
name.reverse()
log(name)
log(name[::-1])


name.pop()

for ele in name:
    log(ele)

# Tuple
ip_address = ('10.20.30.40', 8080)
log(ip_address)
for i in ip_address:
    log(i)


# tuple is immutable data structure
temp = tuple([1, 2])
log(temp)
log(temp.count(1))

# Dictionary
person = {
    'name': "duccao",
    'age': 3
}

log(person['name'])

for key in person.keys():
    log(person[key])
    #log("format: ", format(person[key], key))

# Set
name = {'duc1', 'duc2', 'duc3'}
mylist = [1, 2, 3]
myset = set(mylist)
log(myset)
log(name)

if 1 in mylist:
    log(name)
