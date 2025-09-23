"""
Create Currency Changer
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class CurrencyConverter:
    """Dataclass to convert currency using fixed rates"""
    rates: dict = field(default_factory=lambda: {
        "USD": 1.0,
        "EUR": 0.92,
        "GPB": 0.79,
        "JPY": 146.8,
        "VND": 26350.0
    })

    def convert(self, amount: float, from_currency: str, to_currency: str):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency")

        amount_in_usd = amount / self.rates[from_currency]
        return amount_in_usd * self.rates[to_currency]


def main():
    converter = CurrencyConverter()
    try:
        amount = float(input("Enter amount: "))
        from_cur = input("From currency (USD, EUR, GBP, JPY, VND): ")
        to_cur = input("To currency (USD, EUR, GBP, JPY, VND): ")
        result = converter.convert(amount, from_cur, to_cur)
        print(f"{amount:.2f} {from_cur.upper()} = {result:.2f} {to_cur.upper()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
