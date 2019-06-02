import pydot as pydot

graph = pydot.Dot(graph_type='graph')

def draw(parent_name, child_name):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

def visit(node, parent=None):
    for k,v in node.items():
        if isinstance(v, dict):
            if parent:
                draw(parent, k)
            visit(v, k)
        else:
            draw(parent, k)
            draw(k, k+'_'+v)

def draw_the_graph(input_tree,out_path):
    visit(input_tree)
    graph.write_png(out_path)
