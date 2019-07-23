def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr[:i + 1]) - 1, 0, -1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else:
                break


if __name__ == '__main__':
    arr = [1, 4, 5, 3, 6, 7]
    print(insertion_sort(arr=[1, 4, 5, 3, 6, 7]))
    print(arr)
