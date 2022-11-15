a = list(input('Введите строку'))
r = "".join(dict.fromkeys(a))
a = tuple(r)
print(a)
