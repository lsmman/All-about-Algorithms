num_list = []
n = int(input())
for _ in range(n):
    num_list.append(int(input()))

d = [0] * (n+2)
p = [0] + num_list + [0]
d[1] = p[1]
d[2] = p[1] + p[2]
for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2] + p[i], d[i-3]+p[i-1]+p[i])

# for 