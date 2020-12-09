import pygame
import sys 
import Player


def main(): 

	#Can change size later
	size = width,height = 640, 320

	screen = pygame.display.set_mode(size) 
	pygame.display.set_caption("Fantasy Football Tycoon"); 
	
	me = Player.Player(); 

	print(me.generate_name()); 


	#Main game loop
	while 1: 

		#Check for clicks/key presses/quitting
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit() 

		screen.fill((255,0,0)) 
		pygame.display.flip() 

		
	

main() 
