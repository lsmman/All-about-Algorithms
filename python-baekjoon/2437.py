N = int(input())
query = list(map(int, input().split()))
query.sort()
cul = 0
for q in query:
    if cul + 1 < q:
        break
    cul += q
print(cul+1)