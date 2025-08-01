import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int lineCount = Integer.parseInt(br.readLine());

        for (int i = 1; i <= lineCount; i++) {
            for(int f = lineCount - i; f > 0; f--){
                bw.write(" ");
            }
            for(int j = 0; j < i; j++){
                bw.write("*");
            }
            bw.newLine();
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
