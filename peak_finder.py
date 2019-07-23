def peak_finder_recur(array):
    print(array)
    n = len(array)
    if n > 2:
        mid_index = int(n / 2)
        if array[mid_index] < array[mid_index - 1] and len(array[:mid_index + 1]) > 2:
            return peak_finder_recur(array[:mid_index + 1])
        elif array[mid_index] < array[mid_index + 1] and len(array[mid_index:]) > 2:
            return peak_finder_recur(array[mid_index:])
        else:
            return array[mid_index]


def peak_finder_1d(array):
    if array[0] > array[1]:
        return array[0]
    elif array[-1] > array[-2]:
        return array[-1]
    else:
        return peak_finder_recur(array=array)


# print("*" * 20)
# print(array)
# n = len(array)
# if n > 1:
#     mid_val = int(n / 2)
#     print(n, mid_val, array[mid_val])
#     if array[mid_val] < array[mid_val - 1]:
#         peak_finder_1d(array[:mid_val])
#     elif array[mid_val] < array[mid_val + 1]:
#         peak_finder_1d(array[mid_val + 1:])
#     else:
#         return array[mid_val]

def peak_finder_2d_recur(matrix):
    print(matrix)
    n_cols = len(matrix[0])
    if n_cols > 2:
        mid_col = int(n_cols / 2)
        col_values = [row[mid_col] for row in matrix]
        row_index = col_values.index(max(col_values))
        key = matrix[row_index][mid_col]
        print(col_values, mid_col, key, row_index)
        if key < matrix[row_index][mid_col - 1]:
            return peak_finder_2d_recur([row[:mid_col + 1] for row in matrix])
        elif key < matrix[row_index][mid_col + 1]:
            return peak_finder_2d_recur([row[mid_col:] for row in matrix])
        else:
            return key


def peak_finder_2d(matrix):
    n_cols = len(matrix[0])
    if n_cols == 1:
        return max(matrix[0])
    else:
        first_col = [row[0] for row in matrix]
        key = max(first_col)
        max_index = first_col.index(key)
        if key > matrix[max_index][1]:
            return key
        last_col = [row[n_cols - 1] for row in matrix]
        key = max(last_col)
        max_index = last_col.index(key)
        if key > matrix[max_index][n_cols - 2]:
            return key
        return peak_finder_2d_recur(matrix)


if __name__ == '__main__':
    array = [1, 3, 15, 9, 7, 5, 9, 7, 1]
    matrix = [[4, 6, 2, 2], [8, 9, 6, 5], [5, 13, 8, 6], [0, 9, 8, 4], [12, 13, 4, 1]]
    # print(peak_finder_1d(array=array))
    print(peak_finder_2d(matrix))
