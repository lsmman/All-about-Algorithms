N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

for layer in range(N-1, 0, -1):
    d = data[layer]
    for i in range(layer):
        data[layer-1][i] += max(d[i], d[i+1])
print(data[0][0])

""" input

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

"""