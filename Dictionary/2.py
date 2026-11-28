prices = {"pen": 15, "book": 120, "bag": 850}
requested_items = ["book", "ruler", "pen"]

for item in requested_items:
    price = prices.get(item)       # returns None if missing
    if price is not None:
        print(f"{item}: Tk {price}")
    else:
        print(f"{item}: not found")