delivery_1 = {"pen": 12, "book": 5, "bag": 2}
delivery_2 = {"book": 4, "ruler": 10, "pen": 3}

combined = {}
for delivery in [delivery_1, delivery_2]:
    for item, qty in delivery.items():
        combined[item] = combined.get(item, 0) + qty

grand_total = 0
for qty in combined.values():
    grand_total += qty

print("Combined delivery:", combined)
print("Grand total:", grand_total)