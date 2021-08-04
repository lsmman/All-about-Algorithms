// 프로그래머스 동적계획법(Dynamic programming) 등굣길
// https://programmers.co.kr/learn/courses/30/lessons/42898?language=java

import java.util.*;

class Solution {
    public static int solution(int m, int n, int[][] puddles) {
        boolean[][] jam = new boolean[n+1][m+1];
        int[][] loc = new int[n+1][m+1];
        int mod =  1000000007;

        for (int[] p: puddles) {
            jam[p[1]][p[0]] = true;
        }

        loc[1][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (jam[i][j]) { continue; }
                loc[i][j] = (loc[i-1][j] + loc[i][j-1]) % mod;
            }
        }
        return loc[n][m];
    }

    public static void main(String[] args) {
        int result, answer;
        result = Solution.solution(4, 3 , new int[][] {});
        answer = 10;
        System.out.println(result);
        System.out.println(result == answer);

        result = Solution.solution(4, 3 , new int[][] {{2, 2}});
        answer = 4;
        System.out.println(result);
        System.out.println(result == answer);

    }
}
