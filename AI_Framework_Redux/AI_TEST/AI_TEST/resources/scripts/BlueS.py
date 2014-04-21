import AIE
import pdb
import astar
import astar_grid
import astar_graph
import Globals
from Globals import *

#####################	
def UpdateGame():

	global iCounter
	global Background
	global Enemy
	global Player
	global Obstacle

	AIE.DrawString( " Press A for AStar Example, D for Dijkstra's algorithm " , 100, 100 )

	Background.Update()
	Enemy.Update()
	Obstacle.Update()
	Player.Update()

	#for i in range (0, 10):
		#for j in range(0, 10):
			#AIE.DrawString( str( (nodes[i][j].x, nodes[i][j].y ) ), nodes[i][j].pos.x, nodes[i][j].pos.y )

	if AIE.IsKeyDown(65) :		
		Player.vel.x = (path[iCounter].pos.x - Player.pos.x) * .01
		Player.vel.y = (path[iCounter].pos.y - Player.pos.y) * .01

		#pdb.set_trace()
		
		if path[iCounter].pos.x - 5 <= Player.pos.x < path[iCounter].pos.x + 5 and path[iCounter].pos.y - 5 <= Player.pos.y < path[iCounter].pos.y + 5 :
			if iCounter < len(path) - 1 :
				iCounter += 1
			else:
				pass
	else :
		Player.vel.x = 0
		Player.vel.y = 0
		Player.pos.x = 100
		Player.pos.y = 100
		iCounter = 0

	if AIE.IsKeyDown(68):
		pass


	

	
	