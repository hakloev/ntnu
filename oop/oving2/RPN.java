/*  Håkon Ødegård Løvdal
 *  Øving 2 - Deloppgave 2
 *  
 */

package oving2;

import java.util.EmptyStackException;
import java.util.Stack;

public class RPN {
	
	Stack<Double> operands = new Stack<Double>();
	
	int getOperandCount() {
		return operands.size();
	}
	
	double peek(int n) {
		return (operands.elementAt((operands.size() - 1) - n));
	}
	
	void push(double defaultValue) {
		operands.push(new Double(defaultValue));
	}
	
	double pop(double defaultValue) {
		if (!operands.empty()) {
			return operands.pop();
		} 
		return defaultValue;
	}
	
	void performOperation(char operator) {
		Double b = operands.pop();
		Double a = operands.pop();
		Double result = null;
		switch (operator) {
//			case ',': duplicate();
			case '+': result = b + a; break;
			case '-': result = a - b; break;
			case '*': result = b * a; break;
			case '/': result = a / b; break;
		}
		push(result);
		
	}

//	void duplicate() {
//		Double a = null;
//		try {
//			a = (Double)operands.peek();
//			push(a);
//		}
//		catch (EmptyStackException e) {
//		}
//	}
}
