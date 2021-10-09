stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))



#BE CAREFUL OF {} <-- THIS MAKES A SET AND THEN EACH GOLD COIN BELOW ONLY COUNTS ONCE SO USE A LIST
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {
    'gold coin': 42,
    'rope': 1
}


def addToInventory(inventory, addedItems):
    for items in addedItems:
        if items in inventory:
            inventory[items] = inventory[items] + 1
        else:
            inventory[items] = 1
    return inventory


def main():
    addToInventory(inv, dragonLoot)
    displayInventory(inv)


if __name__ == '__main__':
    main()
