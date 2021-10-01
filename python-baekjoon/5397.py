from collections import deque

def hack_password(input_str):
    left = list()
    right = deque()
    
    for s in input_str:
        if s == "<":
            if not left:
                continue
            right.appendleft(left.pop())
        elif s == ">":
            if not right:
                continue
            left.append(right.popleft())
        elif s == "-":
            if not left:
                continue
            left.pop()
        else:
            left.append(s)

    return "".join(left) + "".join(right)

def main():
    T = int(input())
    inputs = []
    for tc in range(T):
        inputs.append(input())

    for input_str in inputs:
        result = hack_password(input_str)
        print(result)

# main()

import unittest

class testcase(unittest.TestCase):
    def test1(self):
        self.assertEqual(hack_password("ThIsIsS3Cr3t"), "ThIsIsS3Cr3t")
    def test2(self):
        self.assertEqual(hack_password("<<BP<A>>Cd-"), "BAPC")
    def test3(self):
        msg = "f<->--><-l>>d---u-j><>-<u->xb<<axkh<-wk>k>--t--s<b<i<ir>--ey>t>>sx<-yb<>jw<-qaruwy<osnshf><<<-uzz--<"
        print(hack_password(msg))
        self.assertEqual(hack_password(msg), "axwkieybtsbybqaruwosnuhfywx")
    def test4(self):
        msg = "f<->--><-l>>d---u-j><>-<u->xb<<a"
        print(hack_password(msg))
        self.assertEqual(hack_password(msg), "axb")
    def test5(self):
        msg = "j><>-<u->xb<<a"
        print(hack_password(msg))
        self.assertEqual(hack_password(msg), "axb")
    def test6(self):
        msg = "a><><b"
        print(hack_password(msg))
        self.assertEqual(hack_password(msg), "ba")

unittest.main()
