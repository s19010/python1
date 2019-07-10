def division2():
    num = int(input("２で割ります。"))
    return num / 2


print(division2())


def multiplication4():
    num = int(input("４を掛けます"))
    return num * 4


print(multiplication4())


result = division2()
print(multiplication4(result))
