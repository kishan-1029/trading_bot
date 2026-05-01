from bot.client import get_client
from bot.validators import validate_order

def place_order(symbol, side, order_type, quantity, price=None, logger=None, use_mock=True):

    validate_order(symbol, side, order_type, quantity, price)

    try:
        # 🔹 MOCK MODE (default)
        if use_mock:
            order = {
                "orderId": 123456,
                "status": "FILLED",
                "executedQty": quantity,
                "avgPrice": price if price else "market_price"
            }

            if logger:
                logger.info(f"[MOCK] Order placed: {order}")

            return order

        # 🔹 REAL API MODE
        client = get_client()

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        if logger:
            logger.info(f"[REAL] Order placed: {order}")

        return order

    except Exception as e:
        if logger:
            logger.error(f"Error placing order: {str(e)}")
        raise