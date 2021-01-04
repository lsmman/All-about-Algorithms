import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_1103 {
    static int N, M;
    static int[][] MAP, dp;
    static int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    static boolean[][][] visit;
    static int INFINITY = 100000;
    static int maxMove;

    public static void main(String[] args) throws IOException {
        maxMove = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        int i, j;
        char cur;
        String[] inputs = br.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);
        MAP = new int[N][M];
        dp = new int[N][M];
        visit = new boolean[N][M][4];

        for (i = 0; i < N; i++) {
            input = br.readLine();

            for (j = 0; j < M; j++) {
                dp[i][j] = -1;
                cur = input.charAt(j);
                if (input.charAt(j) == 'H'){
                    cur = '0';
                }
                MAP[i][j] = cur - '0';
            }

        }
        bfs(0, 0, 0);
        if (maxMove == INFINITY){
            maxMove = -1;
        }
        System.out.println(maxMove);
    }

    static void bfs(int x, int y, int move) {
        if (maxMove == INFINITY){
            return;
        }
        if (x < 0 || x >= M || y < 0 || y >= N || MAP[y][x] == 0){
            maxMove = Math.max(maxMove, move);
            return;
        }
        if (dp[y][x] >= move){
            return;
        }
        dp[y][x] = move;

        for (int i = 0; i < 4; i++) {
            if (visit[y][x][i]) {
                maxMove = INFINITY;
                break;
            }
            int dx = direction[i][0] * MAP[y][x];
            int dy = direction[i][1] * MAP[y][x];
            visit[y][x][i] = true;
            bfs(x+dx, y+dy, move+1);
            visit[y][x][i] = false;
        }
    }
}
