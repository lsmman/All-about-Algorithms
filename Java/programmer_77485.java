
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
class Solution {
    private static int INF;

    private int get_min_num(int[] query, int[][] MAP){
        int x1, y1, x2, y2;
        int x, y;
        int min_num = INF;

        x1 = query[1]-1;
        y1 = query[0]-1;
        x2 = query[3]-1;
        y2 = query[2]-1;

        y = y1;
        for (x = x1+1; x <= x2; x++){          
            min_num = Math.min(min_num, MAP[y][x]);
        }

        x = x2;
        for (y = y1+1; y <= y2; y++){
            min_num = Math.min(min_num, MAP[y][x]);
        }

        y = y2;
        for (x = x2-1; x >= x1; x--){
            min_num = Math.min(min_num, MAP[y][x]);
        }

        x = x1;
        for (y = y2-1; y >= y1; y--){
            min_num = Math.min(min_num, MAP[y][x]);
        }
        return min_num;
    }

    private void rotate(int[] query, int[][] MAP){
        int x1, y1, x2, y2;
        int x, y, preq, temp;

        x1 = query[1]-1;
        y1 = query[0]-1;
        x2 = query[3]-1;
        y2 = query[2]-1;
        preq = MAP[y1][x1];

        y = y1;
        for (x = x1+1; x <= x2; x++){          
            temp = MAP[y][x];
            MAP[y][x] = preq;
            preq = temp;
        }

        x = x2;
        for (y = y1+1; y <= y2; y++){
            temp = MAP[y][x];
            MAP[y][x] = preq;
            preq = temp;
        }

        y = y2;
        for (x = x2-1; x >= x1; x--){
            temp = MAP[y][x];
            MAP[y][x] = preq;
            preq = temp;
        }

        x = x1;
        for (y = y2-1; y >= y1; y--){
            temp = MAP[y][x];
            MAP[y][x] = preq;
            preq = temp;
        }
    }

    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] MAP = new int[rows][columns];
        int num;

        INF = rows * columns + 1;
        for (int r = 0; r < rows; r++){
            num = r * columns + 1;
            for (int c = 0; c < columns; c++){
                MAP[r][c] = num + c;
            }
        }

        for (int i = 0; i < queries.length; i++){
            rotate(queries[i], MAP);
            answer[i] = get_min_num(queries[i], MAP);
        }

        return answer;
    }
}