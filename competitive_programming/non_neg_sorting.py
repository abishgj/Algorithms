def sort_non_negetive(array: list):
    non_neg_array = [x for x in array if x >= 0]
    non_neg_array.sort()
    indexer = 0
    for i in range(len(array)):
        if array[i] >= 0:
            array[i] = non_neg_array[indexer]
            indexer += 1
    return array

if __name__ == "__main__":
    print(sort_non_negetive([0, -2, -1, 5, 2]))