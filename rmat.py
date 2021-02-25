# Size per edge (asci)
EDGE_SIZE_IN_GB = 20 / 1250000000.0

# Output directoty
out_dir_cluster = "/home/ubuntu/cephstorage/graphs"
shell_script = "rmat.sh"

# RMAT Params
rmat_a = 0.57
rmat_b = 0.19
rmat_c = 0.19

# Graph size and ratio  vertices to edges
min_edges = 2000000000
max_edges = 4000000000
step = 500000000
ratio_vertices_to_edges = 30

# Create RMAT command
def create_graph(rmat_a, rmat_b, rmat_c, num_vertices, num_edges):
    cmd = "./Release/PaRMAT -a {} -b {} -c {} -nVertices {} -nEdges {} -noEdgeToSelf -noDuplicateEdges -threads 4 -memUsage 0.7 -output {}/rmat-{}-{}"
    return cmd.format(rmat_a, rmat_b, rmat_c, num_vertices, num_edges, out_dir_cluster, num_edges, num_vertices)

# Clear file an write lines. 
def write(filename, l):
    lines = map(lambda x: str(x + "\n"), l) 
    f = open(filename, "w")
    f.write(''.join(lines))
    f.close() 

# Create graphs 
graphs = []
estimated_storage = 0
for num_edges in range(min_edges, max_edges + 1, step):
    estimated_storage += (num_edges * EDGE_SIZE_IN_GB)
    num_vertices = int(num_edges / ratio_vertices_to_edges)
    graphs.append(create_graph(rmat_a, rmat_b, rmat_c, num_vertices, num_edges))

print("You need around", estimated_storage, "GB")
print("Write the rmat commands to", shell_script)

write(shell_script, graphs)






