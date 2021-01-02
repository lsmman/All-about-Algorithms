import sys


def get_dict_of_hex_to_bin():
    d = dict()
    d["0"] = ""
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


def get_num_code_dict():
    d = dict()
    d[(3, 2, 1, 1)] = 0
    d[(2, 2, 2, 1)] = 1
    d[(2, 1, 2, 2)] = 2
    d[(1, 4, 1, 1)] = 3
    d[(1, 1, 3, 2)] = 4
    d[(1, 2, 3, 1)] = 5
    d[(1, 1, 1, 4)] = 6
    d[(1, 3, 1, 2)] = 7
    d[(1, 2, 1, 3)] = 8
    d[(3, 1, 1, 2)] = 9
    return d


def convert_code(line, hex_to_bin, num_code_dict):
    # 0000000068B46DDB9346F40000
    word = ""
    for l in line:
        word += hex_to_bin[l]
    preq = "0"
    count = 0
    stack = []

    for w in word:
        if w == preq:
            count += 1
        else:
            preq = w
            stack.append(count)
            count = 1
    if preq:
        stack.append(count)

    code = []
    rate = int(round(len(line) / 14))
    for i in range(0, len(stack), 4):
        code_num = tuple(map(lambda x: x // rate, stack[i : i + 4]))
        if code_num in num_code_dict:
            code.append(num_code_dict[code_num]])
    return code


def check_right_safety_code(code):
    ans = 0
    for i in range(0, len(code), 8):
        id_num = code[i : i + 8]
        sum_num = sum(id_num)
        for num in id_num[:7]:
            if num % 2:
                sum_num += 2 * num
        print(sum_num)
        if sum_num % 10 == 0:
            ans += sum(id_num)

    return ans


def solution(m, lines):
    ans = 0
    hex_to_bin = get_dict_of_hex_to_bin()
    num_code_dict = get_num_code_dict()
    for line in lines:
        code = convert_code(line, hex_to_bin, num_code_dict)
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
    # main()
    print(solution(2, lines=["328D1AF6E4C9BB", "196EBC5A316C578"]))
