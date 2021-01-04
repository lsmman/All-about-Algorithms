import sys

hex_to_bin = dict()
hex_to_bin["0"] = "0000"
hex_to_bin["1"] = "0001"
hex_to_bin["2"] = "0010"
hex_to_bin["3"] = "0011"
hex_to_bin["4"] = "0100"
hex_to_bin["5"] = "0101"
hex_to_bin["6"] = "0110"
hex_to_bin["7"] = "0111"
hex_to_bin["8"] = "1000"
hex_to_bin["9"] = "1001"
hex_to_bin["A"] = "1010"
hex_to_bin["B"] = "1011"
hex_to_bin["C"] = "1100"
hex_to_bin["D"] = "1101"
hex_to_bin["E"] = "1110"
hex_to_bin["F"] = "1111"


def change_hex_word_to_bin(hex_word):
    bin_word = ""
    for w in hex_word:
        bin_word += hex_to_bin[w]
    return bin_word


def abstract_valid_line(lines):
    valid_lines = []
    for line in lines:
        if len(set(line)) == 1 and "0" in line:
            continue
        i, move = 0, 1
        while line[i] == "0":
            i += move
        srt = i
        i, move = len(line) - 1, -1
        while line[i] == "0":
            i += move
        end = i
        valid_lines.append(line[srt : end + 1])
    return valid_lines


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


def convert_rate_code(bin_line):
    preq = "0"
    count = 0
    stack = []
    rate_val = len(bin_line) // 56
    if bin_line[0] == "1":
        bin_line = "0" + bin_line
    for l in bin_line:
        if l == preq:
            count += 1
        else:
            preq = l
            stack.append(count)
            count = 1
    if preq == "1" and count > 1:
        stack.append(count)
    print("rate_val: ", rate_val, stack)  ##########################
    return list(map(lambda x: x // rate_val, stack))


def convert_code(rate_code, num_code_dict):

    code = []
    for i in range(0, 32, 4):
        counts = rate_code[i : i + 4]
        if len(counts) != 4:
            continue
        if sum(counts[1:]) < 7:
            counts[0] = 7 - sum(counts[1:])
        try:  ######################
            code.append(num_code_dict[tuple(counts)])
        except:  ##########################
            print(i, counts, rate_code)  ########################
            return []  #########################
    return code


def check_right_safety_code(code):
    ans = 0
    sum_num = sum(code)
    check_sum = sum_num
    for i in range(0, 7, 2):
        check_sum += 2 * code[i]
    if check_sum % 10 == 0:
        ans += sum_num
    return ans


def solution(lines):
    ans = 0
    # 1. 받아오면 196EBC5A316C578 이런식으로 중요정보만 추리기
    valid_lines = abstract_valid_line(lines)
    # print(len(lines), lines)  ######################
    # print(len(valid_lines), valid_lines)  ######################
    # 2. 이진수로 변환
    # 3. 비율로 해석해서 code로 변환
    num_code_dict = get_num_code_dict()
    for line in valid_lines:
        # print(line)  #####################################
        bin_line = change_hex_word_to_bin(line)
        # print(bin_line)  ###############################
        rate_code = convert_rate_code(bin_line)
        # print(rate_code, len(rate_code))  ###############################
        code = convert_code(rate_code, num_code_dict)
        if not code:
            return 0
        # print(code, len(code))  #############################
        ans += check_right_safety_code(code)
        # print(ans)  #############################

    return ans


def main():
    sys.stdin = open("python-SWExpert/input.txt")

    T = int(input())
    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        lines = set()
        for _ in range(n):
            lines.add(str(input()))
        # if test_case == 7:  #######################
        ans = solution(lines)
        print("#{} {}".format(test_case, ans))
        # break  #########################


if __name__ == "__main__":
    main()
    # solution(["3C33C0CC0F0C3C0F3033CFCF3CFC", "19E1E19FE6781819E79F981E1E18"])

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

"""