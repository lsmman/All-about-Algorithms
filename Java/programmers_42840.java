/*
    프로그래머스 완전탐색 모의고사 java 풀이
 */

//import java.util.List;
import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    public static int @NotNull [] solution(int[] answers) {
        int i, num_of_person = 3;

        int[][] persons = {
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5},
        };
        int[] cnt = new int[num_of_person];
        int[] p_length = new int[num_of_person];

        for (i = 0; i < num_of_person; i++) p_length[i] = persons[i].length;
        for (int ans = 0; ans < answers.length; ans++) {
            for (i = 0; i < num_of_person; i++) {
                if (answers[ans] == persons[i][ans % p_length[i]]) {
                    cnt[i]++;
                }
            }
        }

        ArrayList<Integer> high_scored = new ArrayList<>();
        int max_val = Arrays.stream(cnt).max().getAsInt();
        for (i = 0; i < num_of_person; i++) {
            if (max_val == cnt[i]) {
                high_scored.add(i + 1);
            }
        }
        int[] answer = new int[high_scored.size()];
        i = 0;
        for (int h : high_scored) answer[i++] = h;
        return answer;
    }

    public static void main(String[] args) {
        int[] problem1 = {1, 2, 3, 4, 5};
        int[] answer1 = Solution.solution(problem1);
        Arrays.stream(answer1).forEach(System.out::println); // {1}

        int[] problem2 = {1,3,2,4,2};
        int[] answer2 = Solution.solution(problem2);
        Arrays.stream(answer2).forEach(System.out::println); // {1, 2, 3}
    }
}

