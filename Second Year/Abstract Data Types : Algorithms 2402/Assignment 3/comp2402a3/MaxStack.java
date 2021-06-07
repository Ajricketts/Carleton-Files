package comp2402a3;
import java.util.Stack;


/**
 * An implementation of a Stack that also can efficiently return  
 * the maximum element in the current Stack.  Every operation -
 * push, pop, peek, and max - must run in constant time
 *
 * @param <T> the class of objects stored in the queue
 */
public class MaxStack<T extends Comparable<T>> extends SLListStack<T> {

	// Add any structures you need here...
	Stack<T> stack;

	public MaxStack() {
		stack = new Stack<T>();
	}

	public int compareTo(T x) {
		return stack.peek().compareTo(x);
	}

	public T push(T s) {
		if (stack.empty()) {
			stack.push(s);
		}
		else {
			if (compareTo(s)<=0) {
				stack.push(s);
			}
		}
		return super.push(s);
	}

	public T pop() {
		T holder = super.pop();
		if (holder == stack.peek()) {
			stack.pop();
		}
		return holder;
	}

	public T max(){
		if (stack.isEmpty()) {
			return null;
		}

		else {
			return stack.peek();
		}
	}

	public static void main(String[] args){
		
		MaxStack<Character> stack = new MaxStack<Character>();
		
		String datasequence = "ABXRTSXY";
		for (int i = 0; i < datasequence.length(); i++){
			stack.push(datasequence.charAt(i));
			System.out.println(stack + ", max = " + stack.max());
		}
		while(stack.size() > 0) {
			stack.pop();
			System.out.println(stack + ", max = " + stack.max());
		}
		
		
	}

}
