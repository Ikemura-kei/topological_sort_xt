import numpy as np

test_cases = {'dags': [], 'largest_|S|': []}

# A simple path graph (Width = 1)
# 1 -> 2 -> 3
test_cases['dags'].append({1: [2], 2: [3], 3: []})
test_cases['largest_|S|'].append(1)

# A parallel structure 
# 1 -> 2
# 3 -> 4
test_cases['dags'].append({1: [2], 2: [], 3: [4], 4: []})
test_cases['largest_|S|'].append(2)

# A diamond graph
#   /-> 2 --\
# 1          -> 4
#   \-> 3 --/
test_cases['dags'].append({1: [2, 3], 2: [4], 3: [4], 4: []})
test_cases['largest_|S|'].append(2)

# XT's example
test_cases['dags'].append({1: [5, 6, 7], 2: [5, 6, 7], 3: [5, 6, 7], 4: [5, 6, 7], 8: [9, 10]})
test_cases['largest_|S|'].append(6)

# Course webpage example 1
test_cases['dags'].append({0: [1], 1: [2], 2: [3]})
test_cases['largest_|S|'].append(1)

# Course webpage example 2
test_cases['dags'].append({0: [4], 1: [2, 3], 2: [4], 3: [4]})
test_cases['largest_|S|'].append(3)

# Extra
test_cases['dags'].append({1: [4, 5], 2: [4, 5], 3: [4, 5], 5: [6, 7, 8, 9, 10]})
test_cases['largest_|S|'].append(6)


if __name__ == "__main__":
    from find_max_anti_chain import max_anti_chain_size
    for test_case_idx in range(len(test_cases['dags'])):
        input_dag = test_cases['dags'][test_case_idx]
        answer = test_cases['largest_|S|'][test_case_idx]
        
        S_by_max_anti_chain_size = max_anti_chain_size(input_dag)
        
        print("Test case {}, DAG {}, answer {}, max anti-chain size {}".format(test_case_idx, input_dag, answer, S_by_max_anti_chain_size))
        