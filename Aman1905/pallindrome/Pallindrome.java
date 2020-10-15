package pallindrome;
import java.util.Scanner;

public class Pallindrome {

	public static void main(String[] args) {
	Scanner sc  = new Scanner(System.in);
	
	int n = sc.nextInt();
	int temp = n;
	int rev = 0;
	
	while(temp>0) {
		
		int lastDigit = temp %10;
		rev = rev*10 + lastDigit;
		temp /= 10;
	}
	
	if (rev==n) {
		System.out.println("Pallindrome");
	}
	
	else {
		System.out.println("Not a Pallindrome");
	}
	
	}

}
