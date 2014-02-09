// Håkon Ødegård Løvdal
// TDT4100 

package oving1;

import acm.program.ConsoleProgram;

public class Calc2 extends ConsoleProgram{
	
	double a, b, result;
	String operator; 
	
	public void init() {
		
	}
	
	public void run() {
		a = readDouble("First operand: ");
		b = readDouble("Second operand: ");
		operator = readLine("Operator: ");
		print("The result of " + a + operator + b + " is " + performOperation(operator));
	}
	
	private double performOperation (String operator) {
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

