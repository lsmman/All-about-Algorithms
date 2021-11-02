/*

백준 1774
최소 신장 트리 + union find

 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

class Node {
    int a;
    int b;
    double dist;

    public Node(int a, int b, double dist) {
        this.a = a;
        this.b = b;
        this.dist = dist;
    }
}

public class baekjoon_1774 {
    private double get_distance(int[] xy1, int[] xy2){
        long distX = (xy1[0] - xy2[0]);
        long distY = (xy1[1] - xy2[1]);

        return Math.sqrt(distX * distX + distY * distY);
    }

    private int find(int node, int[] parents){
        if (node == parents[node]){
            return node;
        }
        parents[node] = find(parents[node], parents);
        return parents[node];
    }

    private void union(int a, int b, int[] parents){
        a = find(a, parents);
        b = find(b, parents);

        if (a != b){
            parents[b] = a;
        }
    }

    public String MST(int n, int m, int[][] xys, int[][] edges) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingDouble(o -> o.dist));
        int i, j, a, b;
        double distance;
        double answer = 0;
        int[] parents = new int[n];

        for (i = 0; i < n; i++) {
            parents[i] = i;
        }

        for (i = 0; i < n; i++) {
            for (j = i+1; j < n; j++) {
                distance = get_distance(xys[i], xys[j]);
                pq.offer(new Node(i, j, distance));
            }
        }

        for (i = 0; i < m; i++) {
            a = edges[i][0] - 1;
            b = edges[i][1] - 1;
            union(a, b, parents);
        }

        Node cur;
        while (!(pq.isEmpty())){
            cur = pq.poll();
            a = find(cur.a, parents);
            b = find(cur.b, parents);

            if (a == b) continue;

            union(a, b, parents);
            answer += cur.dist;
        }

        return String.format("%.2f", answer);
    }


    public static void main(String[] args) throws IOException {
//        new Main().test();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        baekjoon_1774 baekjoon_1774 = new baekjoon_1774();
        String s;
        String[] split;
        int N, M, i;
        int[][] xys, edges;
        String answer;

        s = br.readLine();
        split = s.split(" ");
        N = Integer.parseInt(split[0]);
        M = Integer.parseInt(split[1]);

        xys = new int[N][2];
        for (i = 0; i < N; i++) {
            s = br.readLine();
            split = s.split(" ");
            xys[i][0] = Integer.parseInt(split[0]);
            xys[i][1] = Integer.parseInt(split[1]);
        }

        edges = new int[M][2];
        for (i = 0; i < M; i++) {
            s = br.readLine();
            split = s.split(" ");
            edges[i][0] = Integer.parseInt(split[0]);
            edges[i][1] = Integer.parseInt(split[1]);
        }

        answer = baekjoon_1774.MST(N, M, xys, edges);
        System.out.println(answer);
    }

    private void test(){
        String expected = "4.00";
        int N = 4;
        int M = 1;

        int[][] xys = new int[N][2];
        xys[0][0] = 1;
        xys[0][1] = 1;
        xys[1][0] = 3;
        xys[1][1] = 1;
        xys[2][0] = 2;
        xys[2][1] = 3;
        xys[3][0] = 4;
        xys[3][1] = 3;

        int[][] edges = new int[M][2];
        edges[0][0] = 1;
        edges[0][1] = 4;

        String mst = MST(N, M, xys, edges);
        System.out.println(mst + " " + mst.compareTo(expected));
    }


}
