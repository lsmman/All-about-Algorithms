# vending machine report
###########################

#!/bin/python3
#
# Complete the 'getReport' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY checkEvents 그날 마치고 몇 개 남아있나
#  2. 2D_INTEGER_ARRAY fillEvents 얼마나 추가되나
#
from collections import defaultdict


def getReport(checkEvents, fillEvents):
    checks = defaultdict(int)
    fills = defaultdict(int)
    for day, amount in fillEvents:
        fills[day] += amount
    for day, amount in checkEvents:
        checks[day] += amount
    days = max(len(checks), len(fills))
    ans = [0 for _ in range(days)]
    remain = 0
    for day in range(days):
        ans[day] = fills[day] - checks[day] + remain
        remain = checks[day]
    return ans