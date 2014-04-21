import AIE
import Vec2
import Sprite
import astar
from astar import *
import astar_grid
from astar_grid import *
import astar_graph
from astar_graph import make_graph
	
iCounter = 0

Background 	= Sprite.Sprite("./images/bg.png"		   , 1024, 768, Vec2.Vec2(512, 384))
Player 		= Sprite.Sprite("./images/crate_sideup.png", 100 , 100, Vec2.Vec2(100, 100))
Enemy		= Sprite.Sprite("./images/crate_sideup.png", 100 , 100, Vec2.Vec2(800, 500))
Obstacle 	= Sprite.Sprite("./images/crate_sideup.png", 100 , 300, Vec2.Vec2(500, 300))

graph, nodes = make_graph({"width": 10, "height": 10})

graph[nodes[4][1]].remove(nodes[5][2])
graph[nodes[4][2]].remove(nodes[5][2])
graph[nodes[4][2]].remove(nodes[5][3])
graph[nodes[4][3]].remove(nodes[5][3])
graph[nodes[4][4]].remove(nodes[5][4])
graph[nodes[4][3]].remove(nodes[5][4])
graph[nodes[4][4]].remove(nodes[5][5])
graph[nodes[5][1]].remove(nodes[5][2])
graph[nodes[5][1]].remove(nodes[6][2])

paths = AStarGrid(graph)
start, end = nodes[1][1], nodes[8][5]
path = paths.search(start, end)


