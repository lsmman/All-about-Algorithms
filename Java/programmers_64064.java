import java.util.*;

class programmers_64064 {
    //class Solution {
    List<List<Integer>> bannedList = new ArrayList<>();
    boolean[] visit = null;
    Set<String> available = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {
        char wildcard = '*';
        visit = new boolean[user_id.length];
        Map<String, Set<Integer>> positionDict = new HashMap<>();
        List<Integer> all = new ArrayList<>();
        int[] userLengths = new int[user_id.length];

        for (int i = 0; i < userLengths.length; i++) {
            userLengths[i] = user_id[i].length();
        }

        for (int index = 0; index < user_id.length; index++) {
            String cur = user_id[index];
            for (int pos = 0; pos < cur.length(); pos++) {
                String s = pos + String.valueOf(cur.charAt(pos));
                positionDict.putIfAbsent(s, new HashSet<>());
                positionDict.get(s).add(index);
            }
        }

        for (int i = 0; i < user_id.length; i++) {
            all.add(i);
        }

        for (String b : banned_id) {
            Set<Integer> indexes = new HashSet<>();
            int bLength = b.length();
            int wildcardCount = 0;

            for (int pos = 0; pos < bLength; pos++) {
                if (b.charAt(pos) == wildcard) {
                    wildcardCount++;
                    continue;
                }
                String key = pos + String.valueOf(b.charAt(pos));
                if (!positionDict.containsKey(key)) {
                    continue;
                }
                Set<Integer> cur = positionDict.get(key);
                if (indexes.isEmpty()) {
                    indexes = cur;
                    continue;
                }
                indexes.retainAll(cur);
            }
            if (wildcardCount == bLength) {
                indexes = new HashSet<>(all);
            }
            List<Integer> result = new ArrayList<>();
            for (Integer index : indexes) {
                if (bLength != userLengths[index]){
                    continue;
                }
                result.add(index);
            }
            bannedList.add(result);
        }
        dfs(bannedList.size()-1);
        return available.size();
    }

    private void dfs(int bannedIndex){
        if (bannedIndex < 0){
            StringBuilder checker = new StringBuilder();
            for (boolean v : visit) {
                if (v){
                    checker.append(1);
                }
                else{
                    checker.append(0);
                }
            }
            available.add(checker.toString());
            return;
        }
        List<Integer> integers = bannedList.get(bannedIndex);
        int size = integers.size();
        for (int i = 0; i < size; i++) {
            Integer cur = integers.get(i);
            if (visit[cur]){
                continue;
            }
            visit[cur] = true;
            dfs(bannedIndex-1);
            visit[cur] = false;
        }
    }

    public static void main(String[] args) {
        int solution;

//        programmers_64063 p = new programmers_64063();
//        solution = p.solution(new String[]{"frodo", "fradi", "crodo", "abc123", "frodoc"}, new String[]{"fr*d*", "abc1**"});
//        System.out.println(solution); // 2

        programmers_64064 p2 = new programmers_64064();
        solution = p2.solution(new String[]{"frodo", "fradi", "crodo", "abc123", "frodoc"}, new String[]{"*rodo", "*rodo", "******"});
        System.out.println(solution);

    }
}

