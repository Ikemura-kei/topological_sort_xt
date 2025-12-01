import networkx as nx

# Please install networkx by 'pip install networkx==3.6'

def max_anti_chain_size(dag_dict):
    # Finds the maximum anti-chain size in a DAG, which is the size of the largest S in Kahn's algorithm
    nodes = set(dag_dict.keys())
    
    for neighbors in dag_dict.values():
        nodes.update(neighbors)
    node_list = sorted(list(nodes))
    num_nodes = len(node_list)

    if num_nodes == 0:
        return 0

    G_flow = nx.DiGraph()
    source = 's'
    sink = 't'

    for u in node_list:
        u_in = f"{u}_in"
        u_out = f"{u}_out"

        G_flow.add_edge(source, u_in, capacity=1)

        G_flow.add_edge(u_out, sink, capacity=1)

        if u in dag_dict:
            for v in dag_dict[u]:
                v_in = f"{v}_in"
                v_out = f"{v}_out"
                
                G_flow.add_edge(u_in, v_out, capacity=1)
    
    flow_value, _ = nx.maximum_flow(G_flow, source, sink)
    
    min_path_cover_edges = flow_value
    
    min_path_cover_paths = num_nodes - min_path_cover_edges

    s_max = min_path_cover_paths

    return s_max

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