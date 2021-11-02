/**
 *  Deque Example
 */
class Deque{
    public static void main(String[] args) {
        Deque<String> stack = new ArrayDeque<>();
        stack.addLast("Element1");
        stack.addLast("Element2");
        stack.addLast("Element3");
        System.out.println(stack.removeLast());
        System.out.println(stack.removeLast());
        System.out.println(stack.removeLast());
        stack.peekLast();
        stack.getLast();

        Deque<String> queue = new LinkedList<>()
        queue.addFirst("Element1");
        queue.addFirst("Element2");
        queue.addFirst("Element3");
        System.out.println(queue.removeLast());
        System.out.println(queue.removeLast());
        System.out.println(queue.removeLast());
        stack.peek() // stack.peekFirst()와 같다
        queue.getLast();
    }
}