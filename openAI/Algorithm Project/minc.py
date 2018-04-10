from collections import deque

def ford_fulkerson(n, s, t, c):
    '''
    n: number of nodes
    s: start node
    t: target node
    c: capacity matrix
    '''
    INF = 1 << 50
    max_flow = 0


    f = [[0 for k in range(n)] for i in range(n)]

    # while there is a path from s to t in the residual graph
    while True:
        # Use BFS to find s-t path in residual graph
        prev = [ -1 for _ in range(n) ]
        prev[s] = -2
        q = deque()
        q.append(s)

        while q and prev[t] == -1:
            u = q.popleft()
            for v in range(n):
                cf = c[u][v] - f[u][v]
                if cf > 0 and prev[v] == -1:
                    q.append(v)
                    prev[v] = u

        if prev[t] == -1:   # if t has not been reached
            break

        # augment s-t path in residual graph that has been found by BFS
        v = t
        delta = INF
        while True:
            u = prev[v]
            cf = c[u][v] - f[u][v]
            delta = min(delta, cf)
            v = u
            if v == s:
                break

        v = t
        while True:
            u = prev[v]
            f[u][v] += delta
            f[v][u] -= delta
            v = u
            if v == s:
                break

        max_flow += delta

    return max_flow


def readGraphFromFile(filename):
    file = open(filename).read().split()
#     print(file[0:4])
    counter = 0
    node_number, edge_number, s, t = map(int, file[0:4])
    file = open(filename)

    capacity_matrix = [[0 for k in range(node_number)] for i in range(node_number)]

    for line in file:
        if counter > 0 :
            line = line.split()
            u, v, c = [int(x) for x in line]
            capacity_matrix[u-1][v-1] = c
        counter = counter + 1

    # capacity_matrix = [[0 for x in range(3)] for x in range(edge_number)]
    #
    # for i in range(edge_number):
    #
    #         capacity_matrix[i-1][j-1] = int(my_matrix[i][j])

    return (node_number, s, t, capacity_matrix )


def main():
    node_number, s, t, capacity_matrix = readGraphFromFile('fulkerson.txt')
    print(node_number, s, t, capacity_matrix)
    mincut = ford_fulkerson(node_number, s - 1, t - 1, capacity_matrix )
    print('Min cut by Ford-Fulkerson Algorithm is {0}'.format(mincut))

if __name__ == '__main__':
    main()
