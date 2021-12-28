import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class programmers_1806 {
    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] split = bufferedReader.readLine().split(" ");
        int n = Integer.parseInt(split[0]);
        int s = Integer.parseInt(split[1]);

        split = bufferedReader.readLine().split(" ");

        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(split[i]);
        }

        int partSum = 0;
        int left = 0;
        int right = 0;
        int answer = n+1;

        while (left < n && right < n){
            while (right < n && (partSum + nums[right]) < s){
                partSum += nums[right];
                right++;
            }
            if (right < n && partSum + nums[right] >= s){
                answer = Math.min(answer, right - left + 1);
            }
            partSum -= nums[left];
            left++;
        }
        System.out.println(answer % (n+1));
    }
}
