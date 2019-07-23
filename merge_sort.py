def conquer(left_array, right_array):
    merged_array = []
    total_len = len(left_array) + len(right_array)
    i, j, k = 0, 0, 0
    for _ in range(total_len):
        if i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                merged_array.append(left_array[i])
                i += 1
            else:
                merged_array.append(right_array[j])
                j += 1
        elif i < len(left_array):
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            j += 1
    return merged_array


def divide(array):
    if len(array) == 1:
        return array
    cur_index = int(len(array) / 2)
    return conquer(divide(array[:cur_index]), divide(array[cur_index:]))


def mergeSort(arr):
    arr = divide(array=arr)
    return arr


if __name__ == '__main__':
    test = [3, 2, 1, 5, 4, 6]
    print(test)
    print(mergeSort(test))
