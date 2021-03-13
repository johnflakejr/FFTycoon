import pygame
import sys 
import Player
import Team



def main(): 

  #Can change size later
  size = width,height = 640, 320

  screen = pygame.display.set_mode(size) 

  pygame.display.set_caption("Fantasy Football Tycoon"); 

  me = Player.Player("QB"); 
  print("Made player:\n",me)

  #Main game loop
  while True: 

    #Check for clicks/key presses/quitting
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        sys.exit() 
      elif event.type == pygame.MOUSEBUTTONDOWN and 1 == event.button:
        print("Player pressed the mouse at location:", str(pygame.mouse.get_pos())) 

    screen.fill((255,0,0)) 
    pygame.display.flip() 

main() 
#EOF
