// 프로그래머스 Heap 디스크 컨트롤러
// https://programmers.co.kr/learn/courses/30/lessons/42627?language=java

import java.util.*;

class Solution {
// 들어오는 순으로 정렬하고
// 지금 turn수보다 작업 요청되는 시점이 이전일 경우 heap에 넣어주고
// 제일 작은 값을 빼준다.
    public static int solution(int[][] jobs) {
        int turn, answer, i;
        int[] polled;
        int jobs_length = jobs.length;

        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((o1, o2) -> Integer.compare(o1[1], o2[1]));
        Arrays.sort(jobs, (o1, o2) -> Integer.compare(o1[0], o2[0]));

        turn = 0;
        answer = 0;
        i = 0;
        while (i < jobs_length || !pq.isEmpty()){
            while (i < jobs_length && turn >= jobs[i][0]){
                pq.offer(jobs[i++]);
            }
            if (pq.isEmpty()) {
                turn = jobs[i][0];
            }
            else {
                polled = pq.poll();
                turn += polled[1];
                answer += (turn - polled[0]);
            }
        }

        return (int) answer / jobs_length;
    }
    public static void main(String[] args) {
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
        int answer = 9;

        int s = Solution.solution(jobs);
        System.out.println(s == answer);
    }

}
