def calculate_total_price(cart_items):
    total_price = sum(cart_items.values())
    if len(cart_items) > 5:
        total_price *= 0.9
    return total_price

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
total_price = calculate_total_price(cart_items)

if total_price == 0 and len(cart_items) == 0:
    print("Your cart is empty.")
else:
    print(f"Total Price: {total_price}")

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500, 'Monitor': 8000, 'Speaker': 1000}
total_price = calculate_total_price(cart_items)