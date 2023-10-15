class Member:
    members = []

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.purchase_history = []
        Member.members.append(self)

    @staticmethod
    def find_member(member_id):
        for member in Member.members:
            if member.member_id == member_id:
                return member
        return None

    def view_purchase_history(self):
        for transaction in self.purchase_history:
            print(f"Transaction ID: {transaction.transaction_id}, Items: {transaction.items}")


class Item:
    items = []

    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
        Item.items.append(self)

    @staticmethod
    def find_item(item_id):
        for item in Item.items:
            if item.item_id == item_id:
                return item
        return None


class Transaction:
    def __init__(self, transaction_id, member, items):
        self.transaction_id = transaction_id
        self.member = member
        self.items = items
        member.purchase_history.append(self)

def main_menu():
    while True:
        print("Welcome to the Retail Store Management Program!")
        print("1. Member Management")
        print("2. Item Management")
        print("3. Inventory Viewing")
        print("4. Transaction Processing")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            member_management()
        elif choice == "2":
            item_management()
        elif choice == "3":
            inventory_viewing()
        elif choice == "4":
            transaction_processing()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
