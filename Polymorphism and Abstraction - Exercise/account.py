class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @staticmethod
    def handle_transaction(account, transaction_amount):
        if account.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(transaction_amount)
        return f"New balance: {account.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        if self.balance + amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(amount)
        return f"New balance: {self.balance}"

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, idx):
        return self._transactions[idx]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        name = f'{self.owner}&{other.owner}'
        amount = self.amount + other.amount
        account = Account(name, amount)
        transactions = self._transactions + other._transactions
        account._transactions = transactions
        return account
