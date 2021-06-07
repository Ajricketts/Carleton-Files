package finished.bObjects;

public class LinkedList {

    Node head;

    public LinkedList(){
        head = null;
    }

    public void add(Object x){
        Node node = new Node(x);
        node.next = head;
        head = node;
    }


}
