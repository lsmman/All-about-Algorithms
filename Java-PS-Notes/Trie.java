import java.util.HashMap;
import java.util.Map;


class TrieNode {
    // [ 변수 ]
    // 자식 노드 맵
    private Map<Character, TrieNode> childNodes = new HashMap<>();
    // 마지막 글자인지 여부
    private boolean isLastChar;
    // [ GETTER / SETTER 메서드 ]
    // 자식 노드 맵 Getter
    Map<Character, TrieNode> getChildNodes() {
        return this.childNodes;
    }
    // 마지막 글자인지 여부 Getter
    boolean isLastChar() {
        return this.isLastChar;
    }

    // 마지막 글자인지 여부 Setter
    void setIsLastChar(boolean isLastChar) {
        this.isLastChar = isLastChar;
    }

    boolean hasChild() {
        return !this.childNodes.isEmpty();
    }
}



public class Trie {
    // [ 변수 ]
    // 루트 노드
    private final TrieNode rootNode;
    // [ 생성자 ]

    Trie() {
        rootNode = new TrieNode();
    }

    // [ 메서드 ]
    // 자식 노드 추가
    void insert(String word) {
        TrieNode thisNode = this.rootNode;
        for (int i = 0; i < word.length(); i++) {
            thisNode = thisNode.getChildNodes().computeIfAbsent(word.charAt(i), c -> new TrieNode());
        }
        thisNode.setIsLastChar(true);
    }

    // 특정 단어가 들어있는지 확인
    boolean contains(String word) {
        TrieNode thisNode = this.rootNode;
        for (int i = 0; i < word.length(); i++) {
            char character = word.charAt(i);
            TrieNode node = thisNode.getChildNodes().get(character);
            if (node == null) return false; thisNode = node;
        }
        return thisNode.isLastChar();
    }

    // 특정 단어 지우기
    void delete(String word) {
        delete(this.rootNode, word, 0);
        // 최초로 delete 던지는 부분
    }

    private void delete(TrieNode thisNode, String word, int index) {
        char character = word.charAt(index);

        // APPLE, PEN과 같이 아예 없는 단어인 경우 에러 출력
        if(!thisNode.getChildNodes().containsKey(character))
            throw new Error("There is no [" + word + "] in this Trie.");

        TrieNode childNode = thisNode.getChildNodes().get(character);
        index++;
        if(index == word.length()) {
            // 삭제조건 2번 항목
            // PO와 같이 노드는 존재하지만 insert한 단어가 아닌 경우 에러 출력
            if (!childNode.isLastChar())
                throw new Error("There is no [" + word + "] in this Trie.");
            childNode.setIsLastChar(false);
            // 삭제조건 1번 항목
            // 삭제 대상 언어의 제일 끝으로써 자식 노드가 없으면(이 단어를 포함하는 더 긴 단어가 없으면) 삭제 시작
            if (childNode.getChildNodes().isEmpty()) thisNode.getChildNodes().remove(character);
        }
        else {
            delete(childNode, word, index);
            // 콜백함수부분
            // 삭제조건 1,3번 항목
            // 삭제 중, 자식 노드가 없고 현재 노드로 끝나는 다른 단어가 없는 경우 이 노드 삭제
            if(!childNode.isLastChar() && childNode.getChildNodes().isEmpty())
                thisNode.getChildNodes().remove(character);
        }
    }

    private boolean isRootEmpty() {
        return !this.rootNode.hasChild();
    }

    public static void main(String[] args) {
        Trie trie = new Trie();
        // insert 메서드
        System.out.println(trie.isRootEmpty()); // True
        trie.insert("PI");
        trie.insert("PIE");
        trie.insert("POW");
        trie.insert("POP");

        System.out.println(trie.isRootEmpty()); //False

        // Contains 메서드
        System.out.println(trie.contains("POW")); // True
        System.out.println(trie.contains("PIES")); // False

        // Delete 메서드
        trie.delete("POP");
        System.out.println(trie.contains("POP")); // False
        System.out.println(trie.contains("POW")); // True

        // 없는 단어를 지울 때 > 에러발생하는 예
        trie.delete("PO");
        trie.delete("PIES");
        trie.delete("PEN");
    }

}


// 출처 : 개발개님 Trie https://the-dev.tistory.com/3


