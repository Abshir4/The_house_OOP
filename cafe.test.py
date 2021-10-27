from shop_item import inventory
from account import Account


class Cafe:

    # Construct an Account object
    def __init__(self, inventory):
        self.inventory = inventory

    def add_item(self, key, value):
        # add any new item to the inventory
        # use dictionary modification/updation
        # dictionary_name[´key name'] = some value
        self.inventory[key] = value

    def remove_item(self, key):
        del self.inventory[key]
        # add any new item to the inventory

c1 = Cafe(inventory)
# if item already exists, it updates existing item value to new value
c1.add_item('Fanta',5)
# if the item is not present, it adds it to the inventory
c1.add_item('Fika',15)
print(c1.inventory)
c1.remove_item('Fanta')

# class which takes care of customers purchase details
class Orders():
    def __init__(self):
        self.purchase = []

# add to purchase if its found in the inventory
    def add_to_purchase(self, item):
        if item in self.inventory.keys():
            self.purchase.append(item)

    def remove_item_purchase(self, item):
        if item in self.purchase:
            self.purchase.remove(item)
            print(f"{item.capitalize()} was removed from your purchase.\n")

    def total_purchase(self, accountobj):
        if len(self.purchase) < 1:
            print("Please order something.")
        else:
            total = 0
            for item in self.purchase:
                total += self.inventory.get(item)
            print(f"Your total is ${total:.2f}")
            if self.balance >= total:
                purchase_command = input("Ready to pay? Yes or no\n").lower()
                if purchase_command[0] == "y":
                    print(f"You had ${self.balance:.2f}")
                    self.balance -= total
                    print(f"Thank you for your purchase, you have ${self.balance:.2f} remaining.\n")
                    self.purchase.clear()
            else:
                print(f"Sorry you only have ${self.balance:.2f}: and your total is {total:.2f}.\n")

    def display_total(self):
        if len(self.purchase) < 1:
            print("Please order something.")
        else:
            total = 0
            for item in self.purchase:
                total += self.inventory.get(item)
            print(f"Your total is ${total:.2f}")

    def display_order(self):
        if len(self.purchase) > 0:
            print("Purchase:")
            for item in self.purchase:
                print(f"     {item}")
            print(len(self.purchase))
        else:
            print("Your haven't ordered anything.\n")

# Display the inventory and format a string from our <dict> and remove certain objects.
    def display_inventory(self):
        inventory = str(self.inventory)
        inventory = inventory.replace("'", "")
        inventory = inventory.replace("{", "")
        inventory = inventory.replace("}", "")
        inventory = inventory.replace(": ", " $")
        inventory_list = inventory.split(", ")
        for item in inventory_list:
            print(item)

def buy():
    while True:
        buy_command = input("What would you like to order?.\n").lower()
        if buy_command == "help":
            print("\nYou may type food and drink")
            print("inventory = see the list of the inventory items to purchase and prices")
            print("stop = Stop adding i items in to your order.\n")
        elif buy_command == "food":
            shop.display_inventory()
            shop.add_to_purchase(buy_command)
        elif buy_command == "drink":
            shop.display_drink()
            shop.add_to_purchase(buy_command)
        elif shop.inventory.get(buy_command):
            shop.add_to_purchase(buy_command)
            print(f"{buy_command.capitalize()} was added to your order.\n")
        elif buy_command == "inventory":
            shop.display_inventory()
        elif buy_command == "stop":
            break
        else:
            print("Im sorry, i dont understand. Type Help for a list of commands")

#shop = Account()
def find_account(accounts):
    # Reading id from user
    pin = int(input("\nEnter account pin: "))
    # Loop till id is valid
    while pin < 1000 or pin > 9999:
        pin = int(input("\nInvalid Id.. Re-enter: "))
    # Getting account object
    for acc in accounts:
        # Comparing account id
        if acc.getPin() == pin:
            accountobj = acc
            break
    return accountobj

def home_cafe(accounts):
    while True:
        command = input("What would you like to do? write help to get assistance\n").lower()
        if command == "help":
            print("\nYou may type: buy leave, pay, total, remove, or balance")
            print("buy = Pick items to purchase.")
            print("leave = Stop the purchase.")
            print("pay = Get the total of your items and purchase them.")
            print("remove = Remove items from your your order.")
            print("total = See the what you have in your order")
            print("order = See all the items in your order. ")
            print("balance = See how much money you have.\n")
        elif command == "buy":
            buy()
        elif command == "leave":
            if command[0] == "l":
                print("Bye, have a nice day\n")
                break
        elif command == "pay":
            # have to keep record of accounts in the set
            accountobj = find_account(accounts)
            shop.total_purchase(accountobj)

        elif command == "total":
            shop.display_total()
        elif command == "remove":
            if len(shop.purchase) < 1:
                print("There are no items to remove.\n")
            else:
                remove_command = input("What item would you like to remove ").lower()
                shop.remove_item(remove_command)
        elif command == "order":
            shop.display_order()
        elif command == "balance":
            print(f"You have ${shop.balance:.2f}\n")
        else:
            print("Im sorry. I dont understand. Type help for of a list of commands.\n")