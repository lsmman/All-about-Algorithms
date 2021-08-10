// 프로그래머스 dfs/DFS 여행경로
// https://programmers.co.kr/learn/courses/30/lessons/43164?language=java
//
// 코드 설명 : graph를 dictionary로 구현하였고,
//            각 edge는 node별로 linear insert sort로 arraylist에 담겨있도록 만들었다.
//              node("ICN") -> edge(["ATC", "BAN", "CHA"]) 알파벳 순으로 정렬
//            그 후 node를 dfs와 브루트포스로 검색하며
//            edge 리스트에 빠른 알파벳순으로 모든 엣지를 다 방문하는 경우 경로를 return 한다.
//
// 시간 복잡도 : best O(e * maxE), worst O(e * e)
//      e은 edge의 총 개수, maxE는 한 노드의 최대 edge 수, n은 node의 총 개수 (n <= e)
//      make graph -> e * maxE
//      search -> n, best case
//             -> e * e, worst case
// 공간 복잡도 : O(e), e의 총 개수
//
// 실수한 사항 : 엣지의 중복이 존재함을 깨닫고 visit을 boolean에서 int로 바꿨다.
//              HashMap dictionary를 사용했는데 포함되지 않는 key가 나올 경우 예외 처리를 못해 런타임 에러가 떴었다.
//              HashMap의 arrayList가 loop에 들어가기 전 containskey로 검사하는 루틴을 넣어주었다.
// maxE가 충분히 클 시에는,
//      각 node는 알파벳 순으로 sort된 edge를 dictionary에 가지고 있게 되는데
//      linear insert sort를 binary insert sort로 바꿔줄 시 성능 개선을 만들 수 있다.
//
// 코드 예시 중 edge list를 그래프로 만들지 않고 탐색하여 되는 경우를 모두 찾는 코드가 있었는데
// 그 경우 전부 탐색하게된다. 완전 탐색이 된다.
// 그 경우 시간 복잡도는 (엣지의 총 갯수 e) O(e * e)가 되고 성능 향상을 이루기도 힘들어진다.

import java.util.*;

class Pair {
    public String city = "";
    public int visit = 0;
    public Pair(String city_name){
        city = city_name;
        visit++;
    }
    public void add_duplicated(){
        visit++;
    }
}

class Solution {
    private static Map<String, ArrayList<Pair>> dict = new HashMap<String, ArrayList<Pair>>();
    private static String dfs(String cur, int visit_cnt){
        if (visit_cnt == 0){
            return cur;
        }
        String result;
        if (!dict.containsKey(cur)) {
            return "";
        }
        for (Pair p : dict.get(cur)) {
            if (p.visit > 0) {
                p.visit--;
                result = dfs(p.city, visit_cnt - 1);
                if (!result.equals("")) {
                    return cur + ' ' + result;
                }
                p.visit++;
            }
        }
        return "";
    }
    public static String[] solution(String[][] tickets) {
        int i, length, compare;
        boolean check;
        String result, key, value;
        ArrayList<Pair> cur_arr;
        ArrayList<String> answer = new ArrayList<String>();

        for (String[] kv: tickets) {
            key = kv[0];
            value = kv[1];

            if (!dict.containsKey(key)) {
                dict.put(key, new ArrayList<Pair>());
            }
            cur_arr = dict.get(key);
            check = false;
            for (i = 0, length = cur_arr.size(); i < length; i++) {
                compare = cur_arr.get(i).city.compareTo(value);
                if (compare > 0){
                    cur_arr.add(i, new Pair(value));
                    check = true;
                    break;
                }
                else if (compare == 0){
                    cur_arr.get(i).add_duplicated();
                    check = true;
                    break;
                }
            }
            if (!check) {
                cur_arr.add(new Pair(value));
            }

        }
        result = dfs("ICN", tickets.length);

        return result.split(" ");
    }
    public static void main(String[] args) {
//        String[] result = Solution.solution(new String[][] {{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}});
//        String[] answer = {"ICN", "JFK", "HND", "IAD"};
//        System.out.println(result.toString());
//        System.out.println(Arrays.equals(result, answer));
//
//        String[] result2 = Solution.solution(new String[][] {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL","SFO"}});
//        String[] answer2 = {"ICN", "ATL", "ICN", "SFO", "ATL", "SFO"};
//        Arrays.stream(result2).forEach(System.out::println);
//        System.out.println(Arrays.equals(result2, answer2));

        String[] result2 = Solution.solution(new String[][] {{"ICN", "A"}, {"ICN", "C"}, {"C", "ICN"}});
        String[] answer2 = {"ICN", "C", "ICN", "A"};
        Arrays.stream(result2).forEach(System.out::println);
        System.out.println(Arrays.equals(result2, answer2));

    }
}
