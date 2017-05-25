n=int(input("Enter the number of vertices : "))
global u,v
cost = [[0 for x in range(n+1)] for x in range(n+1)]
parent = [0 for x in range(n+1)]
mincost = 0
def find(i):
    while parent[i]:
        i = parent[i]
    return i
def uni(i,j) :
    if i!=j :
        parent[j] = i
        return 1
    return 0
for i in range(1,n+1):
    print("Cost Matrix for Vertex", i)
    for j in range(1,n+1):
        cost[i][j] = int(input())
        if cost[i][j] == 0:
            cost[i][j] = 999
ne=1
print(cost)
while(ne<n):
    min1 = 999
    for i in range(1,n+1):
        for j in range(i, n+1):
            if cost[i][j]<min1:
                min1=cost[i][j]
                u = a = i
                v = b = j
    u = find(u)
    v = find(v)
    if uni(u, v):
        print(ne, "edge(", a, ",", b, ") = ", min1)
        ne += 1
        mincost += min1
    cost[a][b] = cost[b][a]=999
print("Mincost = ", mincost)
