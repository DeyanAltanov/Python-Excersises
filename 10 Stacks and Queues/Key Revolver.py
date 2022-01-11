from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence = int(input())
bullets_shot = 0
bullets_used = 0

while True:
    if len(locks) > 0 and len(bullets) > 0:
        first_lock = locks.popleft()
        last_bullet = bullets.pop()
    else:
        break
    if last_bullet <= first_lock:
        print("Bang!")
        bullets_shot += 1
        bullets_used += 1
        if bullets_shot == barrel_size and len(bullets) > 0:
            bullets_shot = 0
            print("Reloading!")
    else:
        print("Ping!")
        locks.appendleft(first_lock)
        bullets_shot += 1
        bullets_used += 1
        if bullets_shot == barrel_size and len(bullets) > 0:
            bullets_shot = 0
            print("Reloading!")

if len(bullets) == 0 and len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - (bullets_used * bullet_price)}")