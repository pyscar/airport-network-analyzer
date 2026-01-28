# ✈️ Airport Network Analyzer

An **interactive network analysis and visualization application** for exploring global airport connectivity, flight routes, and network efficiency using graph theory and geospatial mapping.

Built with **Python, NetworkX, Folium, and Streamlit**, this project demonstrates how complex transportation networks can be analyzed, visualized, and queried through a user-friendly web interface.

---

## 🔗 Live Demo

[Streamlit App](https://airport-network-analyzer-f3qxcwd9gnjmfvvgsuyxln.streamlit.app/)

---

## 🚀 Features

### 1. Airport Directory

* View a clean, sortable table of global airports
* Includes airport name, city, and country information

### 2. Airport Map by Country

* Visualize all airports within a selected country
* Interactive map with clickable markers

### 3. Global Route Visualization

* Display flight routes between selected departure and arrival airports
* Supports both direct and connecting routes
* Color-coded markers for departure, arrival, and connecting airports

### 4. Shortest Path Analysis

* Compute shortest routes using graph algorithms (Dijkstra)
* Multiple shortest path alternatives
* Display routes using IATA airport codes

### 5. Network Efficiency Analysis

* Evaluate computational performance of shortest path and minimum spanning tree (MST) calculations
* Reports execution times, total nodes, and edges in the network

---

## 🖼️ Screenshots
* Airport Directory view
  <img width="1915" height="905" alt="image" src="https://github.com/user-attachments/assets/ea6ef4a4-e4f8-4bdd-9dd1-70fd07a5cae2" />

* Country-wise airport map
  <img width="1912" height="939" alt="image" src="https://github.com/user-attachments/assets/0f7a4159-cd8f-4ed7-9b14-64493b77902a" />
  <img width="1919" height="960" alt="image" src="https://github.com/user-attachments/assets/73ba86a0-e669-4f61-81e6-f4d3dc127e76" />
  
* Shortest path analysis
  <img width="1897" height="892" alt="image" src="https://github.com/user-attachments/assets/97191aca-5118-44df-b21c-6848c75eb0cc" />

* flight path
  <img width="1906" height="961" alt="image" src="https://github.com/user-attachments/assets/291b64c3-03d4-4b0f-bb68-86869bb237c9" />

* Network efficiency metrics
<img width="1904" height="678" alt="image" src="https://github.com/user-attachments/assets/13538897-d949-4780-a2b9-e5310cdb6875" />

* Airports connections across the world
 <img width="1238" height="643" alt="image" src="https://github.com/user-attachments/assets/8f299b58-01a7-49e7-b1da-0a454e995a43" />
* shortest path finder (graph algorithms)
 <img width="1303" height="678" alt="image" src="https://github.com/user-attachments/assets/f7c78230-86c5-4bbd-bcd1-18b3b14517dc" />
---

## 🧠 Technical Overview

### Architecture

* Airports and routes modeled as a **graph network**
* Nodes represent airports (IATA codes)
* Edges represent flight routes
* Network analysis performed using **NetworkX**
* Geospatial visualization handled with **Folium**
* Interactive UI built with **Streamlit**

### Data Sources

* CSV datasets for airlines, airplanes, airports, and routes
* Compatible with standard **OpenFlights-style datasets**

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – data manipulation
* **NetworkX** – graph construction and analysis
* **Folium** – geospatial mapping
* **Streamlit** – web application framework
* **streamlit-folium** – Folium integration with Streamlit

---

## 📦 Project Structure

```
.
├── streamlit_airport_analysis.py
├── airlines.csv
├── airplanes.csv
├── airports.csv
├── routes.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Application

1. Install dependencies:

```bash
pip install streamlit pandas networkx folium streamlit-folium
```

2. Run the Streamlit app:

```bash
streamlit run streamlit_airport_analysis.py
```

3. Open in your browser — Streamlit will launch automatically.

---

## 📊 Use Cases

* Transportation network analysis
* Aviation route optimization
* Graph theory demonstrations
* Data visualization portfolios
* Educational and research applications

---

## 🔍 Key Highlights

* Demonstrates **graph-based problem solving**
* Combines **data engineering, analytics, and visualization**
* Handles real-world network complexity
* Designed for extensibility and experimentation

---

## 📌 Future Improvements

* Add weighted routes (distance, cost, or time)
* Integrate real-time flight data APIs
* Persist graph data in a database
* Deploy on cloud infrastructure
* Add dashboard-level analytics and interactive charts

---

## 👤 Author

Built by a  Computer Science (AI & ML) graduate**, specializing in real-world data systems, network analysis, and interactive data applications.
