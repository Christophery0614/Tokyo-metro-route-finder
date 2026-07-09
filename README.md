# TOKYO METRO ROUTE FINDER USING DIJKSTRA ALGORITHM — Final Year Project

[![Project Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Python](https://img.shields.io/badge/Python-3.11+-blue)]()

A Python and Flask-based Tokyo Metro Route Finder that uses Dijkstra’s Algorithm to find the shortest travel-time paths between stations.
Designed as an academic project emphasizing clean algorithm implementation, modular architecture, and practical route-planning logic.

A web-based navigation system designed to calculate and visualize the shortest path between stations in the Tokyo subway network. This application is powered by a Python back-end using Flask and implements Dijkstra's Algorithm for efficient pathfinding.

---

## 🌐 Introduction / 概要 / 简介

### 🇬🇧 English
**TOKYO METRO ROUTE FINDER** is an intelligent web-based transit navigation system engineered to solve shortest-path queries within the massive Tokyo underground network. Leveraging **Dijkstra’s Algorithm** on a modeled graph database, the system computes the most efficient routes based on real-world travel metrics. Built with a robust **Flask** back-end and a sleek user interface, it offers seamless route visualization, line browsing, and interactive station mappings.

### 🇯🇵 日本語
**TOKYO METRO ROUTE FINDER** は、広大な東京の地下鉄ネットワークにおける最適な移動経路を計算・可視化するために開発された、インテリジェントなウェブベースのナビゲーションシステムです。バックエンドには **Flask** を採用し、グラフ理論に基づく **ダイクストラ法（Dijkstra's Algorithm）** を実装することで、駅間の実移動時間や距離に応じた最短ルートを瞬時に算出します。直感的なUIによるルート案内、路線情報の閲覧、およびインタラクティブな路線図確認機能を備えています。

### 🇨🇳 简体中文
**TOKYO METRO ROUTE FINDER** 是一款专为庞大的东京地铁网络设计的智能 Web 交通导航系统。该项目作为毕业设计（Final Year Project），核心算法基于图论中的**迪杰斯特拉算法（Dijkstra's Algorithm）**，通过对真实世界地铁线路数据的建模，能够高效计算出任意两站之间的最短路径或最优时间。系统采用 **Flask** 框架搭建后端，配合精美的现代化前端界面，实现了路线规划、地铁线路浏览以及交互式地图辅助查看等功能。

---

## 🚀 Features

- **Shortest Path Calculation:** Computes the most efficient route between any two Tokyo subway stations using Dijkstra's algorithm based on distance or travel time.
- **Subway Line Viewer:** Browse through various Tokyo subway lines and their constituent stations.
- **Interactive Web Interface:** User-friendly frontend designed with HTML/CSS templates for seamless routing queries.
- **Static Map Integration:** Includes a Tokyo subway map visual aid for reference.
- **Cross-Platform Launch Scripts:** Includes automation scripts (`.bat` and `.sh`) for easy deployment on Windows, macOS, or Linux.

---

## 🌍 Live Demo

Try the live version here:  
👉 [Tokyo Metro Route Finder](https://tokyometroroutefinder.christophery0614.workers.dev/)

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
* **Academic Year:** 2026
* **Supervisor:** Ts. Dr. Mohd Nor Akmal Bin Khalid

