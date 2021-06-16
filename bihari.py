x = "aaabbshddddjffjddss"

def split(X):
    res = []
    for i in X:
        res.append(i)
    return res

def Counter(X):
    a = split(X)
    mapstr = {}
    z = []
    print(a)
    for i in a:
        if mapstr.get(i):
            mapstr[i] = mapstr[i] + 1

        else:
            mapstr[i] = 1


        # z.append([i,count])
    return mapstr
# [['b', 2], ['a', 3], ['d', 6], ['j', 2], ['f', 2], ['s', 3], ['h', 1]]

print(Counter(x))