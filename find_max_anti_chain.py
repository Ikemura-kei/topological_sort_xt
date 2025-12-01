import networkx as nx

# Please install networkx by 'pip install networkx==3.6'

def max_anti_chain_size(dag_dict):
    nodes = set(dag_dict.keys())
    for neighbors in dag_dict.values():
        nodes.update(neighbors)
    if not nodes:
        return 0

    G = nx.DiGraph()
    for u in dag_dict:
        for v in dag_dict[u]:
            G.add_edge(u, v)

    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("Input graph is not a DAG")

    G_tc = nx.transitive_closure(G)

    G_flow = nx.DiGraph()
    source = "s"
    sink = "t"

    for u in G_tc.nodes():
        u_in = f"{u}_in"
        u_out = f"{u}_out"
        G_flow.add_edge(source, u_in, capacity=1)
        G_flow.add_edge(u_out, sink, capacity=1)

    for u, v in G_tc.edges():
        if u == v:
            continue
        u_in = f"{u}_in"
        v_out = f"{v}_out"
        G_flow.add_edge(u_in, v_out, capacity=1)

    # Max flow = maximum matching size
    flow_value, _ = nx.maximum_flow(G_flow, source, sink)

    num_nodes = len(G_tc.nodes())

    return num_nodes - flow_value

if __name__ == "__main__":
    # Example 1: A simple path graph (Width = 1)
    # 1 -> 2 -> 3
    dag_path = {1: [2], 2: [3], 3: []}
    s_max_path = max_anti_chain_size(dag_path)
    print(f"Graph 1 (Path 1->2->3): Max S size = {s_max_path}")
    # Expected: 1 (The source set S can only ever contain one node at a time)

    # Example 2: A parallel structure (Width = 2)
    # 1 -> 2
    # 3 -> 4
    dag_parallel = {1: [2], 2: [], 3: [4], 4: []}
    s_max_parallel = max_anti_chain_size(dag_parallel)
    print(f"Graph 2 (Parallel): Max S size = {s_max_parallel}")
    # Expected: 2 (The source set S can contain {1, 3} simultaneously)

    # Example 3: A diamond graph (Width = 2)
    #   /-> 2 --\
    # 1          -> 4
    #   \-> 3 --/
    dag_diamond = {1: [2, 3], 2: [4], 3: [4], 4: []}
    s_max_diamond = max_anti_chain_size(dag_diamond)
    print(f"Graph 3 (Diamond): Max S size = {s_max_diamond}")
    # Expected: 2 (The maximum anti-chain is {2, 3})

    # Example 4: XT's example
    dag_diamond = {1: [5, 6, 7], 2: [5, 6, 7], 3: [5, 6, 7], 4: [5, 6, 7], 8: [9, 10]}
    s_max_diamond = max_anti_chain_size(dag_diamond)
    print(f"Graph 3 (Diamond): Max S size = {s_max_diamond}")