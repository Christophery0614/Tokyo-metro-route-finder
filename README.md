A Python and Flask-based Tokyo Metro Route Finder that uses Dijkstra’s Algorithm to find the shortest travel-time paths between stations.
Designed as an academic project emphasizing clean algorithm implementation, modular architecture, and practical route-planning logic.

# TOKYO METRO ROUTE FINDER USING DIJKSTRA ALGORITHM — Final Year Project

A web-based navigation system designed to calculate and visualize the shortest path between stations in the Tokyo subway network. This application is powered by a Python back-end using Flask and implements Dijkstra's Algorithm for efficient pathfinding.

---

## 🚀 Features

- **Shortest Path Calculation:** Computes the most efficient route between any two Tokyo subway stations using Dijkstra's algorithm based on distance or travel time.
- **Subway Line Viewer:** Browse through various Tokyo subway lines and their constituent stations.
- **Interactive Web Interface:** User-friendly frontend designed with HTML/CSS templates for seamless routing queries.
- **Static Map Integration:** Includes a Tokyo subway map visual aid for reference.
- **Cross-Platform Launch Scripts:** Includes automation scripts (`.bat` and `.sh`) for easy deployment on Windows, macOS, or Linux.

---

## 📂 Project Structure

```text
Final Year Project Program/
│
├── app.py                         # Main Flask application (routes, controller)
├── dijkstra_algorithm.py           # Core pathfinding algorithm logic
├── tokyo_subway_data.py           # Subway network dataset (stations, lines, connections)
├── requirements.txt               # Python dependencies
├── run.bat                        # Windows startup batch script
├── start.sh                       # Linux/macOS startup shell script
│
├── static/
│   └── tokyo_subway_map.jpg       # Visual reference map of the subway system
│
└── templates/                     # HTML UI views
    ├── index.html                 # Main landing & route selection page
    ├── route.html                 # Route results page showing the calculated path
    ├── lines.html                 # Page listing available subway lines
    ├── about.html                 # Project description and metadata
    └── error.html                 # Error fallback view (e.g., station not found)

```

---

## 🛠️ Prerequisites & Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd "Final Year Project Program"

```

### 2. Environment Setup

It is highly recommended to use a Python virtual environment (Python 3.11+ is recommended).

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate

```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt

```

---

## 💻 How to Run

You can launch the web server using either the included scripts or directly via Python.

### Option A: Using Startup Scripts

* **Windows:** Double-click `run.bat` or execute `run.bat` in your terminal.
* **Linux/macOS:** Run `chmod +x start.sh && ./start.sh` in your terminal.

### Option B: Using Python Directly

```bash
python app.py

```

Once started, open your web browser and navigate to:
👉 **`http://127.0.0.1:5000`**

---

## 🧮 Core Logic: Dijkstra's Algorithm

The application treats the Tokyo subway system as a weighted, undirected graph $G = (V, E)$:

* **Vertices ($V$):** Subway stations.
* **Edges ($E$):** Tracks connecting adjacent stations.
* **Weights ($W$):** Real-world travel times or distances between stations.

When a user selects a starting station and a destination, `dijkstra_algorithm.py` processes the network matrix or adjacency list provided by `tokyo_subway_data.py` to yield the precise station sequence and the total cost (time/distance).

---

## 📝 Author

* **Name:** Yu Yifan
* **Project Type:** Final Year Project (FYP)

```

```
