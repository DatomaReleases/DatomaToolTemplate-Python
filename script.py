import networkx as nx

def datoma_entrypoint(params, utils):
    filename = 'results/A1_a.csv'   # Create the output file on the results folder
    f = open(filename, "w")
    f.write("Filename\tNumber of nodes\tNumber of edges\tMin degree\tMax degree\tAvg degree\tAvg clustering coefficient\tAssortativity\tAvg path length\tDiameter\n")

    # Gather parameters
    dataset = params["input_file"][0]
    parameter=params["first_parameter"]
    num_cores = int(utils.get_vcpu())

    # Run the tool's code
    G = nx.read_pajek(dataset)
    print("\nWorking with file: "+str(dataset)+"...")
    G = nx.Graph(G) 
    nod = nx.number_of_nodes(G)
    noe = nx.number_of_edges(G)
    dh = nx.degree_histogram(G)
    list = [i for i, x in enumerate(dh) if x!=0]

    min_d=list[0]
    print("Min. degree: "+str(min_d))

    max_d = list[-1]
    print("Max. degree: " + str(max_d))

    acum=0
    for i in range(len(dh)):
        acum+= dh[i] * i
    avg_d = acum / nod
    print("Average degree: "+str('{:.4f}'.format(avg_d)))

    avc = nx.average_clustering(G)
    print("Average clustering coefficient: "+str('{:.4f}'.format(avc)))

    assortativity = nx.degree_assortativity_coefficient(G)
    print("Assortativity: "+str((assortativity)))

    aspl = nx.average_shortest_path_length(G)
    print("Average path length: "+str('{:.4f}'.format(aspl)))

    dia = nx.diameter(G)
    print("Diameter: "+str(dia))

    f.write(str(parameter)+"\t"+str(nod)+"\t"+str(noe)+"\t"+str(min_d)+"\t"+str(max_d)+"\t"+str('{:.4f}'.format(avg_d))+"\t"+str('{:.4f}'.format(avc))+"\t"+str('{:.4f}'.format(assortativity))+"\t"+str('{:.4f}'.format(aspl))+"\t"+str(dia)+"\n")
    
    f.close() 
    
# if __name__ == "__main__":    # test purposes 
#     datoma_entrypoint(None, None)