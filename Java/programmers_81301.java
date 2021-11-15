import java.util.HashMap;
import java.util.Map;


public class programmers_81301 {
    public int solution(String s) {
        int[] numLength;
        int i;
        int length;
        String substring;

        Map<String, int[]> word2num = new HashMap<>();
        word2num.put("ze", new int[]{0, 4});
        word2num.put("on", new int[]{1, 3});
        word2num.put("tw", new int[]{2, 3});
        word2num.put("th", new int[]{3, 5});
        word2num.put("fo", new int[]{4, 4});
        word2num.put("fi", new int[]{5, 4});
        word2num.put("si", new int[]{6, 3});
        word2num.put("se", new int[]{7, 5});
        word2num.put("ei", new int[]{8, 5});
        word2num.put("ni", new int[]{9, 4});

        StringBuilder builder;
        i = 0;
        length = s.length();
        builder = new StringBuilder();
        while (i < length){
            char c = s.charAt(i);
            if (Character.isDigit(c)){
                builder.append(c);
                i++;
                continue;
            }
            substring = s.substring(i, i + 2);
            numLength = word2num.get(substring);
            builder.append(numLength[0]);
            i += numLength[1];
        }
        return Integer.parseInt(builder.toString());
    }
}