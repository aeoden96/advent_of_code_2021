
def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            input, output = line.split(" | ")
            yield input.rstrip().split(), output.rstrip().split()



f = get_input("input.txt")

# nums = [0,0,0,0]
#
#
# for inp, out in f:
#     for word in out:
#         if len(word) == 3:
#             nums[2] += 1
#         if len(word) == 4:
#             nums[1] += 1
#         if len(word) == 2:
#             nums[0] += 1
#         if len(word) == 7:
#             nums[3] += 1
# print(sum(nums))


def is_one_in_other(a, smaller):
    for i in smaller:
        if i not in a:
            return False
    return True


def find_num_of_len(line, word_len):
    return [word for word in line if len(word) == word_len]


def difference(a, b):
    for i in b:
        a = a.replace(i, "")
    return a


def get_num_from_string(word, alfabet):
    if len(word) == 2:
        return 1
    if len(word) == 3:
        return 7
    if len(word) == 4:
        return 4
    if len(word) == 7:
        return 8
    if len(word) == 5:
        if alfabet['e'] in word:
            return 2
        if alfabet['b'] in word:
            return 5
        return 3
    if len(word) == 6:
        if alfabet['d'] not in word:
            return 0
        elif alfabet['e'] in word:
            return 6
        return 9

#   aaaa
#  b    c
#  b    c
#   dddd
#  e    f
#  e    f
#   gggg

S = 0
for inp, out in f:
    # print(inp, out)
    number_1 = find_num_of_len(inp, 2)[0]
    number_7 = find_num_of_len(inp, 3)[0]
    number_4 = find_num_of_len(inp, 4)[0]

    a = difference(number_7, number_1)

    numbers_6_9_0 = find_num_of_len(inp, 6)
    numbers_2_3_5 = find_num_of_len(inp, 5)
    for num in numbers_6_9_0:
        if not is_one_in_other(num, number_1):
            number_6 = num
            break

    for num in numbers_6_9_0:
        if is_one_in_other(num, number_4):
            number_9 = num
            break
    for num in numbers_6_9_0:
        if num != number_9 and num != number_6:
            number_0 = num
            break

    for num in numbers_2_3_5:
        if is_one_in_other(num, number_1):
            number_3 = num
            break

    c = difference(number_1, number_6)

    f = difference(number_1, c)

    g = difference(difference(number_9, number_4), a)

    b = difference(number_9, number_3)

    for num in numbers_2_3_5:
        if is_one_in_other(num, b):
            number_5 = num
            break

    for num in numbers_2_3_5:
        if num != number_5 and num != number_3:
            number_2 = num
            break
    d = difference(number_5, a + b +f +g)
    e = difference(number_2, a+c+d+g)


    alfabet = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g
    }
    str_out = ""
    for word in out:
        num = get_num_from_string(word, alfabet)
        str_out += str(num)
    real_out = int(str_out)
    S += real_out

print(S)







