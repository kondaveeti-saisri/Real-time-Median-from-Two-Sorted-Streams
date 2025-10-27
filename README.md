# 🧠 Real-time Median from Two Sorted Data Streams

## 📘 Project Overview
This project computes the **real-time median** value from **two continuously updating sorted data streams** — such as live prices from two different stock exchanges or readings from two sensors.  

Instead of merging both streams (which is slow and memory-heavy), the program efficiently updates the **running median** using two heaps (a max-heap and a min-heap).  

---

## 🎯 Objectives
- Calculate the **median** instantly as new data arrives.  
- Handle **continuous data streams** efficiently.  
- Use **minimal memory** (no full data merging).  
- Demonstrate **real-time data processing** logic in Python.  

---

## ⚙️ How It Works
1. Two simulated sorted data streams (`stream1` and `stream2`) continuously generate new values.  
2. Each new value is added to one of two heaps:
   - **Max-heap (low)** → stores the smaller half of numbers  
   - **Min-heap (high)** → stores the larger half  
3. The heaps stay balanced so that the median can be quickly computed:
   - If both heaps have equal size → median = average of two middle values  
   - Otherwise → median = top of the larger heap  
4. The program prints the **current stream values** and **real-time median** continuously.

---

## 🧩 Example Output

Stream1: 15, Stream2: 24, Median: 19.5
Stream1: 20, Stream2: 28, Median: 22.0
Stream1: 24, Stream2: 31, Median: 25.0


This shows the new values arriving from both streams and the updated median after each step.

---

## 🛠️ Technologies Used
- **Python 3**
- **heapq** → for efficient median computation  
- **time** → to simulate real-time delay  
- **random** → to generate fake sorted stream data  

---

## 🚀 How to Run
1. Open the folder in **VS Code**  
2. Run the main script:
   ```bash
   python main.py
