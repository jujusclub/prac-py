package BackJun;
/**
 * left48
 * 문제
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

출력
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
 */
import java.util.Scanner;

public class left48 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] num = new int[10];
        boolean[] numlefts = new boolean[42]; // 나머지가 들어 갈 수 있는 리스트

        System.out.println("정수 10개를 입력하세요:");

        // 사용자가 모든 숫자를 입력할 때까지 대기
        for (int i = 0; i < 10; i++) {
            System.out.print("정수 #" + (i + 1) + ": ");
            num[i] = scanner.nextInt();
            int numleft = num[i] % 42;
            numlefts[numleft] = true; // 해당값을 해당 자리에 넣고
        }
        
        // 사용자가 모든 숫자를 입력한 후 Enter를 누르면 출력 시작
        System.out.println("서로다른 나머지 :");

        int leftCount = 0;
        for (boolean count : numlefts){
            if  (count == true ){
                leftCount++;
            }
        
        }

        System.out.println(leftCount);
    }
}