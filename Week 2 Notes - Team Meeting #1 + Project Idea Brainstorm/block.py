import pydot

graph = pydot.Dot(graph_type="digraph")

components = {
    "ESP32 (Main Controller)": ["Wi-Fi/Bluetooth", "Mobile App", "Web Dashboard", "Soil Moisture Sensor", "Temp/Humidity Sensor", "Light Sensor (Optional)", "Power Supply"],
    "Soil Moisture Sensor": ["ESP32 (Main Controller)"],
    "Temp/Humidity Sensor": ["ESP32 (Main Controller)"],
    "Light Sensor (Optional)": ["ESP32 (Main Controller)"],
    "Power Supply": ["ESP32 (Main Controller)"],
    "Wi-Fi/Bluetooth": ["Mobile App", "Web Dashboard"],
}

nodes = {}
for component in components.keys():
    nodes[component] = pydot.Node(component, shape="box", style="filled", fillcolor="lightblue")
    graph.add_node(nodes[component])


for parent, children in components.items():
    for child in children:
        if child not in nodes:
            nodes[child] = pydot.Node(child, shape="box", style="filled", fillcolor="lightgray")
            graph.add_node(nodes[child])
        graph.add_edge(pydot.Edge(nodes[parent], nodes[child])) #edges

graph.write_png("plantsense_block_diagram.png") #filesave