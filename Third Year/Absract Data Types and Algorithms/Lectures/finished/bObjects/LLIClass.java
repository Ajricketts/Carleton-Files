package finished.bObjects;


public class LLIClass implements LLIterator {
    Node node;

    public LLIClass(LinkedList list){
        node = new Node(-1);
        node.next = list.head;
    }

    @Override
    public Object getNext() {
        node = node.next;
        return node.x;
    }

    @Override
    public boolean hasNext() {
        return node.next != null;
    }
}
