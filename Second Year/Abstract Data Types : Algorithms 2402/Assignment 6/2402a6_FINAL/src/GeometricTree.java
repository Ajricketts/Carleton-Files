
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.Stack;

public class GeometricTree extends BinaryTree<GeometricTreeNode> {

	public GeometricTree() {
		super (new GeometricTreeNode());
	}

	public void inorderDraw() {
		assignLevels();
		// TODO: use your code here instead
		GeometricTreeNode w = firstNode();
		for (int i = 0; w!=nil;i++){
			w.position.x = i;
			w = nextNode(w);
		}
	}


	protected void randomX(GeometricTreeNode u, Random r) {
		if (u == null) return;
		u.position.x = r.nextInt(60);
		randomX(u.left, r);
		randomX(u.right, r);
	}


	/**
	 * Draw each node so that it's x-coordinate is as small
	 * as possible without intersecting any other node at the same level 
	 * the same as its parent's
	 */
	public void leftistDraw() {
		assignLevels();

		GeometricTreeNode k = r;
		k.position.x = 0;

		Queue<GeometricTreeNode> q = new LinkedList<GeometricTreeNode>();
		q.add(r);
		while (!q.isEmpty()) {
			GeometricTreeNode u = q.remove();

			if (k.position.y == u.position.y) {
				u.position.x = k.position.x + 1;
				k = u;
			} else {
				u.position.x = 0;
				k = u;
			}

			if (u.left != nil) {
				q.add(u.left);
			}
			if (u.right != nil) {
				q.add(u.right);
			}
		}

		r.position.x = 0;
	}


	public void balancedDraw() {
		assignLevels();
		Random rand = new Random();
		randomX(r, rand);
	}

	protected void assignLevels() {
//		GeometricTreeNode temp = firstNode();
//
//		for (int i = 0; temp != nil; i++) {
//			if(height(r) == depth(temp)) {
//				temp.position.y = height(r);
//				temp = nextNode(temp);
//			}
//
//			else {
//				temp.position.y = depth(temp) - height(r);
//				temp = nextNode(temp);
//			}
//		}
		Stack<GeometricTreeNode> temp = new Stack<>();
		GeometricTreeNode u = r;
		temp.add(u);
		int count = 0;
		while (!temp.isEmpty()) {
			u = temp.pop();
			h = temp.pop();
			u.position.y = count;
			count++;
			if (u.left != null && u.right != null) {
				temp.add(u.left);
				temp.add(u.right);
			}

		}
		//assignLevels(r, 0);

	}

	protected void assignLevels(GeometricTreeNode u, int i) {
		if (u == null) return;
		u.position.y = i;
		assignLevels(u.left, i+1);
		assignLevels(u.right, i+1);
	}

	public static void main(String[] args) {
		GeometricTree t = new GeometricTree();
		galtonWatsonTree(t, 100);
		System.out.println(t);
		t.inorderDraw();
		System.out.println(t);
	}

}