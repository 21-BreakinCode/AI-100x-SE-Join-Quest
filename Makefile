test:
	python -m behave features/order.feature

test-with-skip:
	python -m behave features/order.feature --tags=order_pricing --tags=-skip --no-capture
