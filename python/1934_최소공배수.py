# 유클리드 호제법 사용
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

def lcm(a, b):
    gcd_num = gcd(a, b)
    # return gcd_num * a/gcd_num * b/gcd_num
    return a * b // gcd_num

def lcm_print(a, b):
    print(lcm(a, b))

def answer():
    for _ in range(int(input())):
        input_str = input()
        a, b = input_str.split(" ")
        lcm_print(int(a), int(b))

answer()