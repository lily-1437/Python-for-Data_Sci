stock = {"pen": 12, "book": 3, "bag": 2, "ruler": 9, "calculator": 1}

total = 0
low_stock = {}

for item, qty in stock.items():
    total += qty
    if qty < 5:
        low_stock[item] = qty

print("Total units:", total)
print("Low stock:", low_stock)