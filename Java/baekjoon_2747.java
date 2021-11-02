
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_2747 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        int n = Integer.parseInt(s);

        if (n <= 1) {
            System.out.println(n);
            return;
        }
        int pre, next;
        pre = 0;
        next = 1;
        int result = 0;

        for (int i = 0; i < n - 1; i++) {
            result = pre + next;
            pre = next;
            next = result;
        }

        System.out.println(result);
    }
}
