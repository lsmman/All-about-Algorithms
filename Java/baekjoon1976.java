import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class baekjoon1976 {

    public static void  main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        baekjoon1976 main = new baekjoon1976(n);

        int[][] conn = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] inputsStr = br.readLine().split(" ");;
            for (int j = 0; j < n; j++) {
                conn[i][j] = Integer.parseInt(inputsStr[j]);
            }
        }
        int[] plan = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        String answer = "NO";
        if (main.isPlanValid(conn, plan)){
            answer = "YES";
        }
        System.out.println(answer);
    }

    int[] parents;
    int n;

    public baekjoon1976(int n) {
        this.n = n;
        this.parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
    }

    private boolean isPlanValid(int[][] conn, int[] plan) {
        int pa, pb;
        for (int a = 0; a < n; a++) {
            for (int b = a+1; b < n; b++) {
                if (conn[a][b] == 0){
                    continue;
                }
                pa = find(a);
                pb = find(b);
                parents[pb] = pa;
            }
        }
        for (int i = 0; i < n; i++) {
            find(i);
        }
        int parent = parents[plan[0]-1];
        for (int p : plan) {
            if (parent != parents[p-1]){
                return false;
            }
        }
        return true;
    }

    private int find(int node) {
        if (parents[node] == node){
            return node;
        }
        parents[node] = find(parents[node]);
        return parents[node];
    }
}
