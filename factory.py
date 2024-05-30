class Product:
    def use_product(self):
        pass


class ConcreteProductA(Product):
    def use_product(self):
        return "Using Product A"


class ConcreteProductB(Product):
    def use_product(self):
        return "Using Product B"


class Creator:
    def factory_method(self, product_type):
        if product_type == "A":
            return ConcreteProductA()
        elif product_type == "B":
            return ConcreteProductB()
        else:
            raise ValueError("Unknown Product Type")


if __name__ == "__main__":
    creator = Creator()
    product = creator.factory_method("A")
    print(product.use_product())  # Output: Using Product A
