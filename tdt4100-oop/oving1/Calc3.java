// Håkon Ødegård Løvdal
// TDT4100 

package oving1;

import acm.program.ConsoleProgram;

public class Calc3 extends ConsoleProgram{
	
	double a, b, result;
	String operator; 
	
	public void init() {
		
	}
	
	public void run() {
		a = readDouble("First operand: ");
		b = readDouble("Second operand: ");
		operator = readLine("Operator: ");
		performOperation();
		print("The result of " + a + operator + b + " is " + result);
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