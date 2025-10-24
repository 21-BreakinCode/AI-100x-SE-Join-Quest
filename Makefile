test-order:
	python -m behave features/order.feature

test-order-with-skip:
	python -m behave features/order.feature --tags=order_pricing --tags=-skip --no-capture

test-order-with-skip:
	python -m behave features/chess.feature --tags=General --tags=-skip --no-capture

test-chess:
	python -m behave features/chess.feature --no-capture
