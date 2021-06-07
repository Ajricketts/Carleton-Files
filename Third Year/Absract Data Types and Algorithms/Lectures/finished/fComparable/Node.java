package finished.fComparable;

public class Node<T extends Comparable<T>>{
    T x;          //data
    Node<T> next;
    public Node(T x){
        this.x = x;
        next = null;
    }
}