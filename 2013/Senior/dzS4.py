import sys
def buildGraph(a):
    graphTall,graphLow = dict(),dict()
    for l in a:
        tall,low = l
        # if high in graph:
        #     graph[high].append([l[1],'L'])
        # else:
        #     graph[high] = [ [l[1],'L'] ] 
        # graph.setdefault(l[0],[]).append([l[1],'L'])
        graphTall.setdefault(tall,set()).add(low)
        graphLow.setdefault(low,set()).add(tall)
        # graph.setdefault(l[1],[]).append([l[0],'H'])
    return graphTall,graphLow

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        # print('QUEUE',queue,'VERTEX',vertex,'PATH',path)
        for next in graph[vertex] - set(path):
            # print(vertex,next)
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


N,M = list(map(int,input().split()))
heightList = [input().split() for i in range(M) ]
p,q = input().split()

graphTall,graphLow = buildGraph(heightList)
print(graphTall,graphLow)

# res = 'unknown'

try:
    list(bfs_paths(graphTall,p,q))
    print('yes')
    # sys.exit(0)
except:

    try:
        list(bfs_paths(graphLow,p,q))
        print('no')
        # sys.exit(0)
    except:
        print('unknown')  



