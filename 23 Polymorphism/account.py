class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.index = 0

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        account._transactions = self._transactions + other._transactions
        return account