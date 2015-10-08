package oving6;

import java.util.ArrayList;

public class AccountOverview {
	
	private ArrayList<Account> accounts;
	
	/**
	 * Constructor, initialices accounts-list
	 */
	public AccountOverview() {
		accounts = new ArrayList<Account>();
	}
	
	public int getAccountCount() {
		return accounts.size();
	}
	
	// get Acconunt-object
	public Account getAccount(int index) {
		if ((index >= 0) && (index < accounts.size())) {
			return accounts.get(index); 
		}
		return null;
	}
	
	public void addAccount(Account account) {
		if (!this.accounts.contains(account)) { // if not in list, add 
			this.accounts.add(account);
		}
 	}
	
	public int getTotalBalance() {
		int totalBalance = 0; // temp-variable for totalBalance
		for (Account ac : this.accounts) {
			totalBalance += ac.getBalance();
		}
		return totalBalance;
	}
	
	public int getTotalCredit() {
		int totalCredit = 0;
		for (Account ac : this.accounts) {
			totalCredit += ac.getCredit();
		}
		return totalCredit;
	}
	
	public int getTotalFees() {
		int totalFee = 0;
		for (Account ac : this.accounts) { // itterate over accounts
			if (ac instanceof CreditAccount) { // if ac is instance of CreditAccount, we can cast it and get getFees
				totalFee += ((CreditAccount) ac).getFees();
			}
		}
		return totalFee;
	}
}
