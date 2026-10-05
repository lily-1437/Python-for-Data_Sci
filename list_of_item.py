store = ["Pen", "pencil", "Notebook", "Bag", "rubber", "scale", "ruler", "watch", "geometry box", "Highlighter"]
search = input("Write down an item name: ").lower()

if search in [i.lower() for i in store]:
    print("Item found")
else:
    print("Item unavailable")
    store.append(search)
    print("Newly added:",store)