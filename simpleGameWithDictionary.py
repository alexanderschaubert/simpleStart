stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print(stuff.items())

def display_inventory(inventory):
 print("Inventory:")
 item_total = 0
 for k, v in inventory.items():
     print(str(k) + ' ' + str(v))
     item_total+= v
 print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):

inv = {'gold coin': 42,  'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'rubby']
inv = addToInventory(inv, dragonLoot)
display_inventory(inv)
display_inventory(stuff)