from collections import deque

food_quantity = int(input())
biggest_order = 0

orders = deque(map(int, input(). split()))
orders_left = []

while orders:
    order = orders.popleft()
    if order > biggest_order:
        biggest_order = order
    if food_quantity - order > 0:
        food_quantity -= order
    else:
        orders_left.append(order)

final_orders_left = [str(order) for order in orders_left]

if len(final_orders_left) == 0:
    print(biggest_order)
    print("Orders complete")
else:
    print(biggest_order)
    print(f"Orders left: {' '.join(final_orders_left)}")