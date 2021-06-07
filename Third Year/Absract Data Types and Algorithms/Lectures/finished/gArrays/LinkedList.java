package finished.gArrays;

public class LinkedList<T> {

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
