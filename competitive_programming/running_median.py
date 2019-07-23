from random import randint
from heapq import heappush, heappop


def insert_val(x):
    global left_heap, right_heap
    if not left_heap:
        heappush(left_heap, -x)
    elif x < -left_heap[0]:
        heappush(left_heap, -x)
    else:
        heappush(right_heap, x)


def balance_heaps():
    global left_heap, right_heap
    if len(left_heap) - len(right_heap) >= 2:
        heappush(right_heap, -heappop(left_heap))
    elif len(right_heap) - len(left_heap) >= 2:
        heappush(left_heap, -heappop(right_heap))


def get_median():
    global left_heap, right_heap
    if len(left_heap) - len(right_heap) == 1:
        return round(float(-left_heap[0]), 1)
    elif len(right_heap) - len(left_heap) == 1:
        return round(float(right_heap[0]), 1)
    elif len(left_heap) == len(right_heap):
        return round((-left_heap[0] + right_heap[0]) / 2, 1)


if __name__ == '__main__':
    left_heap, right_heap = [], []
    n = 10
    for _ in range(n):
        # val = int(input())
        val = randint(1, 100)
        insert_val(val)
        balance_heaps()
        print(get_median())
        print(left_heap)
        print(right_heap)
        print("*" * 10)
