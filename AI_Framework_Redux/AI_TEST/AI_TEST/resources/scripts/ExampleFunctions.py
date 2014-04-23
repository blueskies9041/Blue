import AIE
import Vec2
import Globals
from Globals import *
import Behaviors
from Behaviors import *
import pdb

def update_sprites():
	background.Update()
	obstacle.Update()
	djikstra_pathfinder.Update()
	astar_pathfinder.Update()
	seeker.Update()
	seeker_target.Update()
	arrive_example.Update()
	generic_target.Update()

def show_instructions():
	AIE.DrawString( " Hold a key: (A):AStar, (D)Djikstra, (S)Seek, (R)Arrival " , 100, 700 )

def check_debug_activation():
	if AIE.IsKeyDown(32):
		pdb.set_trace()

def example_astar():
	global iCounter

	if AIE.IsKeyDown(65) :	
		astar_pathfinder.vel.x = (path[iCounter].pos.x - astar_pathfinder.pos.x) * .1
		astar_pathfinder.vel.y = (path[iCounter].pos.y - astar_pathfinder.pos.y) * .1
	
		if path[iCounter].pos.x - 5 <= astar_pathfinder.pos.x < path[iCounter].pos.x + 5 and path[iCounter].pos.y - 5 <= astar_pathfinder.pos.y < path[iCounter].pos.y + 5 :
			if iCounter < len(path) - 1 :
				iCounter += 1
			else:
				pass
	else :
		astar_pathfinder.pos.x = 100
		astar_pathfinder.pos.y = 100
		iCounter = 0

def example_djikstra():
	global iCounter_djikstra

	if AIE.IsKeyDown(68):
		djikstra_pathfinder.vel.x = (path_djikstra[iCounter_djikstra].pos.x - djikstra_pathfinder.pos.x) * .1
		djikstra_pathfinder.vel.y = (path_djikstra[iCounter_djikstra].pos.y - djikstra_pathfinder.pos.y) * .1
	
		if path_djikstra[iCounter_djikstra].pos.x - 5 <= djikstra_pathfinder.pos.x < path_djikstra[iCounter_djikstra].pos.x + 5 and path_djikstra[iCounter_djikstra].pos.y - 5 <= djikstra_pathfinder.pos.y < path_djikstra[iCounter_djikstra].pos.y + 5 :
			if iCounter_djikstra < len(path_djikstra) - 1 :
				iCounter_djikstra += 1
			else:
				pass
	else :
		djikstra_pathfinder.pos.x = 100
		djikstra_pathfinder.pos.y = 100
		iCounter_djikstra = 0

def example_seek():

	if seeker_target.pos.x >= 600 and seeker_target.pos.y >= 200:
		seeker_target.vel.x = 0
		seeker_target.vel.y = 1
	if seeker_target.pos.x >= 600 and seeker_target.pos.y >= 600:
		seeker_target.vel.x = -1
		seeker_target.vel.y = 0
	if seeker_target.pos.x <= 400 and seeker_target.pos.y >= 600:
		seeker_target.vel.x = 0
		seeker_target.vel.y = -1
	if seeker_target.pos.x <= 400 and seeker_target.pos.y <= 200:
		seeker_target.vel.x = 1
		seeker_target.vel.y = 0

	if AIE.IsKeyDown(83):
		seeker.vel.x += Seek(seeker, seeker_target, 3).x
		seeker.vel.y += Seek(seeker, seeker_target, 3).y
	else:
		seeker.vel.x = 0
		seeker.vel.y = 0

def example_arrive():
	if AIE.IsKeyDown(82):
		arrive_example.vel.x += Arrive(arrive_example, generic_target, 50.0).x
		arrive_example.vel.y += Arrive(arrive_example, generic_target, 50.0).y
	else:
		arrive_example.vel.x = 0
		arrive_example.vel.y = 0
		arrive_example.pos.x = 100
		arrive_example.pos.y = 600



