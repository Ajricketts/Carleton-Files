package finished.fComparable;

public class Employee implements Comparable<Employee> {

    static int currentID = 0;
    String name;
    int id;

    @Override
    public int compareTo(Employee o) {
        //return this.id - o.id;
        return name.compareTo(o.name);
    }

    public Employee(String name){
        this.name = name;
        id = currentID ++;
    }
}
