package finished.cGenerics;


public class LLIClass<T> implements LLIterator<T> {
    Node<T> node;

    public LLIClass(LinkedList<T> list){
        node = new Node(null);
        node.next = list.head;
    }

    @Override
    public T getNext() {
        node = node.next;
        return node.x;
    }

    @Override
    public boolean hasNext() {
        return node.next != null;
    }
}
