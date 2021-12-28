

def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            yield line


open_b = "{[(<"
close = "}])>"

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
points2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}
S=0
S2=[]
inputs = get_input("input.txt")
for input in inputs:

    l = len(input)
    while True:
        found = False
        for p, c in zip(input, input[1:]):
            # print(p,c)
            if c in close and p in open_b:
                ind_closed = close.index(c)
                if open_b[ind_closed] == p:
                    found = True
                    break
        if found:
            input = input.replace(p + c, "")

        if l == len(input):
            break
        l = len(input)



    stack = []
    line_wrong=False
    for i in input:
        if i in open_b:
            stack.append(i)
        if i in close:
            top = stack[-1]
            ind_closed = open_b.index(top)
            if i == close[ind_closed]:
                stack.pop()
            else:
                # print("err,found", i, "looking for ", close[ind_closed])
                S += points[i]
                line_wrong=True
                break
    if not line_wrong:
        ss=0

        for i in stack[::-1]:
            ss=ss*5+points2[i]

        S2.append(ss)
        print(input, "            ", stack[::-1],ss)

S2 = sorted(S2)

print(S2[int(len(S2)/2)])