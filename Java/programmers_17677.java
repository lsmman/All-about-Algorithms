import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class programmers_17677 {
    private static int CONVERSION = 65536;

    public int solution(String str1, String str2) {
        Set<String> set1 = makeJacadUnit(str1.toLowerCase());
        Set<String> set2 = makeJacadUnit(str2.toLowerCase());

        Set<String> union = new HashSet<>(set1);
        union.addAll(set2);

        if (union.isEmpty()){
            return CONVERSION;
        }

        Set<String> interaction = new HashSet<>(set1);
        interaction.retainAll(set2);

        int i =  CONVERSION * interaction.size() / union.size();
        return i;
    }

    private static Set<String> makeJacadUnit(String str) {
        Map<String, Integer> strings = new HashMap<>();
        Set<String> set = new HashSet<>();
        int strLength = str.length();
        for (int i = 0; i < strLength-1; i++) {
            String key = str.substring(i, i + 2);
            if (!isAlpha(key)){
                continue;
            }
            strings.putIfAbsent(key, 0);
            set.add(key + strings.get(key));
            strings.computeIfPresent(key, (s, integer) -> integer + 1);
        }
        return set;
    }

    private static boolean isAlpha(String string) {
        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if (!Character.isAlphabetic(c)){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int answer;
        programmers_17677 main = new programmers_17677();
        answer = main.solution("FRANCE", "french");
        System.out.println(answer + " " + (answer == 16384));

        answer = main.solution("aa1+aa2", "AAAA12");
        System.out.println(answer + " " + (answer == 43690));
    }
}
