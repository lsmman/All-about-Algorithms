import java.util.Scanner;

public class baekjoon_13913 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] s = sc.nextLine().split(" ");
        sc.close();
        int n = Integer.parseInt(s[0]);
        int k = Integer.parseInt(s[1]);

        solve(n, k);
    }

    private static int solve(int n, int k) {
        int[][] dp;
        boolean[] visit = new boolean[200001];

        for (int i = 0; i < 200001; i++) {
            visit[i] = false;
        }

        if (n >= k) {
            StringBuilder builder = new StringBuilder();
            for (int i = n; i >= k; i--){
                builder.append(i + " ");
            }
            System.out.println(n - k);
            System.out.println(builder.toString());
            return n - k;
        }

        dp = new int[2 * k + 1][2];

        dp[n][0] = 0;
        dp[n][1] = n;

        for (int i = n-1; i >= 0; i--) {
            dp[i][0] = n-i;
            dp[i][1] = i+1;
        }
        for (int i = n+1; i <= 2 * k; i++){
            dp[i][0] = i-n;
            dp[i][1] = i-1;
        }

        for (int nowNum = Math.max(n / 2, 1); nowNum < k; nowNum++){
            search(dp, k, nowNum, visit);
        }

        int move = dp[k][0];
        String[] answer = new String[move+1];
        answer[move] = Integer.toString(k);
        int nextInt = k;
        while (nextInt != n){
            move--;
            nextInt = dp[nextInt][1];
            answer[move] = Integer.toString(nextInt);
        }
        System.out.println(dp[k][0]);
        System.out.println(String.join(" ", answer) + " ");

        return dp[k][0];
    }

    private static void search(int[][] dp, int k, int nowNum, boolean[] visit) {
        int subtractOne;
        int addOne;
        int doubleNum;
        int lastMove = dp[nowNum][0];

        visit[nowNum] = true;

        addOne = nowNum + 1;
        if (addOne <= 2 * k && dp[addOne][0] > lastMove +1){
            dp[addOne][0] = lastMove +1;
            dp[addOne][1] = nowNum;
        }

        subtractOne = nowNum - 1;
        if (dp[subtractOne][0] > lastMove +1){
            dp[subtractOne][0] = lastMove +1;
            dp[subtractOne][1] = nowNum;
            if (visit[subtractOne]){
                search(dp, k, subtractOne, visit);
            }
        }

        doubleNum = nowNum * 2;
        if (doubleNum <= 2 * k && dp[doubleNum][0] > lastMove +1){
            dp[doubleNum][0] = lastMove + 1;
            dp[doubleNum][1] = nowNum;
            if (visit[subtractOne]){
                search(dp, k, doubleNum, visit);
            }
        }
    }
}
