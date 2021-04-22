n = int(input())
score_info = [list(map(int, input().split())) for _ in range(n)]

# score_info = [[4, 60], [4, 40], [1, 20], [2, 50], [3, 30], [4, 10], [6, 5]]
score = 0
score_pane = [0 for _ in range(1001)]
for d, w in score_info:
    if not score_pane[d]:
        score_pane[d] = w
    else:
        while d:
            if w > score_pane[d]:
                score_pane[d], w = w, score_pane[d]
            d = d - 1
print(sum(score_pane))