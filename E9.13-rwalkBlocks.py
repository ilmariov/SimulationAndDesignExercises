from random import random

def main():
	n = int(input('How many steps? '))
	dx, dy = nSteps(n)
	output(dx, dy)
	
def nSteps(n):
	dx = 0
	dy = 0
	for i in range(n):
		num = random()
		if num <= 0.25:
			dx = dx + 1
		elif 0.25 < num <= 0.5: 
			dx = dx - 1
		elif 0.5 < num <= 0.75:
			dy = dy + 1
		else:
			dy = dy - 1
	return dx, dy
	
def output(dx, dy):
	if dx==0 and dy==0:
		print("\nYou're in the same point where you started.")
	elif dx==0 and dy<0:
		print("\nYou're {} steps behind the starting point.".format(abs(dy)))
	elif dx==0 and dy>0:
		print("\nYou're {} steps ahead of the starting point.".format(dy))
	elif dx>0 and dy==0:
		print("\nYou're {} steps to the right of the starting point.".format(dx))
	elif dx>0 and dy>0:
		print("\nYou're {0} steps ahead of and {1} steps to the right  of the starting point.".format(dy, dx))
	elif dx>0 and dy<0:
		print("\nYou're {0} steps behind and {1} steps to the right of the starting point.".format(abs(dy), dx))
	elif dx<0 and dy==0:
		print("\nYou're {} steps to the left of the starting point.".format(abs(dx)))
	elif dx<0 and dy>0:
		print("\nYou're {0} steps ahead of and {1} steps to the left of the starting point.".format(abs(dy), abs(dx)))
	else:
		print("\nYou're {0} steps behind and {1} steps to the left of the starting point.".format(abs(dy), abs(dx)))
		
		
if __name__=='__main__' : main()