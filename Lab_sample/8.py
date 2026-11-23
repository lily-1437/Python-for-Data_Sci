import numpy as np

sales = np.array([
    [120, 150, 135, 170],
    [ 80,  95, 110, 105],
    [200, 180, 220, 240]
])

product_totals = sales.sum(axis=1)
print("Total sales of each product:", product_totals)

month_totals = sales.sum(axis=0)
print("Total sales of each month:", month_totals)

best_product = np.argmax(product_totals) + 1
print("Product with highest total sales: Product", best_product)

worst_month = np.argmin(month_totals) + 1
print("Month with lowest total sales: Month", worst_month)

modified = sales.copy()
modified[modified < 100] = 0

print("\nOriginal array:")
print(sales)
print("\nModified array:")
print(modified)