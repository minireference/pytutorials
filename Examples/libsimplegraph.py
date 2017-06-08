
# set of simple funcitons for graphs 

def explore(G,v,visited=None ):
    """ Given a graph G(V,E) and node v will return 
        a set 'visited' of all the nodes that can be reached from v """
    
    # was behaving weirdly with the set() as default parameter
    if visited==None:
        visited=set()

    visited.add(v)

    previsit(G,v)
    # go to each neighbour that has not been seen yet 
    for nbr in G.neighbors(v):
        #print "nbr: " + str(nbr)
        if nbr not in visited:
            #print ">>"
            new = explore(G,nbr,visited=visited)
            visited.update(new)
    postvisit(G,v)

    return visited


def previsit(G,v):
    pass

def postvisit(G,v):
    pass


# custom shortest path that uses edge capacity

