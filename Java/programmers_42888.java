// https://programmers.co.kr/learn/courses/30/lessons/42888?language=java#


import java.util.*;

class programmers_42888 {
    public String[] solution(String[] record) {
        ArrayList<String> answer = new ArrayList<>();
        String[] answer_str;
        String[] info;
        Map<String, String> nicknames = new HashMap<>();
        
        String enter_msg = "님이 들어왔습니다.";
        String leave_msg = "님이 나갔습니다.";
        String uid, nickname;
        
        for (String r:record){
            info = r.split(" ");
            uid = info[1];
            if (info[0].equals("Enter")){
                nickname = info[2];
                
                // 닉네임을 갱신한다.
                nicknames.put(uid, nickname);
            }
            else if (info[0].equals("Change")){
                nickname = info[2];
                
                // 닉네임을 갱신한다.
                nicknames.put(uid, nickname);
            }
        }
        for (String r:record){
            info = r.split(" ");
            uid = info[1];
            nickname = nicknames.get(uid);
            if (info[0].equals("Enter")){
                // 문구를 입력한다.
                answer.add(nickname + enter_msg);
            }
            else if (info[0].equals("Leave")){
                answer.add(nickname + leave_msg);
            }
        }
        answer_str = new String[answer.size()];
        for (int i = 0; i < answer.size(); i++){
            answer_str[i] = answer.get(i);
        }
        return answer_str;
    }
    /*
    "Muzi님이 들어왔습니다."
    "Prodo님이 들어왔습니다."
    "Muzi님이 나갔습니다."
    
    "Prodo님이 들어왔습니다."
    "Prodo님이 들어왔습니다."
    "Prodo님이 들어왔습니다."
    
    prodo로 변경하면 아래처럼 바뀌어야함
    
    닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
    */
}