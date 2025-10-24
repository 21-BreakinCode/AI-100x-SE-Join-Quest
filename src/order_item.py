class OrderItem:
    def __init__(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.product = product
        self.quantity = quantity