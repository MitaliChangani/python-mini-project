import random
import time

def fireworks():
    while True:
        print("\033c")  # Clears the screen
        for _ in range(10):
            print(" " * random.randint(10, 50) + "*")
        time.sleep(0.2)

fireworks()