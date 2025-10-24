from src.promotion import Promotion


class BuyOneGetOnePromotion(Promotion):
    def __init__(self, category):
        self.category = category

    def apply(self, order):
        # For each item in the specified category, add one more free item
        for item in order.items:
            if item.product.category == self.category:
                item.quantity += 1
