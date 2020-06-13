from lana_client import LanaClient

client = LanaClient()

basket_ids = []
# Creating fro baskets for four cases
for i in range(4):
    basket_ids.append(client.create_basket())

# Case 1
# Items: PEN, TSHIRT, MUG
# Total: 32.50€
client.add_element_to_basket(basket_ids[0], 'PEN', 1)
client.add_element_to_basket(basket_ids[0], 'TSHIRT', 1)
client.add_element_to_basket(basket_ids[0], 'MUG', 1)

# Case 2
# Items: PEN, TSHIRT, PEN
# Total: 25.00€
client.add_element_to_basket(basket_ids[1], 'PEN', 2)
client.add_element_to_basket(basket_ids[1], 'TSHIRT', 1)

# Case 3
# Items: TSHIRT, TSHIRT, TSHIRT, PEN, TSHIRT
# Total: 65.00€
client.add_element_to_basket(basket_ids[2], 'PEN', 1)
client.add_element_to_basket(basket_ids[2], 'TSHIRT', 4)

# Case 4
# Items: PEN, TSHIRT, PEN, PEN, MUG, TSHIRT, TSHIRT
# Total: 62.50€
client.add_element_to_basket(basket_ids[3], 'PEN', 3)
client.add_element_to_basket(basket_ids[3], 'TSHIRT', 3)
client.add_element_to_basket(basket_ids[3], 'MUG', 1)

# Show results
for i in basket_ids:
    client.get_total_amount_basket(i)

# Deleting baskets
for i in basket_ids:
    client.delete_basket(i)
