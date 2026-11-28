sales = [
    {"product": "Pen", "quantity": 3, "price": 15},
    {"product": "Book", "quantity": 2, "price": 120},
    {"product": "Pen", "quantity": 5, "price": 15},
    {"product": "Bag", "quantity": 1, "price": 850},
    {"product": "Book", "quantity": -1, "price": 120},
    {"product": "Ruler", "quantity": 4, "price": 20}
]

revenue_by_product = {}
large_transactions = []
total_revenue = 0
invalid_count = 0

for record in sales:
    qty = record["quantity"]
    price = record["price"]

    # 1. skip invalid records
    if qty <= 0 or price < 0:
        invalid_count += 1
        continue

    # 2. revenue for this transaction
    revenue = qty * price

    # 3. accumulate by product
    product = record["product"]
    revenue_by_product[product] = revenue_by_product.get(product, 0) + revenue

    # 4. running total
    total_revenue += revenue

    # 6. record large transactions
    if revenue >= 200:
        large_transactions.append(record)

# 5. top product
top_product = None
top_revenue = -1
for product, rev in revenue_by_product.items():
    if rev > top_revenue:
        top_revenue = rev
        top_product = product

print("Revenue by product:", revenue_by_product)
print("Total revenue: Tk", total_revenue)
print(f"Top product: {top_product} (Tk {top_revenue})")
print("Transactions with revenue >= Tk 200:", large_transactions)
print("Invalid records:", invalid_count)