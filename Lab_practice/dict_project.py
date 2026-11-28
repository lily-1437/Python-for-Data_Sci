prices = {
    "rice": 75,
    "oil": 185,
    "sugar": 120,
    "milk": 95,
    "egg": 12,
    "flour": 65,
    "salt": 40,
    "lentil": 130,
    "potato": 45,
    "onion": 80,
    "tea": 250,
    "coffee": 450,
    "biscuit": 50,
    "soap": 70,
    "shampoo": 180
}

# 1. Display available products
print("========== AVAILABLE PRODUCTS ==========")
print(f"{'Product':<15}{'Unit Price (Tk)':>20}")
print("-" * 37)
for product, price in prices.items():
    print(f"{product:<15}{price:>20.2f}")
print()

# 2. Empty order dictionary
order = {}

# 3. Number of order entries (re-ask until valid)
while True:
    entry_text = input("How many order entries? ")
    if entry_text.isdigit() and int(entry_text) > 0:
        num_entries = int(entry_text)
        break
    print("Please enter a positive whole number.")

# 4-9. Take each entry and build the combined order
for i in range(1, num_entries + 1):
    item = input(f"Enter product {i}: ").strip().lower()
    qty_text = input("Enter quantity: ").strip()

    # 5-6. Product must exist
    if item not in prices:
        print(f"{item} is not available.")
        continue

    # 7. Quantity must be a positive integer
    if not qty_text.isdigit() or int(qty_text) <= 0:
        print("Invalid quantity. Quantity must be a positive whole number.")
        continue

    quantity = int(qty_text)

    # 8-9. Combine repeated products
    order[item] = order.get(item, 0) + quantity

# 10. Display final combined order
print("\nFinal order:")
print(order)

# 11-12. Build the bill dictionary
bill = {}
for item, quantity in order.items():
    unit_price = prices[item]
    bill[item] = {
        "quantity": quantity,
        "unit_price": unit_price,
        "total": quantity * unit_price
    }

# 13. Subtotal
subtotal = 0
for details in bill.values():
    subtotal += details["total"]

# 14. Discount: 5% if subtotal >= 1000
if subtotal >= 1000:
    discount = 0.05 * subtotal
else:
    discount = 0

# 15. VAT on the discounted amount
vat = 0.02 * (subtotal - discount)

# 16. Final payable amount
final_amount = subtotal - discount + vat

# 17-18. Itemised bill with two decimal places
print()
print("================ GROCERY SHOP BILL ================")
print(f"{'Item':<12}{'Quantity':>10}{'Unit Price':>15}{'Total':>12}")
print("-" * 52)
for item, details in bill.items():
    print(f"{item:<12}{details['quantity']:>10}"
          f"{details['unit_price']:>15.2f}{details['total']:>12.2f}")
print("-" * 52)
print(f"Subtotal: Tk {subtotal:.2f}")
print(f"Discount (5%): Tk {discount:.2f}")
print(f"VAT (2%): Tk {vat:.2f}")
print("-" * 52)
print(f"Final amount: Tk {final_amount:.2f}")
print("====================================================")