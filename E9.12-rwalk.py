from random import random

def main():
	n = int(input('How many steps? '))
	apart = nSteps(n)
	output(apart)
	
def nSteps(n):
	steps = 0
	for i in range(n):
		if random() <= 0.5:
			steps = steps + 1
		else: 
			steps = steps - 1
	return steps
	
def output(apart):
	if apart == 0:
		print("\nYou're in the same point where you started.")
	elif apart < 0:
		print("\nYou're {} steps behind the starting point.".format(abs(apart)))
	else:
		print("\nYou're {} steps ahead of the starting point.".format(apart))
		
if __name__=='__main__' : main()