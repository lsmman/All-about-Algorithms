
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_10989 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int n = Integer.parseInt(s);
        int[] ints = new int[10001];
        int input_n;
        for (int i = 0; i < n; i++) {
            s = br.readLine();
            input_n = Integer.parseInt(s);
            ints[input_n] += 1;
        }

        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < 10001; i++) {
            for (int j = 0; j < ints[i]; j++) {
                stringBuilder.append(i + "\n");
            }
        }
        System.out.println(stringBuilder.toString());
    }
}
