import sys

#store inputs into variables
input_file = sys.argv[1]
bias_param = float(sys.argv[2])
s_node = sys.argv[3]
t_node = sys.argv[4]

#read the graph given by the user in .txt file
def read_weighted_graph(input_file):
    g = {}
    with open(input_file) as input:
        for line in input:
            parts = line.split()
            n1 = parts[0]
            n2 = parts[1]
            w =  int(parts[-1])
            if n1 not in g:
                g[n1] = []
            if n2 not in g:
                g[n2] = []
            g[n1].append((n2, w))
    return (g)
g = read_weighted_graph(input_file)
#initialize all nodes to unvisited
visited = { k:False for k in g.keys() }
#temporary list where each path is created
path = []
#list where all paths from start node to end node are stored
paths = []

#Depth-first search algorithm
def allSimplePaths(g, s_node, t_node):
    visited[s_node] = True
    path.append(s_node)
    if s_node == t_node:
        paths.append(path[:])
    else:
        for v,w in g[s_node]:
            if not visited[v]:
                allSimplePaths(g, v, t_node)
    path.pop()
    visited[s_node] = False
    return paths
allSimplePaths(g,s_node,t_node)

#find each path's length
length = []
def paths_length(paths):
    for p in paths:
        l = len(p)
        length.append(l)
    return length
paths_length(paths)
#find the costs for each edge in paths list
weight = []
def find_weights(paths,g):
    for pa in paths:
        for (i,p) in enumerate(pa):
            for v,w in g[p]:
                if v == pa[i + 1]:
                    weight.append(w)
    return weight
find_weights(paths,g)
edges_num = [f-1 for f in length]

#sum the paths' costs
total = []
def totalCostPerPath(weight, edges_num):
    i = 0
    for e in edges_num:
        total.append(sum(weight[i:i+e]))
        i += e
    return total
totalCostPerPath(weight, edges_num)

#now get the shortest path and its cost
def shortest_path_position (total):
    m = min(total)
    position = total.index(m)
    return paths[position], m
print(shortest_path_position(total))

#then group the above weights per simple path
costs = []
def costPerPath(weight):
    i = 0
    for e in edges_num:
        costs.append(weight[i:i+e])
        i += e
    return costs
costPerPath(weight))

#TRYING to move on to the next starting node whick i will have to use into
#the next method in order to calculate the biased decision a man would take
results = []
new_weights = []
def biased_start_node(costs):
    for c in costs:
        result = []
        result.append(c[0])
        for i in range(1,len(c)):
            result.append(c[i] * bias_param )
        results.append(result[:])
        result.pop()
        for r in results:
            new_weights.append(sum(r[:]))
            m = min(new_weights)
    pos = new_weights.index(m)
    new_start = paths[pos][1]
    return new_start, m
biased_start_node(costs)

new_path = []
new_paths = []
def biased_paths(g, new_start, t_node):
    visited[new_start] = True
    new_path.append(new_start)
    if new_start == t_node:
        new_paths.append(new_path[:])
    else:
        for v,w in g[new_start]:
            if not visited[v]:
                biased_paths(g, v, t_node)
                biased_start_node(costs)

    new_path.pop()
    visited[new_start] = False
    return new_paths
biased_paths(g,new_start, t_node)
biased_start_node(new_weights)
