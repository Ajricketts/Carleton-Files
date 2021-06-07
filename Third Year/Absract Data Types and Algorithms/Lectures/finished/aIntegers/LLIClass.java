package finished.aIntegers;


public class LLIClass implements LLIterator {
    Node node;

    public LLIClass(LinkedList list){
        node = new Node(-1);
        node.next = list.head;
    }

    @Override
    public int getNext() {
        node = node.next;
        return node.x;
    }

    @Override
    public boolean hasNext() {
        return node.next != null;
    }
}
