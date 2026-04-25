import sys

print("=== Inventory System Analysis ===")
inventory = {}
for arg in range(1, len(sys.argv)):
    parts = sys.argv[arg].split(":")
    if len(parts) != 2:
        print(f"Error- invalid parameter '{sys.argv[arg]}'")
        continue
    if parts[0] in inventory:
        print(f"Redundant item '{parts[0]}'- discarding")
        continue
    try:
        inventory.update({parts[0]: int(parts[1])})
    except ValueError as e:
        print(f"Quantity error for '{parts[0]}': {e}")

if len(inventory) == 0:
    print("No items provided.")
else:
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(inventory.values())}")

    total = sum(inventory.values())
    for item in inventory.keys():
        quantity = inventory[item]
        percent = round(quantity / total * 100, 1)
        print(f"Item {item} represents {percent}%")

    most = list(inventory.keys())[0]
    least = list(inventory.keys())[0]

    for item in inventory.keys():
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
