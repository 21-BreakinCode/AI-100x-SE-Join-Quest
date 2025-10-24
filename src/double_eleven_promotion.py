from src.promotion import Promotion


class DoubleElevenPromotion(Promotion):
    """
    Double Eleven promotion: For every 10 items of the same product,
    those 10 items get 20% discount.

    Example: 12 items at 100 each = (10*100*0.8) + (2*100) = 800 + 200 = 1000
    """

    def apply(self, order):
        # Calculate discount per product based on bulk quantity
        for item in order.items:
            quantity = item.quantity
            unit_price = item.product.unit_price

            # Calculate how many complete sets of 10 items
            bulk_sets = quantity // 10
            remaining_items = quantity % 10

            # Calculate discounted amount for bulk sets (20% off)
            bulk_discount_amount = bulk_sets * 10 * unit_price * 0.2

            # Add to total discount
            order.discount += bulk_discount_amount