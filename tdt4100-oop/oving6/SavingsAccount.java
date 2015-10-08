package oving6;

public class SavingsAccount implements Account {
	
	private int balance;
	
	public SavingsAccount() {
		this.balance = 0;
	}
	
	@Override
	public int getBalance() {
		return this.balance;
	}

	@Override
	public int getCredit() {
		return 0;
	}

	@Override
	public int deposit(int depositSum) {
		if (depositSum >= 0) {
			this.balance += depositSum;			
		}
		return this.balance;
	}

	@Override
	public int withdraw(int withdrawSum) {
		if ((withdrawSum < 0) || this.balance < withdrawSum) { // is withdrawSum is less than 0 or balance is less than withdrawSum
			return 0;
		} else {
			this.balance -= withdrawSum;
			return withdrawSum;			
		}
	}

}
