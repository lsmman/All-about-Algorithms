import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class baekjoon_1298 {
    List<List<Integer>> wants;
    int n;
    boolean[] visit;
    int[] occupied;
    static final int EMPTY = 0;

    private void initVisit(){
        for (int i = 0; i <= n; i++) {
            visit[i] = false;
        }
    }

    public baekjoon_1298() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        n = Integer.parseInt(split[0]);
        int m = Integer.parseInt(split[1]);
        
        wants = new ArrayList<>(n+1);
        for (int i = 0; i <= n; i++) {
            wants.add(new ArrayList<>());
        }
        
        for (int i = 0; i < m; i++) {
            split = br.readLine().split(" ");
            wants.get(Integer.parseInt(split[0])).add(Integer.parseInt(split[1]));
        }
        
        visit = new boolean[n+1];
        initVisit();

        occupied = new int[n+1];
        for (int i = 0; i <= n; i++) {
            occupied[i] = EMPTY;
        }
    }

    public int solve() {
        for (int i = 1; i <= n; i++) {
            initVisit();
            dfs(i);
        }
//        System.out.println(Arrays.toString(occupied));
        return (int) Arrays.stream(occupied)
                .filter(value -> value != EMPTY)
                .count();
    }
    private boolean dfs(int cur){
        for (int want : wants.get(cur)) {
            if (visit[want]) continue;

            visit[want] = true;
            if (occupied[want] == EMPTY || dfs(occupied[want])){
                occupied[want] = cur;
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        baekjoon_1298 main = new baekjoon_1298();
        System.out.println(main.solve());

    }
}