package finished.dContainer;

public class Node<T>{
    T x;          //data
    Node<T> next;
    public Node(T x){
        this.x = x;
    }
}