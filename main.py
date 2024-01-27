import pygame
import simulation
from settings import *
from simulation import Simulation
from visualisation import Visualisation

pygame.init()

simulation = Simulation()
visualisation = Visualisation()

if __name__ == "__main__":
	print("Press <SPACE> to run one step, press <ARROW UP> to run continuously")
	while True:
		visualisation.draw(simulation)
		keys_just_pressed = visualisation.events()
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_UP]:
			simulation.run_simulation_one_step()
		if pygame.K_SPACE in keys_just_pressed:
			simulation.run_simulation_one_step()
		visualisation.update()
