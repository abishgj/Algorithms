def get_sub_array(array, s):
    j = 1
    for i in range(len(array)):
        sub_sum = sum(array[i:j])
        if sub_sum == s:
            return [i, j]
        print(sub_sum)
        while sub_sum <= s and j < len(array):
            sub_sum += array[j]
            j += 1
            print(sub_sum, array[j])
        if sub_sum == s:
            return [i, j-1]
    return None


if __name__ == '__main__':
    print(get_sub_array([1, 2, 3, 7, 5], 12))
