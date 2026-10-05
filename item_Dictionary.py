#in a dictionary check whether an item exist if found print the item if not add the item with a custom price
product = {"pen": 10, "Pencil": 10, "Scale": 10, "Notebook":50, "Bag":100, "rubber":5, "watch":300, "geometry box":200, "Highlighter":50}
search = input("Write down an item: ")
for item,price in product.items():
    if(item.lower() == search.lower()):
        print(f"{item}: {price} found")
        break
else:
    given_price = int(input("Enter a price for the item: "))
    product[search] = given_price
    print(f"{search}: {given_price} item has been added")
