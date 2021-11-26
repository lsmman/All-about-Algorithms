    
import heapq

N, target = map(int, input().split())
primes = list(map(int, input().split()))

q = list(primes)
heapq.heapify(q)

for _ in range(target):
    cur = heapq.heappop(q)
    for p in primes:
        heapq.heappush(q, cur*p)
        if cur % p == 0:
            break
print(cur)
