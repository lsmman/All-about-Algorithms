def element_wise_add(first, second):
    return [x+y for x, y in zip(first, second)]

def fib_counter(n, fib):
    fib[0] = [1,0]
    fib[1] = [0,1]
    for num in range(2, n+1):
        fib[num] = element_wise_add(fib[num-1], fib[num-2])

num_list = []
for _ in range(int(input())):
    num_list.append(int(input()))

fib = [[0,0] for _ in range(41)]
fib_counter(40)
for n in num_list:
    print(fib[n])
    

# def fib_lsh(n):
#     fib = [[0,0] for _ in range(41)]
#     fib[0] = [1,0]
#     fib[1] = [0,1]
#     def fib_cal_down_to_up(n, fib):
#         if n == 0:
            
#         return fib[n-1] + fib[n-2]

# # print(fib[0])
# # print(fib[1])

# ## ================================
# ## test code
# # def fibonacci(n):
# #     if (n==0):
# #         print("0")
# #         return 0
# #     elif (n==1):
# #         print("1")
# #         return 1
# #     else :
# #         return fibonacci(n-1) + fibonacci(n-2)

# # def fibonacci_global_variable(n):
# #     global s0
# #     global s1
# #     if (n==0):
# #         s0 = s0+1
# #         return 0
# #     elif (n==1):
# #         s1 = s1+1
# #         return 1
# #     else :
# #         return fibonacci_global_variable(n-1) + fibonacci_global_variable(n-2)

# # global s0
# # global s1
# # s0 = 0
# # s1 = 0    
# # f = fibonacci_global_variable(40)
# # print(f)
# # print(s0, s1)


# def fibonacci_with_dynamic_counter(n):
    
#     def add_by_list_element(list_x, list_y):
#         return [list_x[0] + list_y[0], list_x[1] + list_y[1]]
#     def fibonacci_global_variable(n, now, fib_save_list):
#         if (now == n+1):
#             return
#         else : 
#             fib_save_list[now] = add_by_list_element(fib_save_list[now-1], fib_save_list[now-2])
#             return fibonacci_global_variable(n, now+1, fib_save_list)
    

#     if (n == 0):
#         answer = [1, 0]
#     elif (n == 1):
#         answer = [0, 1]
#     else :         
#         fib_save_list = [[0,0] for _ in range(n+1)]
#         fib_save_list[0] = [1,0]
#         fib_save_list[1] = [0,1]
        
#         fibonacci_global_variable(n, 2, fib_save_list)
#         answer =  fib_save_list[n]    
    
#     print(answer[0], answer[1])


# if __name__ == "__main__":
#     for _ in range(int(input())):
#         fibonacci_with_dynamic_counter(int(input()))

# # c0=[1,0,1]
# # c1=[0,1,1]

# # def fibo(n):#6
# #     l=len(c0)#3
# #     if l<=n:
# #         for i in range(l,n+1):
# #             c0.append(c0[i-1]+c0[i-2])
# #             c1.append(c1[i-1]+c1[i-2])
# #     print('%d %d'%(c0[n],c1[n]))
# # for _ in range(int(input())):
# #     fibo(int(input()))