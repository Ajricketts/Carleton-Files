package comp2402a2;

import java.util.AbstractList;

/**
 * Treque : an implementation of the List interface 
 * that allows for fast modifications at the head, tail
 * and middle of the list.
 *
 * Modify the methods so that 
 *  -set/get have constant runtime
 *  -add/remove have O(1+min{i, size()-i, |size()/2-i|})
 *              amortized runtime.
 * 
 * @author morin/ArrayDeque
 *
 * @param <T> the type of objects stored in this list
 */

public class Treque<T> extends AbstractList<T> {

	protected ArrayDeque<T> f;

	protected ArrayDeque<T> b;

	public Treque(Class<T> t) {
		f = new ArrayDeque<>(t);
		b = new ArrayDeque<>(t);
	}

	public T get(int i) {
		if (i < 0 || i >= size()) {
			throw new IndexOutOfBoundsException();
		}
		if (i < f.size()) {
			return f.get(i);
		} else {
			return b.get(i - f.size());
		}
	}
	public T set(int i, T n) {
		if (i < 0 || i >= size()) {
			throw new IndexOutOfBoundsException();
		}
		if (i < f.size()) {
			return f.set(i, n);
		} else {
			return b.set(i - f.size(), n);
		}
	}

	public void add(int i, T n) {
		if (i < 0 || i > size()) {
			throw new IndexOutOfBoundsException();
		}
		if (i < f.size()) {
			f.add(i, n);
		} else {
			b.add(i - f.size(), n);
		}
		balanceDeques();
	}

	public T remove(int i) {
		if (i < 0 || i >= size()) {
			throw new IndexOutOfBoundsException();
		}
		T n = null;
		if (i < f.size()) {
			n = f.remove(i);
		} else {
			n = b.remove(i - f.size());
		}
		balanceDeques();

		return n;
	}

	public void clear() {
		f.clear();
		b.clear();
	}

	public int size() {
		return f.size() + b.size();
	}


	protected void balanceDeques() {
		final double scale = 1.00001;
		if (scale * f.size() < b.size()) {
			while(f.size() < b.size()) {
				T removed = b.remove(0);
				f.add(f.size(), removed);
			}
		} else if (scale * b.size() < f.size()) {
			while(b.size() < f.size()) {
				T removed = f.remove(f.size() - 1);
				b.add(0, removed);
			}
		}
	}

}
