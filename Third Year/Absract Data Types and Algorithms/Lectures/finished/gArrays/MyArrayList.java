package finished.gArrays;

import java.lang.reflect.Array;

public class MyArrayList<T> {

    T[] array;

    public MyArrayList(Class c, int size){  // can also be Class c
        //array = new T[size];
        array = (T[]) Array.newInstance(c, size);
    }

    public static void main(String[] args){
        LinkedList<Integer> llist = new LinkedList<>();
        MyArrayList<Integer> list = new MyArrayList<Integer>(Integer.class, 100);
        System.out.println("Success!");

        for (int i = 0; i < 20; i++){
            list.array[i] = i;
        }

        for (int i = 0; i < 20; i++){
            System.out.println(list.array[i]);
        }
    }
}
