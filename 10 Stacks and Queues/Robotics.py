from collections import deque
from datetime import datetime, timedelta

all_robots = input().split(';')
robots = []
available_robots = []
picked = []

time = datetime.strptime(input(), '%H:%M:%S')
current_time = time

products = deque()
product = input()

while product != 'End':
    products.append(product)
    product = input()

for bot in all_robots:
    robot_info = bot.split('-')
    current_time += timedelta(seconds=1)
    robot = {'robot_name': robot_info[0], 'processing_time': int(robot_info[1]), 'availability': current_time}
    robots.append(robot)
    available_robots.append(robot)

time += timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()
    if available_robots:
        robot = {'robot_name': available_robots[0]['robot_name'], 'product': current_product, 'availability': available_robots[0]['availability']}
        picked.append(robot)
        for robot in robots:
            if robot['robot_name'] == available_robots[0]['robot_name']:
                robot['availability'] += timedelta(seconds=robot['processing_time'])
                break
        available_robots.remove(available_robots[0])
    else:
        products.append(current_product)
    time += timedelta(seconds=1)
    for robot in robots:
        if time >= robot['availability'] and robot not in available_robots:
            available_robots.append(robot)

for robot in picked:
    print(f"{robot['robot_name']} - {robot['product']} [{robot['availability'].strftime('%H:%M:%S')}]")