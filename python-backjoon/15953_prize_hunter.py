## a 대회
## 1등 1, 
## 2등 2, 3
## 3등 4, 5, 6
## 4등 7,8,9,10
## 5등 11, 12, 13, 14, 15
## 6등 16, 17, 18, 19, 20, 21

## b 대회
## 1등 1, 
## 2등 2, 3
## 3등 4, 5, 6, 7
## 4등 8,91011121314 15
## 5등 16 ~ 31

def get_prize_money(a, b):
    prize_money = 0
    a_prize, b_prize = 0, 0

    a_prize_setting = [0,
        500, 
        300, 300, 
        200, 200, 200, 
        50, 50, 50, 50, 
        30, 30, 30, 30, 30, 
        10, 10, 10, 10, 10, 10
        ]

    if a > 21 or a < 1 : pass
    else :
        a_prize = a_prize_setting[a]
    
    if b > 31 or b < 1: pass
    else :
        c = 2
        n = 9
        while (b > c-1):
            c = c*2
            n = n-1
        b_prize = 2**n   
        
    prize_money = a_prize + b_prize
    return prize_money * 10000

num = int(input())
ans = [0 for _ in range(num)]
for idx in range(num):
        input_str = input()
        a, b = input_str.split(" ")
        ans[idx] = get_prize_money(int(a), int(b))
for _ in ans:
    print(_)