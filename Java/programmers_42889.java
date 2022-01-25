import java.util.Arrays;
import java.util.Comparator;

// 11시 7분
public class programmers_42889 {
    static int LIMIT = 501;
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] dp = new int[N + 2];
        double[][] failure_ratio = new double[N+1][2];

        for (int stage : stages) {
            if (stage > N){
                stage = N+1;
            }
            dp[stage]++;
        }

        for (int i = 0; i <= N; i++) {
            failure_ratio[i][1] = i;
        }

        int tried = dp[N+1];
        double result;

        for (int i = N; i >= 1; i--) {
            tried += dp[i];
            result = 0;
            if (tried != 0){
                result = (double) dp[i] / (double) tried;
            }
            failure_ratio[i][0] = result;
        }

        Arrays.sort(failure_ratio, Comparator.comparingDouble(value -> -value[0] * Double.MAX_VALUE + value[1]));

        int index = 0;
        for (double[] doubles : failure_ratio) {
            if (doubles[1] == (double) 0){
                continue;
            }
            answer[index++] = (int) doubles[1];
        }
        return answer;
    }
    public static void main(String[] args) {
        programmers_42889 main = new programmers_42889();
        int[] solution;
        int[] answer;

        answer = new int[] {3, 4, 2, 1, 5};
        solution = main.solution(5, new int[] {2, 1, 2, 6, 2, 4, 3, 3});
        System.out.println(Arrays.toString(solution));
        System.out.println(Arrays.compare(solution, answer) == 0);

        answer = new int[] {4, 1, 2, 3};
        solution = main.solution(4, new int[] {4, 4, 4, 4, 4});
        System.out.println(Arrays.toString(solution));
        System.out.println(Arrays.compare(solution, answer) == 0);
    }
}
