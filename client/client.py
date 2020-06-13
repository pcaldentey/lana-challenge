import argparse
from lana_client import LanaClient

client = LanaClient()

# Arguments definition
parser = argparse.ArgumentParser()
parser.add_argument("action", help="action to call to Lanaserver",
                    choices=['create_basket', 'delete_basket', 'add_product', 'get_total'])
parser.add_argument("-bid", "--basket_id", type=int,
                    help="basket identifier")
parser.add_argument("-pid", "--product_id", type=str,
                    help="product identifier", choices=['PEN', 'TSHIRT', 'MUG'])
parser.add_argument("-a", "--amount", type=int, default=1,
                    help="number of items of product to be added to basket")
args = parser.parse_args()


# Actions
if args.action == "create_basket":
    client.create_basket()

elif args.action == "delete_basket":
    if not args.basket_id:
        print("Need to populate basket_id argument for this action")
    else:
        client.delete_basket(args.basket_id)

elif args.action == "add_product":
    if not args.basket_id:
        print("Need to populate basket_id argument for this action")
    elif not args.product_id:
        print("Need to populate product_id argument for this action")
    else:
        client.add_element_to_basket(args.basket_id, args.product_id, args.amount)

elif args.action == "get_total":
    if not args.basket_id:
        print("Need to populate basket_id argument for this action")
    else:
        client.get_total_amount_basket(args.basket_id)
