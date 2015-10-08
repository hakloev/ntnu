// Håkon Ødegård Løvdal
// TDT4100 

package oving1;

import acm.program.ConsoleProgram;

public class Calc4 extends ConsoleProgram{
	
	double a, b, result=0;
	String operator; 
	
	public void init() {
		
	}
	
	public void run() {
		answerCheck();
	}
	
	private void answerCheck() {
		while (result <= 1337) {
			a = readDouble("First operand: ");
			b = readDouble("Second operand: ");
			operator = readLine("Operator: ");
			performOperation(); 
			print("The result of " + a + operator + b + " is " + result + "\n");
		}
		print("The result was over 1337, so I stopped!");
	}
	
	private void performOperation () {
		if (operator.equals("+")) {
			result = (a + b);
		} else if (operator.equals("-")) {
			result = (a - b);
		} else if (operator.equals("*")) {
			result = (a * b);
		} else if (operator.equals("/")) {
			result = (a / b);
		}
	}
}