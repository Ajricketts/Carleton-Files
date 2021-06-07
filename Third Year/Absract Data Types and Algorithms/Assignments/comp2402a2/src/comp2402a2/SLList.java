package comp2402a2;

import java.util.AbstractList;
import java.util.Iterator;
import java.util.Queue;
import java.util.NoSuchElementException;

/**
 * An implementation of a FIFO Queue as a singly-linked list.
 * This also includes the stack operations push and pop, which
 * operate on the head of the queue
 * @author morin
 *
 * @param <T> the class of objects stored in the queue
 */
public class SLList<T> extends AbstractList<T> implements Queue<T> {
	class Node {
		T x;
		Node next;
	}

	/**
	 * Front of the queue
	 */
	Node head;

	/**
	 * Tail of the queue
	 */
	Node tail;

	/**
	 * The number of elements in the queue
	 */
	int n;

	public T get(int i) {
		// TODO: Implement this
		if (i < 0 || i > n - 1) throw new IndexOutOfBoundsException();

		Node temp = head;

		for (int j = 0; j < i; j++) {
			temp = temp.next;
		}
		return temp.x;
	}

	public T set(int i, T x) {
		// TODO: Implement this
		if (i < 0 || i > n - 1) throw new IndexOutOfBoundsException();

		Node temp = head;

		for (int j = 0;j < i; j++) {
			temp = temp.next;
		}
		T data = temp.x;
		temp.x = x;
		return data;
	}

	public void add(int i, T x) {
		// TODO: Implement this
		if (i < 0 || i > n) throw new IndexOutOfBoundsException();

		Node newNode = new Node();
		newNode.x = x;

		if (n == 0) {
			add(x);
		}

		else if (i == 0) {
			Node temp = head;
			head = newNode;
			head.next = temp;
			++n;
		}


		else {

			Node temp1 = head;

			for (int j = 0; j < i - 1; j++) {
				temp1 = temp1.next;
			}

			if (temp1.next == tail) {
				add(x);
			}

			else {
				addAfter(temp1,newNode);
				++n;
			}
		}

	}

	public T remove(int i) {
		// TODO: Implement this
		if (i < 0 || i > n - 1) throw new IndexOutOfBoundsException();
		if (i == 0 && n > 1) {
			head = head.next;
			--n;
			return head.x;
		}

		else if (n == 1) {
			Node temp = head;
			head = null;
			tail = null;
			n--;
			return temp.x;
		}

		else {
			Node temp = head;

			for (int j = 0; j < i - 1; j++) {
				temp = temp.next;
			}
			deleteNext(temp);
			--n;

			return temp.x;
		}
	}

	public void reverse() {
		// TODO: Implement this
		Node curr = head;
		Node prev = null, next = null;

		if (n == 0) {
			return;
		}

		else {

			while (curr != null) {
				// Store the next node
				next = curr.next;
				// Make the current nodes next point to the one before it (flip the nodes)
				curr.next = prev;
				// Make previous be the current node, and move to the next node
				prev = curr;
				curr = next;
			}
			tail = head;
			head = prev;
		}

	}

	public void printList() {
		Node temp = head;

		System.out.print("\n[");
		for (int j = 0; j < n; j++) {
			if (temp.x != null) {
				System.out.print(" -> ");
				System.out.print(temp.x);
			}
			temp = temp.next;
		}
		System.out.print("]");
	}

	public Iterator<T> iterator() {
		class SLIterator implements Iterator<T> {
			protected Node p;

			public SLIterator() {
				p = head;
			}
			public boolean hasNext() {
				return p != null;
			}
			public T next() {
				T x = p.x;
				p = p.next;
				return x;
			}
			public void remove() {
				throw new UnsupportedOperationException();
			}
		}
		return new SLIterator();
	}

	public int size() {
		return n;
	}

	public boolean add(T x) {
		Node u = new Node();
		u.x = x;
		if (n == 0) {
			head = u;
		} else {
			tail.next = u;
		}
		tail = u;
		n++;
		return true;
	}

	public boolean offer(T x) {
		return add(x);
	}

	public T peek() {
		if (n == 0) return null;
		return head.x;
	}

	public T element() {
		if (n == 0) throw new NoSuchElementException();
		return head.x;
	}

	public T poll() {
		if (n == 0)
			return null;
		T x = head.x;
		head = head.next;
		if (--n == 0)
			tail = null;
		return x;
	}

	/**
	 * Stack push operation - push x onto the head of the list
	 * @param x the element to push onto the stack
	 * @return x
	 */
	public T push(T x) {
		Node u = new Node();
		u.x = x;
		u.next = head;
		head = u;
		if (n == 0)
			tail = u;
		n++;
		return x;
	}

	protected void deleteNext(Node u) {
		if (u.next == tail)
			tail = u;
		u.next = u.next.next;
	}

	protected void addAfter(Node u, Node v) {
		v.next = u.next;
		u.next = v;
		if (u == tail)
			tail = v;
	}

	protected Node getNode(int i) {
		Node u = head;
		for (int j = 0; j < i; j++)
			u = u.next;
		return u;
	}

	/**
	 * Stack pop operation - pop off the head of the list
	 * @return the element popped off
	 */
	public T remove() {
		if (n == 0)	return null;
		T x = head.x;
		head = head.next;
		if (--n == 0) tail = null;
		return x;
	}

	public T pop() {
		if (n == 0)	return null;
		T x = head.x;
		head = head.next;
		if (--n == 0) tail = null;
		return x;
	}


	public static void main(String[] args) {
		SLList list = new SLList();

		for (int i = 0; i < 800; i++) {
			list.add(i,i);
		}


		//list.add(5,15);
		//list.add(list.n,30);
		list.printList();
		System.out.println("\n" +list.n);
		//list.add(400,20);
		//list.remove(3);
		//list.printList();

		list.reverse();
		list.printList();
		System.out.print("\n" + list.get(799));
		System.out.print("\n" + list.head.x);
		System.out.print("\n" + list.tail.x);

		list.reverse();
		list.printList();
		System.out.print("\n" + list.head.x);
		System.out.print("\n" + list.tail.x);


		list.set(list.n-1,21);
		list.printList();
		System.out.print("\n" + list.get(list.n-1));


		list.remove(0);
		list.printList();
		System.out.println("\n" +list.n);





	}
}
