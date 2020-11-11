
def sort_bubble(N_list):
    N = N_list[:]
    N_length = len(N)
    for loop in range(N_length-1):
        for i in range(N_length-loop-1):
            if N[i] > N[i+1]:
                N[i], N[i+1] = N[i+1], N[i]

    for v in N:
        print(v)

def answer():
    num_of_input_number = int(input())
    N_list = [0 for _ in range(num_of_input_number)]
    for idx in range(num_of_input_number):
        N_list[idx] = int(input())
        
    sort_bubble(N_list)
    

if __name__ == "__main__":
    answer()