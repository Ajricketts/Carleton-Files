package comp2402a5;

/**
 * This class implements the cuckoo hash
 *
 * See: Rasmus Pagh, Flemming Friche Rodler, Cuckoo Hashing, Algorithms - ESA 2001,
 * Lecture Notes in Computer Science 2161, Springer 2001, ISBN 3-540-42493-8
 *
 * @param <T>
 */
public abstract class CuckooHashTable<T> extends OpenAddressHashTable<T> {

	/* add any attributes you may need here */

	MultiplicativeHashFunction h1 = null;
	MultiplicativeHashFunction h2 = null;

	public int[] valz;
    public int index1 = 0;
    public int index2 = 1;




	/**
	 * Create a new empty hash table
	 * @param clazz is the class of the data to be stored in the hash table
	 * @param zz is an array of integer values to be used for the has functions
	 */
	public CuckooHashTable(Class<T> clazz, int[] zz) {
		//
		// add your code for the constructor here
		//
		super(clazz);
		valz = zz;

		n = 0;

		f = new Factory(clazz);
		d = 4;
		t = f.newArray(1 << d);

		h1 = new MultiplicativeHashFunction(valz[index1], w , d);
		h2 = new MultiplicativeHashFunction(valz[index2], w, d);
	}

	/* define all abstract methods inherited from parent class here */

	public boolean add(T x) {
        if (find(x) == x) {
            return false;
        } else {
            if (n + 1 > t.length / 2) {
                d++;
                rehash();
            }

            while(!injectValue(t, x)) {
                rehash();
            }

            n += 1;
            return true;
        }
    }

    public void resize() {
        rehash();
    }

    public void rehash() {
        T[] test = f.newArray(1 << d);
        boolean inject = false;

        while(!inject) {
            index1 += 2;
            index2 += 2;
            if (index1 >= valz.length || index2 >= valz.length) {
                break;
            }

            h1 = new MultiplicativeHashFunction(valz[index1], w, d);
            h2 = new MultiplicativeHashFunction(valz[index2], w, d);

            for(int i = 0; i < t.length; i++) {
                if (t[i] != null) {
                    if (!injectValue(test, t[i])) {
                        inject = false;
                        break;
                    }

                    inject = true;
                }
            }
        }

        t = test;
    }

    public T remove(T x) {
        if (n - 1 < t.length / 8 && d >= 5) {

            d -= 1;
            resize();
        }

        if (find(x) != null) {

            t[findLoc(x)] = null;
            n -= 1;
        }
        else {

            return null;
        }

        return x;
    }

    public T find(Object x) {
        return (findLoc(x) != -1) ? t[findLoc(x)] : null;
    }

    public int findLoc(Object x) {

	    if (x.equals(t[h1.hash(x)])) {

            return h1.hash(x);
        }
        else {

	        return (x.equals(t[h2.hash(x)])) ? h2.hash(x) : -1;
        }
    }

    public boolean injectValue(T[] arr, T x) {
        int count = 0;

        T place = x;
        int bootedFrom = h1.hash(x);
        T booted = arr[bootedFrom];

        arr[bootedFrom] = place;
        T test;

        while (true) {
            if (booted == null) { break; }


            if (booted.equals(x)) {
              count += 1;

              if (count > 2) {
                  count = 0;
                  return false;
              }
            }


            if (h2.hash(booted) == bootedFrom) {

                bootedFrom = h1.hash(booted);
            }

            else if (h1.hash(booted) == bootedFrom) {

                bootedFrom = h2.hash(booted);
            }

            test = arr[bootedFrom];
            arr[bootedFrom] = booted;
            booted = test;
        }

        return true;
    }
}

