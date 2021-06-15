import collections
import math


class Solution:
    def nCr(self, n, r):
        f = math.factorial
        return f(n) / f(r) / f(n - r)

    def waysToBuildRooms(self, arr):
        MOD = 10 ** 9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(arr):
            g[pre].append(cur)
        print(g)

        def dfs(cur):
            if not g[cur]:
                return 1, 1
            ans, l = 1, 0
            for nxt in g[cur]:
                tmp, r = dfs(nxt)
                ans = (ans * tmp * self.nCr(l + r, r)) % MOD
                l += r
            return ans, l + 1

        return dfs(0)[0]


# class Solution:

#     def waysToBuildRooms(self, prevRoom: List[int]) -> int:
#         n = len(prevRoom)
#         self.cnt = 0

#         connected = [set() for _ in range(n)]
#         srt = 0


#         def dfs(reachable, visited, visit_cnt):
#             if visit_cnt == n:
#                 self.cnt += 1
#             for i in reachable:
#                 if not visited[i]:
#                     visited[i] = True
#                     dfs(reachable|connected[i], visited, visit_cnt+1)
#                     visited[i] = False

#         for i, p in enumerate(prevRoom[1:]):
#             i = i+1
#             connected[i].add(p)
#             connected[p].add(i)

#         reachable = connected[srt].copy()
#         visited = [False] * n
#         visited[srt] = True

#         dfs(reachable, visited, 1)

#         return self.cnt

import unittest


class testcases(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().waysToBuildRooms([-1, 0, 1]), 1)


unittest.main()