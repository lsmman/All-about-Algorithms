from collections import defaultdict

T = int(input())
inputs = map(int, input().split())

answer = [0] * T
d = defaultdict(list)
for i, n in enumerate(inputs):
    d[n].append(i)

keys = list(d.keys())
for i, k in enumerate(sorted(keys)):
    for idx in d[k]:
        answer[idx] = i
for a in answer:
    print(a, end=' ')
print()
