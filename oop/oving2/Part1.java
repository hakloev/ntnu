/*  Håkon Ødegård Løvdal
 *  Øving 2 - Deloppgave 1
 *  
 */

package oving2;


import java.util.EmptyStackException;
import java.util.Stack;
import acm.program.ConsoleProgram; 

public class Part1 extends ConsoleProgram {
	// initaliserer stacken numbers 
	Stack<Double> numbers = new Stack<Double>();
	
	public void init() {
		
	}
	// run-metoden
	public void run() {
		while (true) {
			String input = readLine("Enter choice: "); // input fra brukeren
			if (input.equals("Q") || input.equals("q")) {
				Double answer = pop();
				if (answer == 0.0) {
					print("The stack was empty, no answer!");
					break;					
				} else {
					print("The answer is: " + answer);
					break;
				}
			} else if (input.equals(".")) { // pop
				Double popped = pop();
				if (popped != 0.0) {
					print("The number " + popped + " was popped\n");					
				} else {
					print("The stack is empty!\n");
				}
			} else if (input.equals(",")) { // duplicate
				duplicate();
				// operator-check
			} else if ("+-/*".contains(input)) {
				performOperation(input);
			} else { // operand-input
				try{
				Double number = Double.parseDouble(input);
				push(number);
				printStack();
				}
				catch (NumberFormatException e) {
					print("Can't input empty string, try again!\n");
				}
			}
		}
	}
	
	// performOperation, utfører utregning hvis mulig, tar inn operator
	void performOperation(String input) {
		Double b = pop(), a = pop();
		Double result = null;
		char operator = input.charAt(0);
		if (b == 0.0 && a == 0.0) {
			print("The stack is empty, can't perform operation " + input + "\n");
			return;
		} else if (b == 0.0 || a == 0.0) {
			print("One of the operators doesn't exsist, I will push back the number!\n");
			if (b == 0.0) {
				push(a);
				printStack();
				return;
			} else {
				push(b);
				printStack();
				return;
			}
		}
		switch (operator) {
			case '+': result = b + a; break;
			case '-': result = a - b; break;
			case '*': result = b * a; break;
			case '/': result = a / b; break;
		}
		push(result);
		print("The number " + result + " was pushed to the stack!\n");
		printStack();
	}
	
	// pop-metode, fjerner en fra stack
	Double pop() {
		if (!numbers.empty()) {
			return (Double)numbers.pop();
		}
		return 0.0;
	}
	
	// duplicate-metode, kopierer øverste i stack
	void duplicate() {
		Double a = null;
		try {
			a = (Double)numbers.peek();
			push(a);
			print("The number " + a + " was duplicated!\n");
			printStack();
		}
		catch (EmptyStackException e) {
			print("The stack is empty, can't duplicate!\n");
		}
	}
	
	// printStack-metode, printer hele stacken
	void printStack() {
		for (int i = numbers.size() - 1; i >= 0; i--) {
			print(numbers.elementAt(i) + "\n");
		}
	}
	// push-metode, pusher operand til toppen av stacken
	void push(Double p) {
		numbers.push(new Double(p));
	}
}