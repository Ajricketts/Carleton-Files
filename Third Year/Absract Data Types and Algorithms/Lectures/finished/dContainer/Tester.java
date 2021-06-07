package finished.dContainer;

public class Tester {

    public static void foo(LinkedList<Number> arg){
        arg.add(new Integer(123));
        arg.add(new Double(4.53));
    }

    public static void main(String[] args){
        LinkedList<Number> list = new LinkedList<>();
        foo(list);

        LinkedList<Integer> list2 = new LinkedList<>();

        //foo(list2);
    }

}
