import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class baekjoon_2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);

        int[] trees = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int left, mid, right;
        long gainedTree;
        int answer = 0;

        left = 0;
        right = Arrays.stream(trees).max().getAsInt();
        while (left <= right){
            mid = (left + right) / 2;
            gainedTree = getSlicedTree(trees, mid);
            if (gainedTree >= m){
                answer = Math.max(mid, answer);
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        System.out.println(answer);
    }

    private static long getSlicedTree(int[] trees, int mid) {
        long result = 0;
        for (int tree : trees) {
            result += Math.max(tree - mid, 0);
        }
        return result;
    }
}
