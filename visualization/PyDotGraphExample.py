import pydot

graph = pydot.Dot(graph_type='graph')

edge1= pydot.Edge("India", "TamilNadu")
edge2 = pydot.Edge("India", "Karnataka")
graph.add_edge(edge1)
graph.add_edge(edge2)


edge11 = pydot.Edge("TamilNadu","Chennai")
edge21 = pydot.Edge("Karnataka","Bangalore")
graph.add_edge(edge11)
graph.add_edge(edge21)

edge12 = pydot.Edge("TamilNadu","Trichy")
edge22 = pydot.Edge("Karnataka","Mysore")
graph.add_edge(edge12)
graph.add_edge(edge22)

graph.write_png("/home/dharani/Desktop/samplegraph.png")