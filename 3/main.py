NUM_OF_INPUTS = 1000
BINARY_SIZE = 12


def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            yield line.rstrip()


def get_num_of_ones(elements):
    most_common = [0] * BINARY_SIZE
    for i, bin_num in enumerate(elements):
        for j, k in enumerate(bin_num):
            most_common[j] += int(k)
    return most_common


def most_common(num_of_ones, value, num_of_inputs):
    if value == 1:
        return [str(int(i >= num_of_inputs/2)) for i in num_of_ones]
    return [str(int(i < num_of_inputs/2)) for i in num_of_ones]

f = get_input("input_demo.txt")
num_of_ones = get_num_of_ones(f)

gama =    "".join(most_common(num_of_ones, 1, NUM_OF_INPUTS))
epsilon = "".join(most_common(num_of_ones, 0, NUM_OF_INPUTS))

gama_int = int(gama, 2)
epsilon_int = int(epsilon, 2)


def get_oxygen_or_co2(value):
    f = get_input("input_demo.txt")
    num_of_ones = get_num_of_ones(f)
    gama = "".join(most_common(num_of_ones, value, NUM_OF_INPUTS))
    f = get_input("input_demo.txt")
    oxygen_list = [k for i, k in enumerate(f) if gama[0] == k[0]]
    for i in range(BINARY_SIZE - 1):
        if len(oxygen_list) < 2:
            break
        i += 1
        num_of_ones = get_num_of_ones(oxygen_list)
        num_of_ones = "".join(most_common(num_of_ones, value, len(oxygen_list)))
        oxygen_list = [k for k in oxygen_list if num_of_ones[i] == k[i]]

    return oxygen_list[0]


print("Gama:", gama_int)
print("Epsilon:", epsilon_int)
print("Consumption:", gama_int * epsilon_int)


oxy_int = int(get_oxygen_or_co2(1), 2)
co2_int = int(get_oxygen_or_co2(0), 2)


print("Oxygen:", oxy_int)
print("CO2:", co2_int)
print("Life support rating:", oxy_int*co2_int)

