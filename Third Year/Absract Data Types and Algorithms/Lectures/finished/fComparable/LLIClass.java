package finished.fComparable;


public class LLIClass<T extends  Comparable<T>> implements LLIterator<T> {
    Node<T> node;

    public LLIClass(SortedList<T> list){
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
