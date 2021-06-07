package comp2402a2;

import java.util.AbstractList;
import java.util.List;
import java.util.Random;

/**
 * @author morin
 *
 * @param <T> the type of objects stored in the List
 */
public class BlockedList<T> extends AbstractList<T> {
	/**
	 * keeps track of the class of objects we store
	 */
	Factory<T> f;

	/**
	 * The number of elements stored
	 */
	int n;

	/**
	 * The block size
	 */
	int b;

    /**
	 * Holds our stuff
	 */
	ArrayDeque<ArrayDeque<T>> blocks;

	/**
	 * Constructor
	 * @param t the type of objects that are stored in this list
	 * @param b the block size
	 */
  @SuppressWarnings("unchecked")
	public BlockedList(Class<T> t, int b) {
		this.b = b;
		f = new Factory<T>(t);
		n = 0;
		blocks = new ArrayDeque<ArrayDeque<T>>((Class<ArrayDeque<T>>)(new ArrayDeque<T>(t)).getClass());

		//TODO maybe there should be one or two blocks to start?

	}

	public int size() {
		return n;
	}

	public T get(int i) {
		// TODO: Implement this
		if (i < 0 || i > n - 1) throw new IndexOutOfBoundsException();
		return null;
	}

	public T set(int i, T x) {
		// TODO: Implement this
		if (i < 0 || i > n - 1) throw new IndexOutOfBoundsException();
		return null;
	}

	public void add(int i, T x) {
		// TODO: Implement this
		if (i < 0 || i > n) throw new IndexOutOfBoundsException();
	}

	public T remove(int i) {
		// TODO: Implement this
		if (i < 0 || i > n - 1) throw new IndexOutOfBoundsException();
		return null;
	}

	public static void main(String[] args) {
		List<Integer> bl = new BlockedList<Integer>(Integer.class, 10);

		System.out.println(bl);
		for (int i = 0; i < 53; i++) {
			bl.add(i);
		}
		System.out.println(bl);
		for (int i = -1; i > -25; i--) {
			bl.add(0, i);
		}
		System.out.println(bl);

		Random rand = new Random();
		for (int i = 0; i < 50; i++) {
				bl.add(rand.nextInt(bl.size()+1), 200+i);
		}
		System.out.println(bl);
		while(bl.size() > 5) {
			System.out.println(bl);
			bl.remove(3);
		}

		while (!bl.isEmpty()) {
			bl.remove(rand.nextInt(bl.size()));
		}
	}
}
