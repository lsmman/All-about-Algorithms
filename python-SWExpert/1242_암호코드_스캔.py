import sys


def get_dict_of_hex_to_bin():
    d = dict()
    d["0"] = "0000"
    d["1"] = "0001"
    d["2"] = "0010"
    d["3"] = "0011"
    d["4"] = "0100"
    d["5"] = "0101"
    d["6"] = "0110"
    d["7"] = "0111"
    d["8"] = "1000"
    d["9"] = "1001"
    d["A"] = "1010"
    d["B"] = "1011"
    d["C"] = "1100"
    d["D"] = "1101"
    d["E"] = "1110"
    d["F"] = "1111"
    return d


def convert_code(line, hex_to_bin):
    # 0000000068B46DDB9346F40000
    a = ""
    print(len(line))
    for word in line:
        a += hex_to_bin[word]
    print(a)
    return line


def check_right_safety_code(code):
    return 0


def solution(m, lines):
    ans = 0
    hex_to_bin = get_dict_of_hex_to_bin()
    for line in lines:
        code = convert_code(line, hex_to_bin)
        ans += check_right_safety_code(code)
    return ans


def main():
    sys.stdin = open("python-SWExpert/input.txt")

    T = int(input())
    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        lines = set()
        for _ in range(n):
            lines.add(str(input()))
        ans = solution(m, lines)
        print("#{} {}".format(test_case, ans))
        break


if __name__ == "__main__":
    main()
