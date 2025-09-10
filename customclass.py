class Shopping:
    def __init__(self,items=[]):
        self.items=items

    def add_cart(self,item):
        self.items.append(item)
        print(f"{item} added to cart")

    def __len__(self):
        print("Cart Size : ")
        return len(self.items)

    def __str__(self):
        return f"Items in cart {self.items}"

cart =  Shopping()
print(cart)
print(len(cart))

cart.add_cart("Mobile")
cart.add_cart("Laptop")
cart.add_cart("MacBook")

print(cart)
print(len(cart))
