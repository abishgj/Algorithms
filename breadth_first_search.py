import queue


def bfs(g, N):
    '''
    can use queue module already imported
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
    '''
    traversed_array = []
    bfs_traversal = queue.Queue(N)
    bfs_traversal.put(0)
    traversed_array.append(0)
    parent_root = {0: None}
    while not bfs_traversal.empty():
        v = bfs_traversal.get()
        if v in g:
            for each_v in g[v]:
                if each_v not in traversed_array:
                    bfs_traversal.put(each_v)
                    traversed_array.append(each_v)
                    parent_root[each_v] = v
    print(*traversed_array)


if __name__ == '__main__':
    N = 3
    g = {0: [1, 2], 1: [2], 2: [0]}
    bfs(g, N)
