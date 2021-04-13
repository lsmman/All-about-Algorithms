package Java.Solution.src;

import java.util.ArrayList;

public class Solution {
    public static ArrayList<Integer> solution(int numbers[]) {
        int n = numbers.length;
        int cur, i, j;
        ArrayList<Integer> answer = new ArrayList<>();
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                cur = numbers[i] + numbers[j];
                if (!answer.contains(cur)) {
                    answer.add(cur);
                }
            }
        }
        answer.sort(null);

        return answer;
    }

    public static void main(String[] args) throws Exception {
        int[] a = { 1, 2, 3, 4 };
        solution(a);
    }
}