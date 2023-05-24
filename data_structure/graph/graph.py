# resource: https://www.tutorialspoint.com/python_data_structure/python_graphs.htm
# use dict to store graph in python

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # print vertices
    def getVertices(self):
        return list(self.gdict.keys())

    # print edges
    def findedges(self):
        edgename = []
        for v in self.gdict:
            for next_v in self.gdict[v]:
                if {next_v, v} not in edgename:
                    edgename.append({v, next_v})
        return edgename

    # add vertice
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []
