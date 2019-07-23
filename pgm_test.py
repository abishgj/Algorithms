from random import randint
from heapq import heappush, heappop


def f1():
    print("f1: {}".format(a))


def f2():
    global a
    heappush(a, randint(10, 100))
    print("f2: {}".format(a))


if __name__ == '__main__':
    a = [1, 2]
    for _ in range(10):
        f1()
        f2()
        print(a)
        print("*" * 10)
