import sys
import time
import random
from copy import copy


class MaxHeap:
    INT_MIN = -sys.maxsize - 1

    def __init__(self, array: list = []):
        self.heap_array = self._build_max_heap(array=array)
        self.heap_size = len(self.heap_array)
        self.heap_start = self.heap_size - 1
        self.inc_size = 1000
        print(len(self.heap_array))

    def _build_max_heap(self, array: list):
        start = int(len(array) / 2) - 1
        for i in range(start, -1, -1):
            self._max_heapify(array=array, violated_index=i)
        return array

    def _max_heapify(self, array, violated_index):
        n = len(array)
        left_child = array[2 * violated_index + 1] if (2 * violated_index + 1) < n else MaxHeap.INT_MIN
        right_child = array[2 * violated_index + 2] if (2 * violated_index + 2) < n else MaxHeap.INT_MIN
        if left_child == right_child == MaxHeap.INT_MIN or (
                array[violated_index] >= left_child and array[violated_index] >= right_child):
            return array
        swap_index = (2 * violated_index + 1) if left_child > right_child else (2 * violated_index) + 2
        temp = array[violated_index]
        array[violated_index] = array[swap_index]
        array[swap_index] = temp
        return self._max_heapify(array=array, violated_index=swap_index)

    def _max_heapify_new(self, array, violated_index, offset):
        n = len(array)
        left, right = 2 * violated_index + 1 + offset, 2 * violated_index + 2 + offset
        left_child = array[left] if left < n else MaxHeap.INT_MIN
        right_child = array[right] if right < n else MaxHeap.INT_MIN
        if left_child == right_child == MaxHeap.INT_MIN or (
                array[violated_index] >= left_child and array[violated_index] >= right_child):
            return array
        swap_index = left if left_child > right_child else right
        temp = array[violated_index]
        array[violated_index] = array[swap_index]
        array[swap_index] = temp
        return self._max_heapify(array=array, violated_index=swap_index)

    def get_sorted_elements(self):
        sorted_elements = []
        heap_array = copy(self.heap_array)
        for _ in range(self.heap_size):
            sorted_elements.append(heap_array[0])
            heap_array[0] = heap_array[-1]
            del heap_array[-1]
            self._max_heapify(array=heap_array, violated_index=0)
        return sorted_elements

    def insert_to_heap(self, elem):
        self.heap_array.insert(0, elem)
        self._max_heapify(array=self.heap_array, violated_index=0)

    def insert_to_heap_new(self, elem):
        if self.heap_start < 0:
            # print(len(self.heap_array))
            st_time = time.time()
            new_array = [MaxHeap.INT_MIN] * self.inc_size
            new_array.extend(self.heap_array)
            # print(len(self.heap_array), len(new_array))
            self.heap_array = new_array
            self.heap_start = self.heap_start + self.inc_size
            print("Time taken to extend the heap array: {}".format(time.time() - st_time))
        # print(self.heap_start, len(self.heap_array))
        self.heap_array[self.heap_start] = elem
        # print(self.heap_start, len(self.heap_array))
        self._max_heapify_new(array=self.heap_array, violated_index=0, offset=self.heap_start)
        self.heap_start -= 1
        # print(self.heap_start, len(self.heap_array))
        # exit()

    def print_max_heap(self):
        print(self.heap_array)


if __name__ == '__main__':
    st_time = time.time()
    # mh = MaxHeap([random.randint(0, 1000000) for _ in range(10)])
    mh1 = MaxHeap()
    print("Time taken to build max heap: {}".format(time.time() - st_time))
    vals = [random.randint(0, 100000) for _ in range(1000)]
    st_time = time.time()
    for x in vals:
        mh1.insert_to_heap(elem=x)
    print("Time taken to insert 10K elements into heap using strategy I: {}".format(time.time() - st_time))
    st_time = time.time()
    mh2 = MaxHeap([MaxHeap.INT_MIN] * 1000)
    print("Time taken to build max heap: {}".format(time.time() - st_time))
    st_time = time.time()
    for x in vals:
        mh2.insert_to_heap_new(elem=x)
    print("Time taken to insert 10K elements into heap using strategy II: {}".format(time.time() - st_time))
    print(mh1.heap_array)
    print(mh2.heap_array)
    print(mh1.get_sorted_elements() == mh2.get_sorted_elements())
