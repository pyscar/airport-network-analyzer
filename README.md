---

# ✈️ Airport Network Analyzer

An interactive **network analysis and visualization application** for exploring global airport connectivity, flight routes, and network efficiency using graph theory and geospatial mapping.

Built with **Python, NetworkX, Folium, and Streamlit**, this project demonstrates how complex transportation networks can be analyzed, visualized, and queried through a user-friendly web interface.

---
## Live Demo (Streamlit link)-> https://airport-network-analyzer-f3qxcwd9gnjmfvvgsuyxln.streamlit.app/
## 🚀 Features

### 1. Airport Directory

* View a clean, sortable table of global airports
* Includes airport name, city, and country information

### 2. Airport Map by Country

* Visualize all airports within a selected country
* Interactive map with clickable markers

### 3. Global Route Visualization

* Display flight routes between a selected departure and arrival airport
* Supports:

  * Direct routes
  * Multi-hop (connecting) routes
* Color-coded markers for:

  * Departure airport
  * Arrival airport
  * Connecting airports

### 4. Shortest Path Analysis

* Uses graph algorithms to compute:

  * Shortest route between two airports
  * Multiple shortest path alternatives
* Displays routes using IATA airport codes

### 5. Network Efficiency Analysis

* Evaluates computational performance of:

  * Shortest path (Dijkstra)
  * Minimum Spanning Tree (MST)
* Reports:

  * Execution times
  * Total number of nodes and edges in the network

---

## 🧠 Technical Overview

### Architecture

* Airports and routes are modeled as a **graph network**
* Nodes represent airports (IATA codes)
* Edges represent flight routes
* Network analysis performed using **NetworkX**
* Geospatial visualization handled with **Folium**
* Interactive UI built with **Streamlit**

### Data Sources

The application uses CSV datasets for:

* Airlines
* Airplanes
* Airports
* Routes

(Compatible with standard OpenFlights-style datasets)

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

### 1. Install dependencies

```bash
pip install streamlit pandas networkx folium streamlit-folium
```

### 2. Run the Streamlit app

```bash
streamlit run streamlit_airport_analysis.py
```

### 3. Open in browser

Streamlit will automatically open the application in your default browser.

---

## 📊 Use Cases

* Transportation network analysis
* Aviation route optimization studies
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

* Add weighted routes (distance, cost, time)
* Integrate real-time flight data APIs
* Persist graph data in a database
* Deploy on cloud infrastructure
* Add dashboard-level analytics

---

## 👤 Author

Built by a **Data Engineer / Computer Science (AI & ML) graduate** with a focus on real-world data systems, network analysis, and interactive data applications.

---



