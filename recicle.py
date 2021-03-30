from networkx.drawing.nx_agraph import write_dot
import pydot

# graph = nx.drawing.nx_pydot.to_pydot(ego)
# pos = nx.nx_pydot.pydot_layout(ego, prog="circo")
# graph.write(pos)
graph = pydot.Dot('my_graph', graph_type='digraph', bgcolor='white')
graph.set_graph_defaults(
    fontcolor='#A1B1D9',
    sortv= True
)
# Add nodes
main_node = pydot.Node('main_node',
                       label='Scarlett Johansson',
                       color='#A1B1D9',
                       penwidth=4,
                       fillcolor='#7285C7')
graph.add_node(main_node)
for node in list(ego.nodes()):
    cur_node = pydot.Node(node,
                       label=node,
                       color='#A1B1D9',
                       penwidth=4,
                      fillcolor= '#7285C7')
    graph.add_node(cur_node)
    my_edge = pydot.Edge(main_node, cur_node)
    graph.add_edge(my_edge)

graph.set_layout('fdp')
graph.write_png('output2.png')