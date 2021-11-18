import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 틀렸습니다...
public class baekjoon_5719 {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final int EDGE_LIMIT = 1001;

    private List<List<Integer>> connected;
    private int[][] edgeInfo;
    private int N;
    private int S;
    private int D;

    private void init() {
        connected = new ArrayList<>(this.N);
        for (int i = 0; i < N; i++) {
            connected.add(new ArrayList<>());
        }

        edgeInfo = new int[this.N][this.N];
        for (int i = 0; i < this.N; i++) {
            for (int j = 0; j < this.N; j++) {
                edgeInfo[i][j] = EDGE_LIMIT;
            }
        }
    }

    public boolean getInput() throws IOException {
        String[] input;
        int U, V, P;

        input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        if (N == 0 && M == 0){
            return false;
        }
        init();

        input = br.readLine().split(" ");
        S = Integer.parseInt(input[0]);
        D = Integer.parseInt(input[1]);

        for (int i = 0; i < M; i++) {
            input = br.readLine().split(" ");
            U = Integer.parseInt(input[0]);
            V = Integer.parseInt(input[1]);
            P = Integer.parseInt(input[2]);

            connected.get(U).add(V);
            edgeInfo[U][V] = P;
        }
        for (int i = 0; i < this.N; i++) {
            final int[] ints = this.edgeInfo[i];
            connected.get(i).sort(
                    Comparator.comparingInt(o -> ints[o]));
        }
        return true;
    }
    private int findShortestPath(ArrayList<String> paths){
        boolean[] nodeVisited = new boolean[this.N];
        Deque<int[]> dq = new LinkedList<>();
        int[] prevs = new int[this.N];
        int noway = this.N * EDGE_LIMIT;
        int answer = noway; // distance limit
        int[] item;
        int node, dist;

        for (int i = 0; i < this.N ; i++) {
            prevs[i] = i;
        }
        Arrays.fill(nodeVisited, false);

        dq.add(new int[] {this.S, 0});
        nodeVisited[this.S] = true;
        while (!dq.isEmpty()){
            item = dq.pollFirst();
            node = item[0];
            dist = item[1];
            if (node == this.D){
                if (paths != null){
                    StringBuilder path = new StringBuilder(node +" ");
                    int cur = node;
                    int prev = prevs[node];
                    while (cur != prev){
                        path.append(prev);
                        path.append(" ");
                        cur = prev;
                        prev = prevs[cur];
                    }
                    path.append(dist);
                    paths.add(path.toString());
                }
                answer = Math.min(answer, dist);
                continue;
            }

            for (int next : this.connected.get(node)) {
                if (nodeVisited[next]) continue;
                int[] nextInfo = {next, dist + edgeInfo[node][next]};
                if (next == this.D){
                    dq.addFirst(nextInfo);
                    prevs[next] = node;
                    continue;
                }
                dq.addLast(nextInfo);
                prevs[next] = node;
                nodeVisited[next] = true;
            }
        }
        if (answer == noway){
            answer = -1;
        }
        return answer;
    }
    public int findAlmostShortestPath() {
        ArrayList<String> paths = new ArrayList<>();

        int minDist = findShortestPath(paths);
        removeMinPathEdges(paths, minDist);

        return findShortestPath(null);
    }

    private void removeMinPathEdges(ArrayList<String> paths, int minDist) {
        int[] path;
        for (String pathStr : paths) {
            path = Arrays.stream(pathStr.split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            if (path[path.length-1] != minDist){
                continue;
            }
            for (int i = path.length-2; i > 0; i--) {
                List<Integer> nextNodes = connected.get(path[i]);
                nextNodes.remove((Integer)path[i-1]);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        baekjoon_5719 main  = new baekjoon_5719();
        boolean stop;
        int result;

        while (true){
            stop = !(main.getInput());
            if (stop){
                break;
            }
            result = main.findAlmostShortestPath();
            System.out.println(result);
        }
    }
}
