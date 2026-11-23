products = {
    "rice": 75,
    "milk": 90,
    "bread": 55,
    "egg": 15,
    "apple": 180,
    "oil": 190,
    "sugar": 130,
    "salt": 45,
    "soap": 60,
    "tea": 220
}

print("Available products:")
for name, price in products.items():
    print(name, "-", price)

order = {}  # (d) accumulated quantity of each ordered product

while True:
    item = input("\nEnter product name (or 'done' to finish): ").lower()

    if item == "done":
        break

    if item not in products:
        print("Product not available")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity")
        continue

    if item in order:
        order[item] += quantity
    else:
        order[item] = quantity

print("\n----------- BILL -----------")
print("Product    Unit Price    Qty    Total")

grand_total = 0
for item, qty in order.items():
    unit_price = products[item]
    item_total = unit_price * qty
    grand_total += item_total
    print(item, "   ", unit_price, "   ", qty, "   ", item_total)

# (g) Grand total
print("----------------------------")
print("Grand Total:", grand_total)