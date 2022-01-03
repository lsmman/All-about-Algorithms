import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class baekjoon_1516 {
    public static void main(String[] args) throws IOException {
        String[] split;
        int i, j;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<List<Integer>> products = new ArrayList<>();
        int[] costs = new int[n];
        int[] minCosts = new int[n];

        for (i = 0; i < n; i++) {
            minCosts[i] = -1;
        }
        for (i = 0; i < n; i++) {
            products.add(new ArrayList<>());
            split = br.readLine().split(" ");
            costs[i] = Integer.parseInt(split[0]);

            for (j = 1; j < split.length-1; j++){
                products.get(i).add(Integer.parseInt(split[j])-1);
            }
        }

        for (i = 0; i < n; i++) {
            products.get(i).sort(Comparator.reverseOrder());
        }

        for (i = 0; i < n; i++) {
            calc(i, products, costs, minCosts);
        }

        for (i = 0; i < n; i++) {
            System.out.println(minCosts[i]);
        }
    }

    static void calc(int i, List<List<Integer>> products, int[] costs, int[] minCosts) {
        int cost = 0;
        for (int p : products.get(i)) {
            if (minCosts[p] == -1) calc(p, products, costs, minCosts);
            cost = Math.max(minCosts[p], cost);
        }
        minCosts[i] = costs[i] + cost;
    }
}
