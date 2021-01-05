import sys

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
decode = {
    (1, 1, 2): 0,
    (1, 2, 2): 1,
    (2, 2, 1): 2,
    (1, 1, 4): 3,
    (2, 3, 1): 4,
    (1, 3, 2): 5,
    (4, 1, 1): 6,
    (2, 1, 3): 7,
    (3, 1, 2): 8,
    (2, 1, 1): 9,
}


def exam_check_sum(code):
    check_sum = sum(code) + sum([2 * code[i] for i in [1, 3, 5, 7]])
    return check_sum % 10 == 0


def main():
    sys.stdin = open("python-SWExpert/input.txt")

    T = int(input())
    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        lines = list(set([input() for _ in range(n)]))
        valid_codes = set()
        for line in lines:
            if len(set(line)) == 1:
                continue
            binary = ""
            for word in line:
                binary += hex_to_bin[word]
            fir, sec, thr = 0, 0, 0
            code = []
            for bin_num in reversed(binary):
                if sec == 0 and thr == 0 and bin_num == "1":
                    fir += 1
                elif fir and thr == 0 and bin_num == "0":
                    sec += 1
                elif fir and sec and bin_num == "1":
                    thr += 1
                elif thr and bin_num == "0":
                    count = min(fir, sec, thr)
                    code.append(decode[(fir // count, sec // count, thr // count)])
                    fir, sec, thr = 0, 0, 0
                if len(code) == 8:
                    if exam_check_sum(code):
                        valid_codes.add(tuple(code))
                    code = []
        ans = 0
        for valid_code in valid_codes:
            ans += sum(valid_code)
        print("#{} {}".format(test_case, ans))


if __name__ == "__main__":
    main()

"""
#1 38
#2 0
#3 36
#4 36
#5 44
#6 80
#7 76
#8 72
#9 182
#10 166
#11 212
#12 192
#13 1164
#14 1196
#15 1272
#16 1584
#17 4378
#18 6908
#19 7736
#20 6604

Thanks to 'https://pg-wonie.tistory.com/27?category=830857'
"""