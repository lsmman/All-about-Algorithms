import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Solution_9184 {
    private static final int NONACTIVE = 0;

    private int[][][] dp;
    ArrayList<ArrayList<Integer>> inputList;

    private int w(int a, int b, int c){
        if (a <= 0 || b <= 0 || c <= 0){
            return 1;
        }

        if (dp[a][b][c] != Main.NONACTIVE){
            return dp[a][b][c];
        }

        int result;

        if (a > 20 || b > 20 || c > 20){
            result = w(20, 20, 20);
        }

        else if (a < b && b < c) {
            result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
        }

        else {
            result = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
        }

        dp[a][b][c] = result;
        return result;
    }

    public ArrayList<ArrayList<Integer>> getInput(){
        String input;
        inputList = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            while (true){
                input = br.readLine();
                if (input.equals("-1 -1 -1")){
                    break;
                }

                ArrayList<Integer> inputLine = new ArrayList<>();

                for (String inputStr: input.split(" ")){
                    inputLine.add(Integer.parseInt(inputStr));
                }

                inputList.add(inputLine);
            }
            return inputList;
        } catch (Exception e) {
            System.out.println("Error caused by BufferedReader or Integer.parseInt.");
            e.printStackTrace();
        }

        return null;
    }

    private int[] getEachMaxValue(){
        int[] max_val = new int[3];

        for (ArrayList<Integer> integers : inputList) {
            for (int j = 0; j < 3; j++) {
                max_val[j] = Math.max(max_val[j], integers.get(j));
            }
        }
        return max_val;
    }

    private void initDp(int[] maxValues){
        int a, b, c;
        a = maxValues[0];
        b = maxValues[1];
        c = maxValues[2];

        dp = new int[a+1][b+1][c+1];

        for (int i = 0; i <= a; i++) {
            for (int j = 0; j <= b; j++) {
                for (int k = 0; k <= c; k++) {
                    dp[i][j][k] = Main.NONACTIVE;
                }
            }
        }
    }

    public void solve() {
        int[] maxValues = getEachMaxValue();
        initDp(maxValues);
        w(maxValues[0], maxValues[1], maxValues[2]);

        StringBuilder printMsg = new StringBuilder();

        for (ArrayList<Integer> integers : inputList) {
            int a = integers.get(0);
            int b = integers.get(1);
            int c = integers.get(2);

            int result = w(a, b, c);
            printMsg.append("w(");
            printMsg.append(a);
            printMsg.append(", ");
            printMsg.append(b);
            printMsg.append(", ");
            printMsg.append(c);
            printMsg.append(") = ");
            printMsg.append(result);
            printMsg.append("\n");

        }

        System.out.println(printMsg);
    }

    public static void main(String[] args) {
        Main main = new Main();
        main.getInput();
        main.solve();
    }
}