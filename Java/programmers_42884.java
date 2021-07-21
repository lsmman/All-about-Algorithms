// 프로그래머스 탐욕법(Greedy) 단속카메라
// https://programmers.co.kr/learn/courses/30/lessons/42884

import java.util.*;

class Solution {
    public static int solution(int[][] routes) {
        int lastTime = -30001;
        int answer = 0;
        Arrays.sort(routes, (o1, o2) -> Integer.compare(o1[1], o2[1]));
        for (int i = 0; i < routes.length; i++) {
            if (lastTime < routes[i][0]){
                answer++;
                lastTime = routes[i][1];
            }
        }
        // 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return
        return answer;
    }

    public static void main(String[] args) {
        int result = Solution.solution(new int[][] {{-20, 15}, {-14, -5}, {-18, -13}, {-5, -3}});
        int answer = 2;
        System.out.println(result);
        System.out.println(result == answer);

    }
}
