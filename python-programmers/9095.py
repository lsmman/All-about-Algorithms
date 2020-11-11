
num_list = []
def count_of_sum(num, counts):
    for n in range(4, num+1):
        counts[n] = counts[n-1] + counts[n-2] + counts[n-3]
        
for _ in range(int(input())):
    num_list.append(int(input()))

max_ = max(num_list)
counts = [0 for _ in range(max_+1)]
counts[1] = 1
counts[2] = 2
counts[3] = 4
# counts[4] = 7

count_of_sum(max_, counts)
for n in num_list:
    print(counts[n])
# 1
# 1

# 2
'''
1, 1
2
'''

# 3
'''
1, 1, 1
1, 2
2, 1
3
'''

# 4
'''
1, 1, 1, 1
1, 1, 2
1, 2, 1
1, 3

2, 1, 1
2, 2

3, 1
'''
# 5
'''
### 1, 4
# 1, 1, 1, 1, 1
# 1, 1, 1, 2
# 1, 1, 2, 1
# 1, 2, 1, 1
# 1, 2, 2
# 1, 1, 3
# 1, 3, 1

### 2, 3
# 2, 1, 1, 1
# 2, 1, 2
# 2, 2, 1
# 2, 3

### 3, 2
# 3, 1, 1
# 3, 2
'''
# 5
'''
1, 1, 1, 1, 1
1, 1, 1, 2
1, 1, 2, 1
1, 2, 1, 1
2, 1, 1, 1
1, 1, 3
1, 3, 1
3, 1, 1
1, 2, 2
2, 1, 2
2, 2, 1
2, 3
3, 2
: 13
'''
# 1 2 3
