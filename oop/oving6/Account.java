package oving6;

/**
 * @author hakloev
 * public interface for Account
 */
public interface Account {

	// Method-declarations
	public int getBalance();
	public int getCredit();
	public int deposit(int depositSum); 
	public int withdraw(int withdrawSum);
	
}
