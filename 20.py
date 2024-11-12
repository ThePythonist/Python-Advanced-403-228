class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class Basket:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.total_price = sum([i.price for i in self.items])
        self.count = len(self.items)

    def add_to_basket(self, product):
        self.items.append(product)

        self.total_price = sum([i.price for i in self.items])
        self.count = len(self.items)

        print(f"Product {product.name} added to basket")
        print("-" * 50)

    def remove_from_basket(self, product):
        if product in self.items:
            self.items.remove(product)

            self.total_price = sum([i.price for i in self.items])
            self.count = len(self.items)

            print(f"Product {product.name} removed from basket")
            print("-" * 50)

    def show_factor(self):
        print(f"Your basket items : {[i.name for i in self.items]}")
        print(f"Final factor : {self.total_price}")
        print("-" * 50)


pr1 = Product("dkp-9798841", "شورت مردانه آوین", 69000)
pr2 = Product("dkp-9221811", "MacBook Air 2022", 61710000)
pr3 = Product("dkp-13714776", "Galaxy S24 Ultra", 62840000)

ali = Basket("14030817-1001")
hamed = Basket("14030817-1026")

ali.add_to_basket(pr1)
ali.add_to_basket(pr2)
ali.add_to_basket(pr3)

ali.show_factor()

ali.remove_from_basket(pr1)

ali.show_factor()
