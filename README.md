# Real-time-Median-from-Two-Sorted-Streams


Compute the running median across two continuously updating sorted streams (e.g., two stock exchanges) **without merging** the full streams.



## Overview

This project efficiently computes the **real-time median** from two or more continuously updating sorted data streams — such as price feeds from multiple stock exchanges — while using **minimal memory** and ensuring **scalability**.



##  Objectives

-  **Efficient real-time median computation**  
-  **Minimal memory usage** using heaps  
-  **Scalable** to multiple data streams  



##  Concept

The core logic maintains two balanced heaps:

- **`max_heap`** – stores the **lower half** of elements (using negative values for max-heap behavior)  
- **`min_heap`** – stores the **upper half** of elements  

Each new value is inserted into the correct heap and rebalanced when necessary.  

- **Median retrieval:** `O(1)`  
- **Insertion + rebalance:** `O(log n)`



##  Features

-  Real-time simulated streams using `asyncio` or `threading`  
-  Efficient heap-based median updates  
-  Command-line demo support  
-  Optional FastAPI + Streamlit visualization  
-  Unit testing with `pytest`

---

## 🧩 Repository Layout

