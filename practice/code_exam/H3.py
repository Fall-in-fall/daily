import sys

x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())

graph={ 1:[ 0,2,10,5,3,-1],
     	2:[-1,0,12,-1,-1,10],
      	3:[-1,-1,0,-1,7,0],
      	4:[2,-1,-1,0,2,-1],
      	5:[4,-1,-1,1,0,-1],
      	6:[3,-1,1,-1,2,0],
        }

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for i in xrange(1,7):
        if i not in path and graph[start][i-1]>-1:
            newpaths=find_all_paths(graph, i, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
