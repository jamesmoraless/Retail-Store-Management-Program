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

def member_management():
    while True:
        print("\nMember Management")
        print("1. Add Member")
        print("2. Update Member")
        print("3. View Purchase History")
        print("4. Return to Main Menu")

        choice = input("Enter Choice: ")

        if choice == "1":
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Member Name: ")
            Member(member_id, name)
            print(f"Member {name} added!")

        elif choice == "2":
            member_id = int(input("Enter Member ID to update: "))
            member = Member.find_member(member_id)
            if member:
                new_name = input("Enter New Member Name: ")
                member.name = new_name
                print(f"Member {member_id} updated!")
            else:
                print("Member not found!")

        elif choice == "3":
            member_id = int(input("Enter Member ID to view purchase history: "))
            member = Member.find_member(member_id)
            if member:
                member.view_purchase_history()
            else:
                print("Member not found!")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def item_management():
    while True:
        print("\nItem Management")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Return to Main Menu")

        choice = input("Enter Choice: ")

        if choice == "1":
            item_id = int(input("Enter Item ID: "))
            name = input("Enter Item Name: ")
            price = float(input("Enter Item Price: "))
            Item(item_id, name, price)
            print(f"Item {name} added!")

        elif choice == "2":
            item_id = int(input("Enter Item ID to update: "))
            item = Item.find_item(item_id)
            if item:
                new_name = input("Enter New Item Name: ")
                new_price = float(input("Enter New Item Price: "))
                item.name = new_name
                item.price = new_price
                print(f"Item {item_id} updated!")
            else:
                print("Item not found!")

        elif choice == "3":
            item_id = int(input("Enter Item ID to remove: "))
            item = Item.find_item(item_id)
            if item:
                Item.items.remove(item)
                print(f"Item {item_id} removed!")
            else:
                print("Item not found!")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def inventory_viewing():
    print("\nInventory Viewing")
    for item in Item.items:
        print(f"Item ID: {item.item_id}, Name: {item.name}, Price: ${item.price}")

