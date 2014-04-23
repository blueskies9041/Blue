from Vec2 import Vec2

def Seek( current, target, speed ):
	desired_vel = (target.pos - current.pos).normal() * speed
	return desired_vel - current.vel

def Arrive( current, target, deceleration):
	to_target = target.pos - current.pos
	distance = to_target.mag()

	if distance > 0:
		speed = distance / deceleration 
		desired_vel = to_target * (speed / distance)
		return desired_vel - current.vel

	return Vec2(0,0)







	




