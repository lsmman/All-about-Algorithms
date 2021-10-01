def fibonacci_with_dynamic_counter(n):
    def add_by_list_element(list_x, list_y):
        return [list_x[0] + list_y[0], list_x[1] + list_y[1]]

    def fibonacci_global_variable(n, now, fib_save_list):
        if now == n + 1:
            return
        else:
            fib_save_list[now] = add_by_list_element(fib_save_list[now - 1], fib_save_list[now - 2])
            return fibonacci_global_variable(n, now + 1, fib_save_list)

    if n == 0:
        answer = [1, 0]
    elif n == 1:
        answer = [0, 1]
    else:
        fib_save_list = [[0, 0] for _ in range(n + 1)]
        fib_save_list[0] = [1, 0]
        fib_save_list[1] = [0, 1]

        fibonacci_global_variable(n, 2, fib_save_list)
        answer = fib_save_list[n]

    print(answer[0], answer[1])


if __name__ == "__main__":
    for _ in range(int(input())):
        fibonacci_with_dynamic_counter(int(input()))
