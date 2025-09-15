
# class Fruits:

#     def __init__(self, text: list):
#         self.text = text

#     def sort_fruit(self) -> list:
#         return [x for x in self.text if "a" in x]


# def main():
#     fruits_ls = ["apple", "banana", "cherry", "kiwi", "mango"]
#     fruits = Fruits(fruits_ls)
#     print(f"Fruits have 'a' in name is: {fruits.sort_fruit()}")


class Final_Bill:

    def __init__(self, transactions: list[float]):
        self.transactions = transactions

    def calculate_bill(self):
        TAX = 0.08
        SERVICE_CHARGE = 0.07
        return [
            round(bill*(1 + TAX + SERVICE_CHARGE), 3)
            for bill in self.transactions
        ]


def main():
    transactions_ls = [100, 250.5, 3000, 400]
    final_bill = Final_Bill(transactions_ls)
    print(f"Finall bill are: {final_bill.calculate_bill()}")


if __name__ == "__main__":
    main()
