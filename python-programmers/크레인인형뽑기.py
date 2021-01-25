def solution(board, moves):
    def search_top_idx(board):
        num_of_lines = len(board[0])
        idx_list = [len(board)] * num_of_lines
        end_checker = [False] * num_of_lines
        for col_num, col in enumerate(board):
            for i in range(num_of_lines):
                if not end_checker[i] and col[i]:
                    idx_list[i] = col_num
                    end_checker[i] = True
        return idx_list

    answer = 0
    pocket = []
    bottom_idx = len(board)
    top_idx_nums = search_top_idx(board)
    for m in moves:
        loc = m - 1
        if top_idx_nums[loc] is bottom_idx:
            pass
        else:
            picking = board[top_idx_nums[loc]][loc]
            top_idx_nums[loc] += 1

            if pocket and pocket[-1] is picking:
                pocket.pop()
                answer += 2
            else:
                pocket.append(picking)
    return answer