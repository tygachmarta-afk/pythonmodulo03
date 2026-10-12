#!/usr/bin/env python3

import sys


def main():
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name = parts[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            qty = int(parts[1])
        except ValueError as err:
            print(f"Quantity error for '{name}': {err}")
            continue
        inventory.update({name: qty})

    print("Got inventory:", inventory)
    items = list(inventory.keys())
    print("Item list:", items)
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    if total == 0:
        print("Nothing to analyze.")
        return

    for item in items:
        percent = round(inventory[item] / total * 100, 1)
        print(f"Item {item} represents {percent}%")

    most = items[0]
    least = items[0]
    for item in items:
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()