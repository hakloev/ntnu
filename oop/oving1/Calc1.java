// Håkon Ødegård Løvdal
// TDT4100 

package oving1;

import acm.program.ConsoleProgram;

public class Calc1 extends ConsoleProgram {
	
	public void init() {
		
	}
	
	public void run() {
		
		double a, b;
		a = readDouble("First operand: ");
		b = readDouble("Second operand: ");
		String operator = readLine("Operand: ");
		print("The result of " + a + operator + b + " is " + performOperation(a, b, operator));
	}
	
	private double performOperation (double a, double b, String operator) {
		double result = 0;
		if (operator.equals("+")) {
			result = (a + b);
		} else if (operator.equals("-")) {
			result = (a - b);
		} else if (operator.equals("*")) {
			result = (a * b);
		} else if (operator.equals("/")) {
			result = (a / b);
		}
		return result;
	}
}