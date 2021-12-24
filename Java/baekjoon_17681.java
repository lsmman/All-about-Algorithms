

class baekjoon_17681 {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        int result, length;
        String line;
        
        String binary1, binary2;
        int length1, length2, pos1, pos2;
        for (int i = 0; i < n; i++){
            StringBuilder builder = new StringBuilder();
            result = arr1[i] | arr2[i];
            line = Integer.toBinaryString(result);
            length = line.length();
            for (int j = n - length; j > 0; j--){
                builder.append(" ");
            }
            for (int pos=0; pos < length; pos++){
                if (line.charAt(pos) == '1'){
                    builder.append("#");
                }
                else {
                    builder.append(" ");
                }
            }
            answer[i] = builder.toString();
        }
        return answer;
    }
}
