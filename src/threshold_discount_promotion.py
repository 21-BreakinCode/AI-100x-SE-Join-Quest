from src.promotion import Promotion


class ThresholdDiscountPromotion(Promotion):
    def __init__(self, threshold, discount):
        self.threshold = threshold
        self.discount = discount

    def apply(self, order):
        # Apply discount if threshold is met (based on original amount before promotions)
        if order.original_amount >= self.threshold:
            order.discount += self.discount
