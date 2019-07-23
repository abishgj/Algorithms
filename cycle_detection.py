def detect_cycle(node, g, visit_array, recur_stack):
    visit_array[node] = True
    recur_stack[node] = True

    if node in g:
        for v in g[node]:
            if visit_array[v]:
                return True
            else:
                visit_array[v] = True
                if detect_cycle(v, g, visit_array):
                    return True


def is_cyclic(n, graph):
    visit = [False] * n
    recursion_stack = [False] * n
    for i in range(n):
        cycle = detect_cycle(i, graph, visit, recursion_stack)
        print(visit, cycle)


if __name__ == '__main__':
    n = 4
    g = {0: [1], 2: [3], 3: [2]}
    print(is_cyclic(n, g))
