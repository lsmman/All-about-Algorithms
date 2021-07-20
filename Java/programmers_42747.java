// 프로그래머스 정렬 H-Index
// https://programmers.co.kr/learn/courses/30/lessons/42747?language=java

import java.util.*;

class Solution {
    /**
     * @param citations 발표한 논문의 수
     * @return H-index
     *
     * 1. citations를 ArrayList의 sort를 이용해 내림차순으로 정렬해준다.
     *   예시 ) ArrayList<Integer> c_arr = {6, 5, 3, 1, 0}
     * 2. h를 1부터 citations의 max 값까지 1씩 증가시키면서
     *        h보다 element의 값이 작거나 같으면 해당 element의 index+1이 h이상 인용된 논문의 횟수이다.
     *        c_arr를 역순으로 훑으며 값이 작거나 같은 것을 찾는다.
     *        찾으면 answer의 h 값을 큰 것으로 업데이트 해준다.
     *   예시 ) c_arr = {6, 5, 3, 1, 0}
     *         index -> 0, 1, 2, 3, 4
     *         만약 h 값이 3이라면 c_arr을 역순으로 훑었을 때 값이 작거나 같은 것은 3이다.
     *         element 3의 index 값은 2이고 index+1은 3보다 큰 수의 개수이므로 문제의 조건에 부합한다.
     *
     * N := citations.length
     * M := citations.max
     * Big_O = ArrayList.sort -> O(NlogN)
     *       = search h -> O(M)
     *       = O(M)과 O(NlogN) 중 큰 값
     * */
    public static int solution(int[] citations) {
        ArrayList<Integer> c_arr = new ArrayList<>();
        int max_val, answer, i;

        for (int c: citations) {
            c_arr.add(c);
        }

        max_val = Collections.max(c_arr);
        i = c_arr.size()-1;
        answer = 0;

        c_arr.sort(Collections.reverseOrder());
        for (int h = 1; h < max_val; h++) {
            while (i >= 0) {
                if (h <= c_arr.get(i)) {
                    if (i+1 >= h){
                        answer = Math.max(answer, h);
                    }
                    break;
                }
                else {
                    i -= 1;
                }
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        int[] citations = {3, 0, 6, 1, 5};
        int answer = 3;

        int s = Solution.solution(citations);
        System.out.println(s == answer);
    }

}
