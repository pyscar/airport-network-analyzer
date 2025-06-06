# streamlit_airport_analysis.py

import streamlit as st
import pandas as pd
import networkx as nx
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import time

# Load data
df_airlines = pd.read_csv("airlines.csv")
df_airplanes = pd.read_csv("airplanes.csv")
df_airports = pd.read_csv("airports.csv")
df_routes = pd.read_csv("routes.csv")

def get_graph():
    return nx.from_pandas_edgelist(df_routes, 'Source airport', 'Destination airport')

def show_airports_table():
    airports_data = df_airports[['Name', 'City', 'Country']].copy()
    airports_data.rename(columns={'Name': 'Airport Name', 'City': 'City Name', 'Country': 'Country Name'}, inplace=True)
    return airports_data.sort_values(by='Country Name').reset_index(drop=True)

def plot_routes_from_airport_to_airport(dep_iata, arr_iata):
    G = get_graph()

    if dep_iata not in G or arr_iata not in G:
        return None

    try:
        # Find shortest path between dep and arr airports
        path = nx.shortest_path(G, dep_iata, arr_iata)
    except nx.NetworkXNoPath:
        return None

    # Get airport info for all airports in path
    airports_in_path = df_airports[df_airports['IATA'].isin(path)].set_index('IATA')

    # Center map on first airport in path
    first_airport = airports_in_path.loc[path[0]]
    fmap = folium.Map(location=[first_airport['Latitude'], first_airport['Longitude']], zoom_start=4)

    # Mark airports in path with distinct colors
    for iata in path:
        airport = airports_in_path.loc[iata]
        if iata == dep_iata:
            color = 'green'
            popup_text = f"Departure Airport: {airport['Name']} ({iata})"
        elif iata == arr_iata:
            color = 'red'
            popup_text = f"Arrival Airport: {airport['Name']} ({iata})"
        else:
            color = 'blue'
            popup_text = f"Connecting Airport: {airport['Name']} ({iata})"

        folium.Marker(
            location=[airport['Latitude'], airport['Longitude']],
            popup=popup_text,
            icon=folium.Icon(color=color, icon='plane', prefix='fa')
        ).add_to(fmap)

    # Draw lines between airports in the path
    for i in range(len(path) - 1):
        src = airports_in_path.loc[path[i]]
        dst = airports_in_path.loc[path[i + 1]]
        folium.PolyLine(
            locations=[[src['Latitude'], src['Longitude']], [dst['Latitude'], dst['Longitude']]],
            color='blue',
            weight=3,
            opacity=0.7
        ).add_to(fmap)

    return fmap


def shortest_paths(source, destination):
    G = get_graph()
    if source not in G or destination not in G:
        return None, []
    try:
        sp = nx.shortest_path(G, source, destination)
        all_paths = list(nx.all_shortest_paths(G, source, destination))
        return sp, all_paths[:3]
    except nx.NetworkXNoPath:
        return None, []

def analyze_efficiency(source, destination):
    G = get_graph()
    results = {}
    start = time.time()
    nx.shortest_path(G, source, destination)
    results['dijkstra_time'] = time.time() - start

    start = time.time()
    nx.minimum_spanning_tree(G)
    results['mst_time'] = time.time() - start

    results['nodes'] = len(G.nodes())
    results['edges'] = len(G.edges())
    return results

def plot_folium_map(country):
    airports_data = df_airports[['Name', 'City', 'Country', 'Latitude', 'Longitude']]
    filtered = airports_data[airports_data['Country'] == country]
    if filtered.empty:
        return None
    fmap = folium.Map(location=[filtered.iloc[0]['Latitude'], filtered.iloc[0]['Longitude']], zoom_start=4)
    for _, row in filtered.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name'], tooltip=row['Name'], icon=folium.Icon(color='blue')).add_to(fmap)
    return fmap

# Streamlit UI
st.set_page_config(page_title="Airport Network Analyzer", layout="wide")
st.title("Airport Network Analyzer")

option = st.sidebar.selectbox("Select an option", (
    "Show Airports",
    "Map of Airports by Country",
    "Show Connections on World Map",
    "Shortest Path Between Airports",
    "Efficiency Analysis",
))

if option == "Show Airports":
    st.subheader("Airports Information")
    st.dataframe(show_airports_table())

elif option == "Map of Airports by Country":
    countries = df_airports['Country'].dropna().unique()
    countries.sort()
    country = st.selectbox("Select a Country", countries)

    st.subheader(f"Map of Airports in {country}")
    fmap = plot_folium_map(country)
    if fmap:
        folium_static(fmap)
    else:
        st.warning("No airports found in the specified country.")

elif option == "Show Connections on World Map":
    st.subheader("Flight Routes Visualization by Airport")
    airports_list = df_airports['IATA'].dropna().unique()
    airports_list.sort()

    dep_iata = st.selectbox("Select Departure Airport (IATA Code)", airports_list, index=list(airports_list).index("NBO") if "NBO" in airports_list else 0)
    arr_iata = st.selectbox("Select Arrival Airport (IATA Code)", airports_list, index=list(airports_list).index("BBI") if "BBI" in airports_list else 0)

    if st.button("Show Routes"):
        fmap = plot_routes_from_airport_to_airport(dep_iata, arr_iata)
        if fmap:
            folium_static(fmap)
        else:
            st.warning(f"No routes found from {dep_iata} to {arr_iata}.")

elif option == "Shortest Path Between Airports":
    source = st.text_input("Enter source IATA code", "DEL")
    destination = st.text_input("Enter destination IATA code", "BOM")
    shapefile_path = st.text_input("Enter shapefile path", "ne_110m_admin_0_countries.shp")
    if st.button("Find Shortest Path"):
        sp, top_paths = shortest_paths(source, destination)
        if not sp:
            st.error("No path found.")
        else:
            st.write("Shortest Path:", " → ".join(sp))
            for i, p in enumerate(top_paths[1:], 2):
                st.write(f"Route {i}:", p)

elif option == "Efficiency Analysis":
    source = st.text_input("Source Airport", "DEL")
    destination = st.text_input("Destination Airport", "BOM")
    if st.button("Analyze"):
        result = analyze_efficiency(source, destination)
        st.write("Execution Time for Dijkstra's Algorithm:", result['dijkstra_time'])
        st.write("Execution Time for MST:", result['mst_time'])
       


# Run with:
# streamlit run streamlit_airport_analysis.py

