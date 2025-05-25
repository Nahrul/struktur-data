import networkx as nx
import streamlit as st
import matplotlib.pyplot as plt

class MyGraph:
    def __init__(self):
        if "edges" not in st.session_state:
            st.session_state.edges = [("Jakarta", "Bandung", 153),("Jakarta", "Cirebon", 220),("Bandung", "Cirebon", 141)]
        self.add_route()
        self.draw_graph(self.create_graph())
        self.find_shortest_path()
    
    def create_graph(self):
        G = nx.Graph()
        G.add_weighted_edges_from(st.session_state.edges)
        return G

    def draw_graph(self, G, path=[]):
        pos = nx.spring_layout(G, seed=42)
        edge_labels = nx.get_edge_attributes(G, "weight")
        st.write("Visualisasi Graph Rute Kota")
        plt.figure(figsize=(8,6))
        nx.draw(G, pos, with_labels=True, node_color="red", node_size=2000)
        nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels,font_size=10)
        if path:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="blue", width=2)
        st.pyplot(plt)
    def add_route(self):
        with st.form(key='add_route_form'):
            kota1 = st.text_input("Kota Asal")
            kota2 = st.text_input("Kota Tujuan")
            weight = st.number_input("Jarak (km)", min_value=0)
            submit_button = st.form_submit_button(label="Tambah Rute")
            if submit_button:
                st.session_state.edges.append((kota1, kota2, weight))
                st.success(f"Rute dari {kota1} Ke {kota2} dengan jarak {weight} km talah ditambahkan.")
    def find_shortest_path(self):
        st.write("Cari Rute Terpendek")
        st.write("Pilih dua kota untuk mencari rute terpendek.")    
        G = self.create_graph()
        kota_list = sorted(G.nodes())
        with st.form(key='shortest_path_form'):
            start = st.selectbox("Kota Awal", kota_list)
            end = st.selectbox("Kota Tujuan", kota_list)
            submit_button = st.form_submit_button(label="Cari Rute Terpendek")
            if submit_button:
                try:
                    path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
                    total_distance = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')
                    st.success(f"Rute terpendek dari {start} ke {end} adalah: {' -> '.join(path)} dengan Jarak total: {total_distance} km")
                    self.draw_graph(G, path)
                except nx.NetworkXNoPath:
                    st.error(f"Tidak ada rute dari {start} ke {end}.")

if __name__ == "__main__":
    app = MyGraph()