class InsufficientBalance(Exception):
    def __init__(self, amount_needed, amount_got):
        self.amount_needed = amount_needed
        self.amount_got = amount_got

    def __str__(self):
        base = super().__str__()
        return f"{base} | User tried to perform an action that requires {self.amount_needed} coins, but they only have {self.amount_got} coins."