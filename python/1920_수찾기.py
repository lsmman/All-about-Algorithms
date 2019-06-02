def read_input_n_return_int_list():
    num_of_int = int(input())
    input_int_list = [0 for _ in range(num_of_int)]
    receive_input_list = input().split(" ")
    for int_idx in range(num_of_int):
        input_int_list[int_idx] = int(receive_input_list[int_idx])
    return num_of_int, input_int_list

def find_number():
    exist_num_of_int, exist_list = read_input_n_return_int_list()
    find_num_of_int, find_list = read_input_n_return_int_list()

    max_exist_num = max(exist_list)
    number_list = [0 for _ in range(max_exist_num+1)]
    result_find = [0 for _ in range(find_num_of_int)]

    for exist_now_int in exist_list:
        number_list[exist_now_int] = 1
    for idx in range(find_num_of_int):
        if max_exist_num < find_list[idx]:
            pass
        elif (number_list[find_list[idx]] == 1):
            result_find[idx] = 1
    for result in result_find:
        print(result)

def answer():
    find_number()
    
answer()