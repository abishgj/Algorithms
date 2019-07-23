def calc_median(array: list):
    mid_index = len(array) // 2
    if len(array) % 2 == 0:
        return (array[mid_index] + array[mid_index - 1]) / 2
    else:
        return array[mid_index]


def median_pooling(input_arr: list, pool_window: list, stride_window: list) -> list:
    """
    Calculate the median pooling for the given input array
    :param input_arr: Input array
    :param pool_window: Pooling window
    :param stride_window: Pooling operation strides
    :return: Returns median pooled array
    """
    pool_rows = pool_window[0]
    pool_columns = pool_window[1]
    stride_rows = stride_window[0]
    stride_columns = stride_window[1]
    output_arr = []
    for i in range(0, len(input_arr) - stride_rows, stride_rows):
        each_row = []
        for j in range(0, len(input_arr[1]) - stride_columns, stride_columns):
            pool_arr = [x for k in range(i, i + pool_rows) for x in input_arr[k][j:j + pool_columns]]
            pool_arr.sort()
            each_row.append(calc_median(pool_arr))
        output_arr.append(each_row)
    return output_arr


if __name__ == '__main__':
    inp_arr = [[1, 5, 6, 2], [7, 4, 3, 2], [8, 6, 1, 3]]
    p_win = [2, 2]
    s_win = [1, 1]
    out_arr = median_pooling(input_arr=inp_arr, pool_window=p_win, stride_window=s_win)
    print(out_arr)
