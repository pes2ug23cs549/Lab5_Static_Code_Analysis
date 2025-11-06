import json
import logging  

# Global variable
stock_data = {}


def addItem(item_name, quantity, stock_data=None):
    """Add a new item to inventory or update its quantity."""
    # Fix for W0102: avoid mutable default []
    if stock_data is None:
        stock_data = []

    # Adds item to stock
    if item_name in stock_data:
        stock_data[item_name] += quantity
    else:
        stock_data[item_name] = quantity
    print(f"Added {quantity} of {item_name}")


def removeItem(item, stock_data):
    """Remove item from stock."""
    try:
        del stock_data[item]
    # Fix for W0702/E722: avoid bare except
    except KeyError:
        print(f"Item '{item}' not found in stock data.")


def getQty(item, stock_data):
    """Get the quantity of an item."""
    return stock_data.get(item, 0)


def loadData():
    """Load inventory data from a file."""
    global stock_data  
    # Fix for R1732: use context manager + encoding
    try:
        with open("inventory_data.json", "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        stock_data = {}
    return stock_data


def saveData(stock_data):
    """Save inventory data to a file."""
    # Fix for R1732: use context manager + encoding
    with open("inventory_data.json", "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)
    print("Inventory data saved successfully.")


def printData(stock_data):
    """Print all items in the inventory."""
    print("Current Inventory:")
    for item, qty in stock_data.items():
        print(f"{item}: {qty}")


def checkLowItems(stock_data, threshold=5):
    """Check and print items below the threshold quantity."""
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    if low_items:
        print("Low stock alert for items:")
        for item in low_items:
            print(f"  - {item}")
    else:
        print("All items are sufficiently stocked.")

if __name__ == "__main__":
    stock_data = loadData()
    addItem("Apples", 10, stock_data)
    removeItem("Bananas", stock_data)
    printData(stock_data)
    checkLowItems(stock_data)

    saveData(stock_data)

    # Fix for B307/W0123: Removed insecure eval() usage
    print("Inventory check completed safely.")
