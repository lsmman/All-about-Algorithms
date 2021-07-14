# Min, Max를 관리하는 DeHeapQ 구현
# doubly linked list를 활용한 queue를 사용
# binary search를 사용해 push(item) 구현

from collections import deque


class DeHeapQ:
    def __init__(self):
        self.dq = deque()
        self._length = 0

    def push(self, item):
        if self.isEmpty():
            self.dq.append(item)
            self._length += 1
            return
        low = 0
        high = self._length - 1
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if item < self.dq[mid]:
                high = mid - 1
            elif item > self.dq[mid]:
                low = mid + 1
            else:
                low = mid
                break
        self.dq.insert(low, item)
        self._length += 1

    def popMin(self):
        if self.isEmpty():
            return -1
        self._length -= 1
        return self.dq.popleft()

    def popMax(self):
        if self.isEmpty():
            return -1
        self._length -= 1
        return self.dq.pop()

    def getMaxMin(self):
        if self.isEmpty():
            return [0, 0]
        return [self.dq[-1], self.dq[0]]

    def isEmpty(self):
        return self._length == 0

    def toList(self):
        return list(self.dq)


def solution(operations):
    deHeapQ = DeHeapQ()
    for o in operations:
        if o == "D 1":
            deHeapQ.popMax()
        elif o == "D -1":
            deHeapQ.popMin()
        else:
            I, item = o.split()
            deHeapQ.push(int(item))
    return deHeapQ.getMaxMin()


import unittest


class test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(solution(["I 16", "D 1"]), [0, 0])
        self.assertEqual(solution(["I 7", "I 5", "I -5", "D -1"]), [7, 5])


unittest.main()
