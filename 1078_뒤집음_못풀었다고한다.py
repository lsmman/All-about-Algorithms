# def get_reversed_num(target):
#     num = (int)(target)
#     ten_num = 10
#     # figure = 0
#     reversed_num = 0

#     while (num > 0):
#         figure_num = num%10
#         reversed_num = (reversed_num) * ten_num + figure_num

#         num = num // ten_num
#         # figure += 1
#     return reversed_num

# def check_equal_with_target_sub_between_reversed_and_test_num(target, test):
#     reversed_num = get_reversed_num(test_num)
#     if (reversed_num + target == test_num):
#         return test_num
#     else : return -1

def reversed_baekjoon_1078(D):

    if (D%9 != 0):
        return -1

    key_num = D
    test_num = key_num + 1
    reversed_num = 0
    
    while (test_num < key_num * 3):
        reversed_num = get_reversed_num(test_num)
        if (reversed_num + key_num == test_num):
            return test_num
        else : 
            test_num = test_num + 1

    return -1

def testing():
    num_o = (int)(input())
    print(reversed_baekjoon_1078(num_o))
    # print(num_o, ":",reversed_baekjoon_1078(num_o))   

# def ten_super(target,figure):
#     super_num = 10 ** (figure-1)
#     return target * super_num

def first_try(ho):
    # highest_figure = [1,2,3,4,5,6,7,8,9]
    # lowest_figure = [1,0]
    # middle_figure = [1,2,3,4,5,6,7,8,9]
    num_list = [1,2,3,4,5,6,7,8,9]

    temp = ho
    figure_num = 0
    list_o = []
    while (temp > 0):
        temp = temp // 10
        figure_num += 1

    if (figure_num == 2):
        temp = figure_num-1
        
        for first in num_list:
            temp_num = first * (10 ** (figure_num-1))
            if first == 1:
                list_o.append(temp_num + 1)
                list_o.append(temp_num + 0)
            else :
                list_o.append(temp_num + 0)
#==============================================================

def test():

    num = 100000
    limit = 1000000000
    result_limit = 1000000
    store = 0
    list_o = []
    list_result = []
    while (num < limit):
        store = get_reversed_num(num)
        result = num-store
        if (result > 0) and result <= result_limit:
            # print(num, ",", store, ":", result, "   ", result//9)
            # sorted(list_o)
            # a =list_o.find(result)
            result_9 = result//9
            if (result % 9 != 0):print("#############################")
            if result_9 in list_o: pass
            else : 
                list_o.append(result_9)
                print(num, ",", store, ":", result, "   ", result//9)
                list_result.append(num)
        num = num+1

    print(sorted(list_o))
    print(max(list_o)*9)
    print(max(list_result))
########################################################

def get_reversed_num(target):
    num = (int)(target)
    ten_num = 10
    # figure = 0
    reversed_num = 0

    while (num > 0):
        figure_num = num%10
        reversed_num = (reversed_num) * ten_num + figure_num

        num = num // ten_num
        # figure += 1
    return reversed_num

def get_figure_num(target):
    temp = target
    figure_num = 0
    while (temp > 0):
        temp = temp // 10
        figure_num += 1 
    return figure_num

def check_equal_with_target_sub_between_reversed_and_test_num(target, test_num):
    reversed_num = get_reversed_num(test_num)
    if (reversed_num + target == test_num):
        return test_num
    else : return -1

def check_loop_method(target, loop_num_input, limit_num_input):
    result = 0
    loop_num = loop_num_input
    limit_num = limit_num_input
    while(loop_num < limit_num):
        result = check_equal_with_target_sub_between_reversed_and_test_num(target, loop_num)
        if (result == -1) :
            loop_num = loop_num + 10
        else : return result
    return -1

def reversed_baekjoon_1078_new(D):
    target = D
    if (target % 9 != 0) :
        return -1
    figure_num = get_figure_num(target)
    return_result = -1
    
    first_figure = target % 10
    if first_figure == 0:
        # 앞자리 뒷자리 1 same+2
        sub_result = reversed_baekjoon_1078_new(target // 10)
        result_format = (1 * 10 ** figure_num) + 1
        return_result = result_format + sub_result*10

    elif first_figure == 1:
        # 앞자리가 1이고 뒷자리 0 same
        # 앞자리가 10이고 뒷자리 0 same+1
        unit_figure_num = 1 * 10 ** (figure_num-1)
        first_start_num = unit_figure_num
        first_limit_num = first_start_num + unit_figure_num 
        
        second_start_num = unit_figure_num * 10
        second_limit_num = second_start_num + unit_figure_num

        third_start_num = unit_figure_num * 9
        third_limit_num = third_start_num + unit_figure_num

        return_result = check_loop_method(target, first_start_num, first_limit_num)
        if(return_result == -1):
            return_result = check_loop_method(target, second_start_num, second_limit_num)
        if(return_result == -1):
            return_result = check_loop_method(target, third_start_num, third_limit_num)
    
    elif first_figure == 9:
        # 앞자리가 10이고 뒷자리 0 same+1
        # 앞자리가 100이고 뒷자리 0 same+2
        
        unit_figure_num = 1 * 10 ** (figure_num-1)
        first_start_num = unit_figure_num * 1
        first_limit_num = first_start_num + unit_figure_num
        
        second_start_num = unit_figure_num * 10
        second_limit_num = second_start_num + unit_figure_num

        third_start_num = unit_figure_num * 100
        third_limit_num = third_start_num + unit_figure_num

        return_result = check_loop_method(target, first_start_num, first_limit_num)
        if(return_result == -1):
            return_result = check_loop_method(target, second_start_num, second_limit_num)
        if(return_result == -1):
            return_result = check_loop_method(target, third_start_num, third_limit_num)
    
    else :
    
        result_higher = 10 - first_figure
        
        # 앞자리가 result_higher이고 뒷자리 0 same
        unit_figure_num = 1 * 10 ** (figure_num-1)
        start_num = unit_figure_num * result_higher
        limit_num = start_num + unit_figure_num
        return_result = check_loop_method(target, start_num, limit_num)
        
    return return_result

if __name__ == "__main__":
    
    num_i = (int)(input())
    num_o = reversed_baekjoon_1078_new(num_i)
    print(num_o)
