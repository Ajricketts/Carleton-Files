package finished.eNumber;

public class Node<T extends Number>{
    T x;          //data
    Node<T> next;
    public Node(T x){
        this.x = x;
    }
}