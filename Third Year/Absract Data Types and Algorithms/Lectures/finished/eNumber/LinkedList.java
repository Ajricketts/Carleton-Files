package finished.eNumber;

public class LinkedList<T extends Number> {

    Node<T> head;

    public LinkedList(){
        head = null;
    }

    public void add(T x){
        Node node = new Node(x);
        node.next = head;
        head = node;
    }


}
