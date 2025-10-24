from behave import given, when, then
from src.product import Product
from src.order_item import OrderItem
from src.order_service import OrderService
from src.threshold_discount_promotion import ThresholdDiscountPromotion
from src.buy_one_get_one_promotion import BuyOneGetOnePromotion
from src.double_eleven_promotion import DoubleElevenPromotion


@given('no promotions are applied')
def step_no_promotions(context):
    context.order_service = OrderService()


@given('the threshold discount promotion is configured')
def step_threshold_discount_promotion(context):
    if not hasattr(context, 'order_service'):
        context.order_service = OrderService()
    row = context.table[0]
    threshold = int(row['threshold'])
    discount = int(row['discount'])
    promotion = ThresholdDiscountPromotion(threshold, discount)
    context.order_service.add_promotion(promotion)


@given('the buy one get one promotion for cosmetics is active')
def step_buy_one_get_one_promotion(context):
    if not hasattr(context, 'order_service'):
        context.order_service = OrderService()
    promotion = BuyOneGetOnePromotion('cosmetics')
    context.order_service.add_promotion(promotion)


@given('the Double Eleven promotion is active')
def step_double_eleven_promotion(context):
    if not hasattr(context, 'order_service'):
        context.order_service = OrderService()
    promotion = DoubleElevenPromotion()
    context.order_service.add_promotion(promotion)


@when('a customer places an order with')
def step_customer_places_order(context):
    items = []
    for row in context.table:
        product_name = row['productName']
        unit_price = int(row['unitPrice'])
        quantity = int(row['quantity'])

        category = row.get('category', None)

        product = Product(product_name, unit_price, category)
        order_item = OrderItem(product, quantity)
        items.append(order_item)

    context.order = context.order_service.checkout(items)


@then('the order summary should be')
def step_order_summary(context):
    row = context.table[0]

    if 'totalAmount' in row.headings:
        expected_total = int(row['totalAmount'])
        assert context.order.total_amount == expected_total, \
            f"Expected total amount {expected_total}, but got {context.order.total_amount}"

    if 'originalAmount' in row.headings:
        expected_original = int(row['originalAmount'])
        assert context.order.original_amount == expected_original, \
            f"Expected original amount {expected_original}, but got {context.order.original_amount}"

    if 'discount' in row.headings:
        expected_discount = int(row['discount'])
        assert context.order.discount == expected_discount, \
            f"Expected discount {expected_discount}, but got {context.order.discount}"


@then('the customer should receive')
def step_customer_receives(context):
    expected_items = {}
    for row in context.table:
        product_name = row['productName']
        quantity = int(row['quantity'])
        expected_items[product_name] = quantity

    actual_items = {}
    for item in context.order.items:
        actual_items[item.product.name] = item.quantity

    assert actual_items == expected_items, \
        f"Expected items {expected_items}, but got {actual_items}"
