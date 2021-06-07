package finished.fComparable;

public class Tester {



    public static void main(String[] args){
        SortedList<Integer> list = new SortedList<>();

        for (int i = 20; i >0; i--){
            list.add(i);
            System.out.println("Added "+i);
        }

        System.out.println("Done adding");

        LLIterator<Integer> lli = new LLIClass<Integer>(list);
        while(lli.hasNext()){
            System.out.println(lli.getNext());
        }


        //SortedList<Number> list2 = new SortedList<>();

        SortedList<Employee> list3 = new SortedList<>();

    }

}
