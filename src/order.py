class Order:
    def __init__(self):
        self.items = []
        self.original_amount = 0
        self.discount = 0
        self.total_amount = 0

    def add_item(self, item):
        self.items.append(item)

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.product.unit_price * item.quantity
        return subtotal
