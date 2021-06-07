package finished.cGenerics;

public class LLIteratorTester {

    public static void main(String[] args){
        LinkedList<Integer> list = new LinkedList();
        for (int i = 0; i < 20; i++){
            list.add(i);
        }

        LLIterator<Integer> lli = new LLIClass(list);
        int total = 0;

        while (lli.hasNext()){
            total += lli.getNext();
        }

        System.out.println("The total is "+ total);

    }
}
