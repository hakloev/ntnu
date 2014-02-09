package oving6;

public class CreditAccount implements Account {
	
	private int balance;
	private int creditLimit;
	private final int CREDIT_FEE = 50;
	private int totalFee;
	
	public CreditAccount(int creditLimit) {
		this.balance = 0;
		this.creditLimit = creditLimit;
	}
	
	public int getFees() {
		return this.totalFee;
	}
	
	public void addFee() {
		this.totalFee += CREDIT_FEE; // adds fee to totalFee
		this.balance -= CREDIT_FEE; // adds fee to balance
	}

	@Override
	public int getBalance() {
		return this.balance;
	}

	@Override
	public int getCredit() {
		return this.creditLimit;
	}

	@Override
	public int deposit(int depositSum) {
		if (depositSum > 0) {
			this.balance += depositSum;
		}
		return this.balance;
	}

	@Override
	public int withdraw(int withdrawSum) {
		int nextBalance = this.balance - withdrawSum; // temp-variable for nextBalance without fee
		if (withdrawSum < 0) { // if withdrawSum are negative
			return 0;
		} else { // if withdrawSum are positive
			if ((nextBalance) < 0) { // if nextBalance is less than 0, we must add fee
				if ((nextBalance - CREDIT_FEE) >= -this.creditLimit) { // if nextBalance - CREDIT_FEE is larger than creditLimit
					addFee(); // adds fee to balance
					this.balance -= withdrawSum; // withdraws withdrawSum
				} else { // if nextBlanace - CREDIT_FEE is less than creditLimit we cant withdraw
					return 0;
				}
			} else { // if withdrawSum are larger than 0
				this.balance -= withdrawSum; 
			}
		}
		return withdrawSum; // always return withdrawSum as default else
	}
	
	
	
}
