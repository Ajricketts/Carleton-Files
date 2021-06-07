package comp2402a5;

public class Cuckoo<T> extends CuckooHashTable<T>{
    public Cuckoo(Class<T> clazz, int[] zz) {
        super(clazz, zz);
    }

    T[] getArray(){
        T[] copyOfArray = f.newArray(1<<d);
        System.arraycopy(t, 0, copyOfArray, 0, t.length);
        return copyOfArray;
    }


    public static void main(String[] args){
        int[] Z;
        Z = new int[]{1445229539, 372911817, 2113534159, 1880685119, 532791015, 1428079773};

        System.out.println("zz=" + java.util.Arrays.toString(Z) );
        CuckooHashTable<String> c = new Cuckoo<String>(String.class, Z);
        System.out.println( "h1=" + java.util.Arrays.toString(c.h1.getParams()) );
        System.out.println( "h2=" + java.util.Arrays.toString(c.h2.getParams()) );
        System.out.println(c);
        c.add("cat");
        System.out.println(c);
        c.add("dog");
        System.out.println(c);
        c.add("eel");
        System.out.println(c);
        c.add("cow");
        System.out.println(c);
        c.add("elf");
        System.out.println(c);
        System.out.println( java.util.Arrays.toString( ((Cuckoo)c).getArray() ) );
    }

}