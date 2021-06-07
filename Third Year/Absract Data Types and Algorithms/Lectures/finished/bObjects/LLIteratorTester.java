package finished.bObjects;

public class LLIteratorTester {

    public static void main(String[] args){
        LinkedList list = new LinkedList();
        for (int i = 0; i < 20; i++){
            list.add(i);
        }

        LLIterator lli = new LLIClass(list);
        int total = 0;

        while (lli.hasNext()){
            total += (Integer)lli.getNext();
        }

        System.out.println("The total is "+ total);

    }
}
