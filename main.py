import heapq
from data_stream import generate_sorted_stream

# Two heaps: one max-heap (lower half), one min-heap (upper half)
low, high = [], []

def add_number(num):
    """Add number to one of the heaps."""
    if not low or num < -low[0]:
        heapq.heappush(low, -num)
    else:
        heapq.heappush(high, num)

    # Balance heaps
    if len(low) > len(high) + 1:
        heapq.heappush(high, -heapq.heappop(low))
    elif len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))

def get_median():
    """Return current median."""
    if len(low) == len(high):
        return (-low[0] + high[0]) / 2
    return float(-low[0])

def main():
    stream1 = generate_sorted_stream(start=10)
    stream2 = generate_sorted_stream(start=20)

    while True:
        num1 = next(stream1)
        num2 = next(stream2)
        
        add_number(num1)
        add_number(num2)

        print(f"Stream1: {num1}, Stream2: {num2}, Median: {get_median()}")

if __name__ == "__main__":
    main()
