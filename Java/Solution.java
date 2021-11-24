import java.util.*;

public class Solution {

    public int solution(String[] id_list, int k) {
        int answer = 0;

        // 하루에 들렸는지..

        // 하루 map
        HashMap<String, Integer> map = new HashMap<>();

/*
        "JAY",                  // JAY + 1
        "JAY ELLE JAY MAY",     // JAY ELLE MAY
        "MAY ELLE MAY",         // MAY ELLE
        "ELLE MAY",             // ELLE MAY
        "ELLE ELLE ELLE",       // ELLE
        "MAY"

        하루마다 체크
        총 2번 이상은 체크 할 필요 없고

        그 날 하루에서 중복체크는 불가
*/

        // 키 전부 다 추가
        for (String s : id_list) {
            for (String temp: s.split(" ")) {
                map.putIfAbsent(temp, 0); // <- 키가 없을 때만 등록을 해라
            }
        }

        // 1번 뜰 때마다 체크를 하자
        // 2번 총 count가 2가 넘어가면 체크할 필요가 없다.
        // 3번 중복체크는 불가
        //      -> 3-1 "JAY ELLE JAY MAY" <- 이게 하루
                  // 하루마다 중복체크, unique 키만 남긴다 -> Set
                  // 3-1-1 Set를 만든다 - 초기화
                  // 3-1-2 하루에 해당하는 이름들을 set에 넣는다
                  // 3-1-2 넣은 셋으로 count 체크를한다.

        //      -> 3-2 "JAY ELLE JAY MAY" - 하루에 등장했는 지
                 //  -> Map <String, boolean> 등장했으면 True


        // 1, 2, 3-2
        Map<String, Boolean> checker = new HashMap<>();

        // 초기화
        for (String s : map.keySet()) {
            checker.putIfAbsent(s, Boolean.FALSE);
        }

        for (String s : id_list) {
            String[] day = s.split(" ");

            // 하루 단위 s : "JAY ELLE JAY MAY"
            for (String temp: day) {
                // 이미 체크가 되어 있으면 수행하면 안되자나요
                if (checker.get(temp)){ // True
                    continue;
                }

                checker.put(temp, Boolean.TRUE);
                Integer curCount = map.get(temp);

                if (curCount > 2){
                    continue;
                }
                map.put(temp, curCount + 1);
            }
        }


        // 1, 2, 3-1
        Set<String> daySet;
        for (String s : id_list) {
            String[] day = s.split(" ");
            // day -> Set에 넣는다
            daySet = new HashSet<>(); // 초기화
            daySet.addAll(Arrays.asList(day)); // 새로 넣음

            // 하루 단위 s : "JAY ELLE JAY MAY"
            for (String temp: daySet) {
                Integer curCount = map.get(temp);
                if (curCount > 2){
                    continue;
                }
                map.put(temp, curCount + 1);
            }
        }


        // 출력
        System.out.println("answer = " + answer);
        for (Map.Entry<String, Integer> stringIntegerEntry : map.entrySet()) {
            System.out.println("stringIntegerEntry = " + stringIntegerEntry);
        }

        return answer;
    }

    public static void main(String[] args) {


        String[] id_list = {"JAY",                  // JAY
                "JAY ELLE JAY MAY",     // JAY ELLE MAY
                "MAY ELLE MAY",         // MAY ELLE
                "ELLE MAY",             // ELLE MAY
                "ELLE ELLE ELLE",       // ELLE
                "MAY"                   // MAY
        };
        int k = 3;

        Solution solution = new Solution();
        solution.solution(id_list, k);

        String[] id_list2 = {"A B C D", "A D", "A B D", "B D"};
        int k2 = 2;

        Solution solution2 = new Solution();
        solution2.solution(id_list, k);
    }
}