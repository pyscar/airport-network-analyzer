# airport-network-analyzer
Great! Here's a full **README.md** template for your GitHub project that includes:

* Project description
* Features
* How to install dependencies
* How to run locally
* How to deploy on Streamlit Sharing
* How to use

---

````markdown
# Airport Network Analyzer

A Streamlit web app that analyzes and visualizes airport networks and flight routes worldwide. It uses graph algorithms to find shortest paths between airports and displays interactive maps for better insights.

## Features

- Display detailed airport information in tables.
- View airport locations by country on an interactive map.
- Visualize flight routes between airports on a world map.
- Find shortest and alternative flight paths between two airports.
- Show the flight path on an interactive Folium map.
- Analyze efficiency of graph algorithms like Dijkstra and MST.

## Technologies Used

- Python 3.x
- Streamlit
- NetworkX
- Folium
- Pandas

## Installation

1. Clone the repository:

```bash
git clone https://github.com/pyscar/airport-network-analyzer.git
cd airport-network-analyzer
````

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Locally

Make sure your CSV data files (`airlines.csv`, `airplanes.csv`, `airports.csv`, `routes.csv`) are in the project directory. Then run:

```bash
streamlit run streamlit_airport_analysis.py
```

Your app will be available at `http://localhost:8501`.

## Deployment on Streamlit Cloud

1. Push your project to a GitHub repository.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in.
3. Click **New app** and connect your GitHub repo.
4. Select the branch and main file (`streamlit_airport_analysis.py`).
5. Click **Deploy** and wait for your app to build.
6. Share the generated link with others!

## Usage

* Use the sidebar to navigate between:

  * Airport tables
  * Maps of airports by country
  * Visualize connections between airports
  * Find shortest paths and see routes on a map
  * Run efficiency analysis of algorithms

## Data

* The app requires four CSV files:

  * `airlines.csv`
  * `airplanes.csv`
  * `airports.csv`
  * `routes.csv`

Make sure these are correctly formatted and placed in the project root.


