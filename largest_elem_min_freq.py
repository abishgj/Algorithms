from collections import Counter


def largest_elem_min_freq(array: list):
    counter_dict = Counter(array)
    sorted_array = sorted(counter_dict.items(), key=lambda x: (-x[0], x[1]))
    return sorted_array[0][0]


if __name__ == '__main__':
    print(largest_elem_min_freq([2, 2, 5, 50, 1]))