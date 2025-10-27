import random
import time

def generate_sorted_stream(start=1, step=5):
    """Simulates a sorted data stream."""
    value = start
    while True:
        value += random.randint(1, step)
        yield value
        time.sleep(1)  # simulate real-time data (1 sec delay)
