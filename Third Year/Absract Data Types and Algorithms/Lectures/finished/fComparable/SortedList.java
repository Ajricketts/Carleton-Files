package finished.fComparable;

public class SortedList<T extends Comparable<T>> {

    Node<T> head;

    public SortedList(){
        head = null;
    }

    public void add(T x){

        Node<T> node = new Node(x);


        if((head == null)||(x.compareTo(head.x)<0)){
            node.next = head;
            head = node;
            return;
        }

        Node<T> temp = head;

        while((temp.next!= null)&&(x.compareTo(temp.next.x)>0)){
            temp = temp.next;
        }

        if (temp.next == null){
            temp.next = node;
        }else{
            node.next = temp.next;
            temp.next = node;
        }

    }


}
