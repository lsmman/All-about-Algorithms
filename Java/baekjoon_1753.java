import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class baekjoon_1753 {
    public static final int INF = 10 * 20000 + 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs;
        int n, numOfEdges, srt;
        int u, v, w;
        int[] dist;
        boolean[] visit;
        List<List<ToAndWeight>> edges;

        inputs = br.readLine().split(" ");
        n = Integer.parseInt(inputs[0]) + 1;
        numOfEdges = Integer.parseInt(inputs[1]);
        srt = Integer.parseInt(br.readLine());
        dist = new int[n];
        visit = new boolean[n];
        edges = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            edges.add(new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            dist[i] = INF;
            visit[i] = false;
        }
        dist[srt] = 0;

        for (int i = 0; i < numOfEdges; i++) {
            inputs = br.readLine().split(" ");
            u = Integer.parseInt(inputs[0]);
            v = Integer.parseInt(inputs[1]);
            w = Integer.parseInt(inputs[2]);

            edges.get(u).add(new ToAndWeight(v, w));
        }

        int via;
        for (int i = 1; i < n; i++) {
            via = findMinIndex(n, dist, visit);
            visit[via] = true;

            if (dist[via] == INF) {
                continue;
            }
            // srt - via - target
            for (ToAndWeight toAndWeight : edges.get(via)) {
                int to = toAndWeight.to;
                int weight = toAndWeight.weight;
                dist[to] = Math.min(dist[to], dist[via] + weight);
            }

        }
        for (int i = 1; i < n; i++) {
            if (dist[i] == INF) {
                System.out.println("INF");
            } else {
                System.out.println(dist[i]);
            }
        }
    }

    private static int findMinIndex(int n, int[] dist, boolean[] visit) {
        int minVal = INF;
        int minIdx = 0;
        for (int i = 1; i < n; i++) {
            if (visit[i]) {
                continue;
            }
            if (minVal > dist[i]) {
                minIdx = i;
                minVal = dist[i];
            }
        }
        return minIdx;
    }

    static class ToAndWeight {
        public int to, weight;

        public ToAndWeight(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }
}
