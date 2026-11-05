# Floyd-Warshall Algorithm

INF = float('inf')


def floyd_warshall(graph):
    n = len(graph)

    # Copy the graph
    distance = [row[:] for row in graph]

    # Consider each vertex as an intermediate vertex
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


# Graph represented as an adjacency matrix
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

result = floyd_warshall(graph)

print("Shortest distances between all pairs of vertices:")

for row in result:
    for value in row:
        if value == INF:
            print("INF", end="\t")
        else:
            print(value, end="\t")
    print()