def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


def get_sum_of_fraction(a_b, a_m, b_b, b_m):
    A, B, C, D = 1, 1, 1, 1
    max_diviable_num = 1
    result_X = 1
    result_Y = 1

    A = a_b
    B = a_m
    C = b_b
    D = b_m

    # A/B + C/D

    X = A * D + B * C
    Y = B * D

    max_diviable_num = gcd(X, Y)

    result_X = X / max_diviable_num
    result_Y = Y / max_diviable_num

    return_val = (result_X, result_Y)
    print((int)(result_X), (int)(result_Y))
    return return_val


if __name__ == "__main__":
    a, b = input().split()
    c, d = input().split()
    A = (int)(a)
    B = (int)(b)
    C = (int)(c)
    D = (int)(d)

    result = get_sum_of_fraction(A, B, C, D)
