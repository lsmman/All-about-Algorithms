// 프로그래머스 이진 탐색 징검다리
// https://programmers.co.kr/learn/courses/30/lessons/43236?language=java


import java.util.Arrays;

class Solution {
    public static int solution(int distance, int[] rocks, int n) {
        int[] pos = new int[rocks.length+1];
        int i, length;
        int answer = -1;
        int left, mid, right;
        int last_pos, removed;

        Arrays.sort(rocks);
        i = 0;
        length = pos.length;
        for (int r: rocks) {
            pos[i++] = r;
        }
        pos[i] = distance;

        left = 0;
        right = distance;
        mid = 0;
        while (left <= right) {
            mid = (left + right) / 2;
            removed = 0;
            last_pos = 0;
            for (int p: pos) {
                if ((p - last_pos) < mid) {
                    removed++;
                }
                else {
                    last_pos = p;
                }
            }
            if (removed > n) {
                right = mid - 1;
            }
            else {
                answer = Math.max(answer, mid);
                left = mid + 1;
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        int result = Solution.solution(25, new int[] {2, 14, 11, 21, 17}, 2);
        int answer = 4;
        System.out.println(result);
        System.out.println(result == answer);
    }
}
