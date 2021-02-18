q = 99999
def floydWarshall(graph,n): 
    dist=graph
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
        for i in range(n):
            print(dist[i])
        print("\n")
    return dist

g = [[0,q,q,1,q,q],
[q,0,1,q,q,q],
[2,q,0,3,q,q],
[q,q,4,0,q,2],
[q,2,5,q,0,q],
[q,q,q,q,1,0]]
floydWarshall(g, 6)
