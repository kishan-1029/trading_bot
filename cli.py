import argparse
from bot.orders import place_order
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        print("\n📊 Order Summary")
        print(vars(args))

        order = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            logger=logger,
            use_mock=False  
        )

        print("\n🔍 Full API Response:")
        print(order)

        print("\n✅ Order Executed Successfully")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n❌ Order Failed")
        print(str(e))


if __name__ == "__main__":
    main()