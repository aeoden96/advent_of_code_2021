def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            a, b = line.split(" -> ")
            a,b,c,d = (*a.split(","), *b.split(","))
            yield int(a),int(b),int(c),int(d)




X = [[0] * 10 for i in range(10)]


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
        for y in range(b, d+1):
            X[y][a] += 1
    elif b == d:
        for x in range(a, c+1):
            X[b][x] += 1

[print(x) for x in X]