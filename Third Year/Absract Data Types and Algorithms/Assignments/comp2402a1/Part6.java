package comp2402a1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Part6 {

    /**
     * Your code goes here - see Part0 for an example
     * @param r the reader to read from
     * @param w the writer to write to
     * @throws IOException
     */
    public static void doIt(BufferedReader r, PrintWriter w) throws IOException {
        // Your code goes here - see Part0 for an example

        //String s = r.readLine();
        ArrayList<String> a = new ArrayList<String>();
        //a.add(s);

        for (String line = r.readLine(); line != null; line = r.readLine()) {
//
            boolean flag = true;
            if (!a.contains(line)) {
                a.add(line);
            }
            //a.add(line);


            for (int i = 0; i < a.size() - 1; i++) {
                //if (a.get(i).endsWith(line)) {
                if(line.length() <= a.get(i).length()) {
                    //if (a.get(i).endsWith(line)) {
                    if(a.get(i).substring(a.get(i).length()-line.length()).equals(line)){
                        flag = false;
                        break;
                   }
                }

            }

            if (flag) {
                w.println(line);
            }
        }

    }

    /**
     * The driver.  Open a BufferedReader and a PrintWriter, either from System.in
     * and System.out or from filenames specified on the command line, then call doIt.
     * @param args
     */
    public static void main(String[] args) {
        try {
            BufferedReader r;
            PrintWriter w;
            if (args.length == 0) {
                r = new BufferedReader(new InputStreamReader(System.in));
                w = new PrintWriter(System.out);
            } else if (args.length == 1) {
                r = new BufferedReader(new FileReader(args[0]));
                w = new PrintWriter(System.out);
            } else {
                r = new BufferedReader(new FileReader(args[0]));
                w = new PrintWriter(new FileWriter(args[1]));
            }
            long start = System.nanoTime();
            doIt(r, w);
            w.flush();
            long stop = System.nanoTime();
            System.out.println("Execution time: " + 10e-9 * (stop-start));
        } catch (IOException e) {
            System.err.println(e);
            System.exit(-1);
        }
    }
}

