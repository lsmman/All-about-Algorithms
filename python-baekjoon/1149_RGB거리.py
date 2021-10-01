# RGB 거리
# https://www.acmicpc.net/problem/1149

def main():
    loop = int(input())
    arr = []
    for _ in range(loop):
        arr.append(list(map(int, input().split())))
    d = [[0 for _ in range(3)] for _ in range(loop)]
    d[0] = arr[0]
    for i in range(loop):
        for j in range(3):
            d[i][j] = min(d[i-1][(j+1)%3], d[i-1][(j+2)%3]) + arr[i][j]
    print(min(d[loop-1]))
if __name__ == "__main__":
  main()