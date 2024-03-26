from functools import reduce


def sum_filter_temp(array):
    temp_filtered = list(filter(lambda x: x > 0, array))
    print(temp_filtered)
    temp_reordered = list(map(lambda x: x * 9 / 5 + 32, temp_filtered))
    print(temp_reordered)
    temp_sum = reduce(lambda x, y: x + y, temp_reordered, 0)
    print(temp_sum)
    print(len(temp_filtered))
    return temp_sum / len(temp_filtered)


print(sum_filter_temp([1, 2, 3, 4, 6, -1]))
