class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    def set_amount(self, amount):
        self.amount = amount

    def in_currency(self, amount):
        return amount / self.exchange_to_usd

    def to_usd(self, amount=None):
        to_convert = amount or self.amount
        # to_convert = amount if amount is not None else self.amount
        return amount * self.exchange_to_usd

    def __gt__(self, other):  # greater than
        return self.exchange_to_usd > other.exchange_to_usd


pounds = Currency("GBP", 1.21)
euros = Currency("EUR", 1.07)

print(pounds > euros)


