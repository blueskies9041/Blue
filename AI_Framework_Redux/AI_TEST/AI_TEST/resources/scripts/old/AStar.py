import AIE
from itertools import product
from operator import attrgetter
import pdb
import Vec2
from math import sqrt
from copy import copy

class AStarGridNode(object):
	def __init__(self, _x, _y, _pos):
		self.x = _x
		self.y = _y
		self.g = 0
		self.h = 0
		self.f = 0
		self.pos = _pos
		self.parent = None
		
class Grid(object):
	def __init__(self, _rows, _cols, _cellSize):
		self.nodes = [[AStarGridNode(x, y, Vec2.Vec2(x * _cellSize, y * _cellSize)) for y in range(_cols)] for x in range(_rows)]
		self.rows = _rows
		self.cols = _cols
		self.cellSize = _cellSize

	def DrawNodes(self):
		os = self.cellSize / 2
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				AIE.DrawLine( self.nodes[i][j].pos.x - os, self.nodes[i][j].pos.y - os, self.nodes[i][j].pos.x + os, self.nodes[i][j].pos.y - os)
				AIE.DrawLine( self.nodes[i][j].pos.x + os, self.nodes[i][j].pos.y - os, self.nodes[i][j].pos.x + os, self.nodes[i][j].pos.y + os)
		
class AStarGrid(object):
	def __init__(self):
		self.grid = Grid( 10, 10 , 100)
		self.source = self.grid.nodes[1][5]
		self.target = self.grid.nodes[8][5]
		self.current = None
		self.source.parent = self.source
		self.source.g = 0
		self.source.h = self.Heuristic(self.source, self.target)
		self.source.f = self.source.g + self.source.h
		self.openList = []
		self.openList.append(self.source)
		self.closedList = []
		self.closedList.append( self.grid.nodes[4][5] )
		self.closedList.append( self.grid.nodes[5][5] )
		self.closedList.append( self.grid.nodes[6][5] )
		print self.openList[0].x , self.openList[0].y
		#for i in range (0, self.GetNeighbors(self.source)):
			#print self.GetNeighbors(self.source)[i].x, self.GetNeighbors(self.source)[i].y
		
	def MoveCost(self, _node, _target):
		diagonal = abs( _node.x - _target.x) == 1 and abs(_node.x - _target.y) == 1
		return 14 if diagonal else 10
	
	def GetNeighbors(self, _node):
		neighbors = []
		for i,j in product([-1,0,1],[-1,0,1]):
			if not( 0 <= _node.x + i < self.grid.rows) :
				continue
			if not( 0 <= _node.y + j < self.grid.cols) :
				continue
			neighbors.append( self.grid.nodes[_node.x + i][_node.y + j] )
		return neighbors
	
	def OpenContains(self, _node):
		for i in range (0, len(self.openList)):
			if _node.x == self.openList[i].x and _node.y == self.openList[i].y:
				return True
		return False
	
	def ClosedContains(self, _node):
		for i in range (0, len(self.closedList)):
			if _node.x == self.closedList[i].x and _node.y == self.closedList[i].y:
				return True
		return False

	def Heuristic(self, _node, _end):
		 return sqrt((_end.x - _node.x)**2 + (_end.y - _node.y)**2)
		 
	def Search(self):
		if len(self.openList) > 0 :
			self.openList.sort( key = lambda x: x.f)
			self.current = self.openList[0]
			self.closedList.append(self.current)
			for i in range (0, len(self.GetNeighbors(self.current))):
				if self.ClosedContains(self.GetNeighbors(self.current)[i]):
					print "Passing..."
					pass
				if self.OpenContains(self.GetNeighbors(self.current)[i]) == False:
					print "Trigger 2"
					self.GetNeighbors(self.current)[i].parent = self.current
					self.GetNeighbors(self.current)[i].g = self.MoveCost(self.current, self.GetNeighbors(self.current)[i]) + self.current.parent.g
					self.GetNeighbors(self.current)[i].h = self.Heuristic( self.GetNeighbors(self.current)[i], self.target)
					self.GetNeighbors(self.current)[i].f = self.GetNeighbors(self.current)[i].g + self.GetNeighbors(self.current)[i].h
					self.openList.append( self.GetNeighbors(self.current)[i] )
				#if self.OpenContains(self.GetNeighbors(self.current)[i]):
					#print "Trigger 3"
					#if self.MoveCost(self.current, self.GetNeighbors(self.current)[i]) + self.current.g < self.GetNeighbors(self.current)[i].g:
						#self.GetNeighbors(self.current)[i].parent = self.current
						#self.GetNeighbors(self.current)[i].g = self.MoveCost(self.current, self.GetNeighbors(self.current)[i]) + self.current.parent.g
						#self.GetNeighbors(self.current)[i].h = self.Heuristic( self.GetNeighbors(self.current)[i], self.target)
						#self.GetNeighbors(self.current)[i].f = self.GetNeighbors(self.current)[i].g + self.GetNeighbors(self.current)[i].h
						
				if self.ClosedContains(self.target):
					print "Path Found!"
					
	def Draw(self):
		self.grid.DrawNodes()

			
		

	