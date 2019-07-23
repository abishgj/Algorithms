def dfs_recursion(node, g):
    print(node, end=" ")
    global visited
    if node in g:
        for v in g[node]:
            if v not in visited:
                visited.append(v)
                dfs_recursion(v, g)
    return visited


def dfs(g, N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    dfs_recursion(0, g)


if __name__ == '__main__':
    visited = []
    N = 4
    g = {0: [1, 2, 3], 2: [4]}
    dfs(g, N)
