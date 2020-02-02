
if __name__ == "__main__":
    rided = 0
    each_rided = []
    max_count = 0
    for _ in range(10):
        line = input()
        if not line:
            break
        out_in = line.split()
        rided = rided - int(out_in[0]) + int(out_in[1])
        if max_count < rided:
            max_count = rided
    print(max_count)