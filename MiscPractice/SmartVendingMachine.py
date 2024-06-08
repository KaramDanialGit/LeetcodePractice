# Design a smart vending machine

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class VendingMachine:
    def __init__(self, id, items):
        self.id = id
        self.items = items

    def remove_item(self, row, col):
        if self.items[row, col]:
            self.items[row, col] -= 1
        else:
            print("We are out of this item")


words = "Ajax Location"
id = sum(ord(words[i]) * i for i in range(len(words)))
items = {"KitKat": 10, "Snickers": 10, "OH Henry": 4}

myMachine = VendingMachine(id, items)
print(myMachine.items)
