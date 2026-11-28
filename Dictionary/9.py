stock = {"pen": 10, "book": 5, "bag": 2}
transactions = [
    {"type": "receive", "item": "pen", "quantity": 4},
    {"type": "sell", "item": "book", "quantity": 3},
    {"type": "sell", "item": "bag", "quantity": 5},
    {"type": "receive", "item": "ruler", "quantity": 6},
    {"type": "sell", "item": "pen", "quantity": 8}
]

accepted = 0
rejected = 0

for t in transactions:
    item = t["item"]
    qty = t["quantity"]

    if t["type"] == "receive":
        stock[item] = stock.get(item, 0) + qty
        accepted += 1
    elif t["type"] == "sell":
        if stock.get(item, 0) >= qty:
            stock[item] -= qty
            accepted += 1
        else:
            print(f"Rejected: cannot sell {qty} {item} (available: {stock.get(item, 0)})")
            rejected += 1

print("Final stock:", stock)
print("Accepted:", accepted)
print("Rejected:", rejected)