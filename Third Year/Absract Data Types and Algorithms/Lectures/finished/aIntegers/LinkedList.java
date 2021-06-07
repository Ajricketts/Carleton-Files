package finished.aIntegers;

public class LinkedList {

    Node head;

    public LinkedList(){
        head = null;
    }

    public void add(int x){
        Node node = new Node(x);
        node.next = head;
        head = node;
    }


}
