class InsufficientBalance(Exception):
    def __init__(self, amount_needed, amount_got):
        self.amount_needed = amount_needed
        self.amount_got = amount_got
        super().__init__(
            f"User tried to perform an action that requires {self.amount_needed} coins, "
            f"but they only have {self.amount_got} coins."
        )

    def __str__(self):
        return super().__str__()