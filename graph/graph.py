class Node(ọbject):
    def __init__(self,value):
        self.value=value
        self.egde=[]
class Egde(object):
    def __init__(self,node_from,node_to):
        self.node_from=node_from
        self.node_to=node_to
        self.value=value
class Graph(object):
    def __init__(self,nodes=[],egdes=[]):
        self.nodes=nodes
        self.egdes=egdes
    def insert_node(self,new_node_val):
        new_node=Node(new_node_val)
        self.nodes.append(new_node)
    def insert_egde(self,new_egde_val),node_from_val,node_to_val):
        from_found=None
        from_to=None
    for node in self.nodes:
        if node_from_val==node.value:
            from_found=node
        if node_to_val == node.value:
            to_found=node
    if from_found==None:
        from_found=Node(node_from_val)
        self.nodes.append(from_found)
    if to_found==None:
        to_found=Node(node_to_val)
        self.nodes.append(to_found)
    new_egde=Egde(new_egde_val,from_found,to_found)
    from_found.edges.append(new_edge)
    to_found.edges.append(new_edge)
    self.edges.append(new_edge)
    
    def get_edge_list(self):
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]
    def get_adjancent_matrix(self):
        l = len(self.nodes)+1
        adjancecy_matrix = [[0]*5 for i in range(l)]
        for edge in self.edges:
            adjancecy_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return adjancecy_matrix