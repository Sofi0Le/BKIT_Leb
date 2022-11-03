data =[1, 2, 3]

res1 = list(zip(data, map(lambda x: x**2, data)))
print(res1)

res2 =list([(x, x**2) for x in data])
print(res2)

res3 = list((x, y) for ix, x in enumerate(data) for iy, y in enumerate(map(lambda x: x**2, data)) if ix == iy)
print(res3)

res4 =list(map(lambda x: (x,x**2), data))
print(res4)

res5 = list(zip(data, [i**2 for i in data]))
print(res5)