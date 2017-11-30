import argparse
import networkx as nx
import random
import matplotlib.pyplot as plt

"""
======================================================================
  Complete the following function.
======================================================================
"""

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    G = nx.Graph()
    edges = []
    ddict = {}
    #need a way to deal with constraints that don't tell us anyting new
    for con in constraints: 
        if (con[0], con[1]) not in edges:
            edges.append((con[0],con[1]))
            G.add_edge(con[0],con[1])
        # if (con[0], con[2]) in edges and (con[1], con[2]) not in edges:
        #     edges.append((con[1],con[2]))
        #     G.add_edge(con[1],con[2])
        # elif (con[1], con[2]) in edges and (con[0], con[2]) not in edges:
        #     edges.append((con[0],con[2]))
        #     G.add_edge(con[0],con[2])
        elif (con[1], con[2]) not in edges and (con[0], con[2]) not in edges:
            if G.degree(con[0]) == {} and G.degree(con[1]) == {}:
                k = random.randint(0, 1)
                edges.append((con[k],con[2]))
                G.add_edge(con[k],con[2])
            elif G.degree(con[0]) == {}: 
                edges.append((con[0],con[2]))
                G.add_edge(con[0],con[2])
            elif G.degree(con[1]) == {}:
                edges.append((con[1],con[2]))
                G.add_edge(con[1],con[2])
            elif G.degree(con[0]) < G.degree(con[1]):
                edges.append((con[0],con[2]))
                G.add_edge(con[0],con[2])
            elif G.degree(con[0]) > G.degree(con[1]):
                edges.append((con[1],con[2]))
                G.add_edge(con[1],con[2])
            else:
                k = random.randint(0, 1)
                edges.append((con[k],con[2]))
                G.add_edge(con[k],con[2])

    #G.add_edges_from(edges)

    for wiz in wizards:
        ddict[wiz] = G.degree(wiz)

    start = max(ddict, key=ddict.get)
    final = hamilton(G, start)
    plt.subplot(121)
    nx.draw_networkx(G)
    plt.show()
    print("executed")
    return final

def hamilton(G, start):
    F = [(G,[start])]
    n = G.number_of_nodes()
    result = []
    while F:
        graph,path = F.pop()
        confs = []
        for node in graph.neighbors(path[-1]):
            conf_p = path[:]
            conf_p.append(node)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            result = p
            if len(p)==n:
                return p
            else:
                F.append((g,p))
    return result
"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)
                
    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)
