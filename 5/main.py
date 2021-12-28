def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            a, b = line.split(" -> ")
            a,b,c,d = (*a.split(","), *b.split(","))
            yield int(a),int(b),int(c),int(d)




X = [[0] * 1000 for i in range(1000)]


f = get_input("input.txt")
# for a,b,c,d in f:
#     K = (d-b)/(c-a)
#
#     if K > 1 or K < -1:
#         for y in range(a,c):
#             expr = (y-b)*(c-a)/(d-b)+a
#             if expr.is_integer():
#                 X[y][int(expr)] += 1
#     else:
#
#         for x in range(a,c):
#             expr = (d-b)/(c-a)*(x-a)+b
#             if expr.is_integer():
#                 X[int(expr)][x] += 1

for a, b, c, d in f:

    if a == c:
        for y in range(min(b, d), max(d, b)+1):
            X[y][a] += 1
    elif b == d:
        for x in range(min(a, c), max(a, c)+1):
            X[b][x] += 1
    elif abs(a-c) == abs(b-d):
        x = a
        y = b

        ind_x = 1 if max(a, c) == c else -1
        ind_y = 1 if max(b, d) == d else -1

        while y != d:
            X[y][x] += 1
            x += ind_x
            y += ind_y
        X[y][x] += 1
    # print()
    # print(a, b, c, d)
    # [print(x) for x in X]



S = sum([1 for line in X for i in line if i >= 2])
print("S:", S)

