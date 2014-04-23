import AIE
from Vec2 import Vec2
from Sprite import *
from astar import *
from astar_grid import *
from astar_graph import make_graph
from itertools import product
	
background			= Sprite("./images/bg.png"	 				, 1024, 768, Vec2.Vec2(512, 384))
astar_pathfinder 	= Sprite("./images/astar_pathfinder.png"	, 100 , 100, Vec2.Vec2(100, 100))
djikstra_pathfinder = Sprite("./images/djikstra_pathfinder.png"	, 100 , 100, Vec2.Vec2(100, 100))
seeker				= Sprite("./images/seeker.png"				, 100 , 100, Vec2.Vec2(300, 100))
seeker_target		= Sprite("./images/seeker_target.png"		, 100 , 100, Vec2.Vec2(600, 300))
arrive_example		= Sprite("./images/arrive_example.png"		, 100 , 100, Vec2.Vec2(100, 600))	
generic_target		= Sprite("./images/generic_target.png"		, 100 , 100, Vec2.Vec2(800, 500))
obstacle		 	= Sprite("./images/plain_red_square.png" 	, 100 , 300, Vec2.Vec2(500, 400))

iCounter = 0
iCounter_djikstra = 0

graph, nodes = make_graph({"width": 10, "height": 10})

#removed edges
for i, j in product([-1, 0, 1], [-1, 0, 1]):
	graph[nodes[ 5 + i ][ 3 + j ]].remove(nodes[5][3])
	graph[nodes[ 5 + i ][ 4 + j ]].remove(nodes[5][4])
	graph[nodes[ 5 + i ][ 5 + j ]].remove(nodes[5][5])

graph[nodes[5][2]].remove(nodes[6][3])

paths = AStarGrid(graph)							# The pathfinder object
start, end = nodes[1][1], nodes[8][5]				# The start node and end node
path = paths.search(start, end)						# The list of nodes that compose the path from start to end
path_djikstra = paths.search_djikstra(start,end)	# The list of nodes that compose the path from start to end using Djikstra's alogorithm instead of the A * algorithm



