  

if __name__ == "__main__":
    number_list = []
    for i in range(1, 46):
        number_list += [i] * i
        
    A, B = map(int, input().split())
    print(sum(number_list[A-1:B]))
            