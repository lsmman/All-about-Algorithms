/*
그래프 가장 먼 노드
https://programmers.co.kr/learn/courses/30/lessons/49189
 */

import java.util.*;


class Solution {
    public static int solution(int n, int[][] edge) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> connected = new ArrayList<>(n+1);
        boolean[] visited = new boolean[n+1];
        for (int i = 0; i <= n; i++) {
            connected.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < edge.length; i++) {
            connected.get(edge[i][0]).add(edge[i][1]);
            connected.get(edge[i][1]).add(edge[i][0]);
        }

        int cur;
        int dist;
        Queue<int[]> queue = new LinkedList<>();
        int[] distance = new int[n+1];
        int[] pop;

        cur = 1;
        visited[cur] = true;
        queue.add(new int[] {0, cur});
        while (!(queue.isEmpty())){
            pop = queue.poll();
            dist = pop[0];
            cur = pop[1];
            for (int v: connected.get(cur)){
                if (!visited[v]){
                    visited[v] = true;
                    distance[v] = dist+1;
                    queue.add(new int[] {dist+1, v});
                }
            }
        }

        int max_val = Arrays.stream(distance).max().orElseThrow();
        for (int i = 0; i < distance.length; i++) {
            if (distance[i] == max_val) {
                answer += 1;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        int result, answer;

        result = Solution.solution(6, new int[][] {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}});
        answer = 3;
        System.out.println(result);
        System.out.println(result == answer);


    }
}
