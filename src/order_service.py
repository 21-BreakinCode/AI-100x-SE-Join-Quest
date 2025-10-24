from src.order import Order


class OrderService:
    def __init__(self):
        self.promotions = []

    def add_promotion(self, promotion):
        self.promotions.append(promotion)

    def checkout(self, items):
        order = Order()
        for item in items:
            order.add_item(item)

        # Calculate original amount
        order.original_amount = order.calculate_subtotal()

        # Apply all promotions
        for promotion in self.promotions:
            promotion.apply(order)

        # Calculate final total
        order.total_amount = order.original_amount - order.discount

        return order
