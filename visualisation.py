import pygame
import sys
from settings import *
import gui

def load_image(path, width, height):
	image = pygame.image.load(path).convert_alpha()
	image = pygame.transform.smoothscale(image, (width, height))
	return image

class Visualisation:
	def __init__(self):
		self.mainClock = pygame.time.Clock()
		self.SCREEN = pygame.display.set_mode((VISUALISATION_WIDTH + VISUALISATION_PANEL_WIDTH, VISUALISATION_HEIGHT), 0, 32)
		pygame.display.set_caption(WINDOW_NAME)

		self.cell_width = VISUALISATION_WIDTH // WIDTH
		self.cell_height = VISUALISATION_HEIGHT // HEIGHT

		# images
		self.tree_image = load_image("assets/tree.png", self.cell_width, self.cell_height)
		self.rabbit_image = load_image("assets/rabbit.png", self.cell_width//1.2, self.cell_height//1.2)
		self.fox_image = load_image("assets/fox.png", self.cell_width, self.cell_height)
		self.wolf_image = load_image("assets/wolf.png", self.cell_width, self.cell_height)

		self.transition_speed = 1000 # ms
		self.start_transition_time = 0



	def draw_panel(self, simulation):
		# draw the background
		pygame.draw.rect(self.SCREEN, DARK_BLUE, (VISUALISATION_WIDTH, 0, VISUALISATION_PANEL_WIDTH, VISUALISATION_HEIGHT))
		text_x_pos = VISUALISATION_WIDTH + VISUALISATION_PANEL_WIDTH // 2
		# draw the title
		gui.draw_text(self.SCREEN, WINDOW_NAME, text_x_pos, 50, font=SMALL_FONT, color=YELLOW)
		# draw the stats
		gui.draw_text(self.SCREEN, f"Step: {simulation.step}", text_x_pos, 150)
		pygame.draw.line(self.SCREEN, GREY, (VISUALISATION_WIDTH, 190), (VISUALISATION_WIDTH + VISUALISATION_PANEL_WIDTH, 190), 2)
		gui.draw_text(self.SCREEN, f"Trees: {len(simulation.trees)}", text_x_pos, 225, color=GREEN)
		gui.draw_text(self.SCREEN, f"Rabbits: {len(simulation.rabbits)}", text_x_pos, 260, color=WHITE)
		gui.draw_text(self.SCREEN, f"Foxes: {len(simulation.foxes)}", text_x_pos, 295, color=ORANGE)
		gui.draw_text(self.SCREEN, f"Wolves: {len(simulation.wolves)}", text_x_pos, 330, color=GREY)
		pygame.draw.line(self.SCREEN, GREY, (VISUALISATION_WIDTH, 370), (VISUALISATION_WIDTH + VISUALISATION_PANEL_WIDTH, 370), 2)

		# draw the buttons
		if gui.button(self.SCREEN, "Next", text_x_pos, 640):
			simulation.run_simulation_one_step()
			self.start_transition_time = pygame.time.get_ticks()



	def draw_simulation(self, simulation):
		pygame.draw.rect(self.SCREEN, LIGHT_GREEN, (0, 0, VISUALISATION_WIDTH, VISUALISATION_HEIGHT))
		for y in range(HEIGHT):
			for x in range(WIDTH):
				cell = simulation.grid[y][x]
				rect = pygame.rect.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
				center_rect = rect.center
				if cell == TREE:
					# pygame.draw.rect(self.SCREEN, GREEN, rect)
					self.SCREEN.blit(self.tree_image, self.tree_image.get_rect(center=center_rect))
					pass
				elif cell == RABBIT:
					# pygame.draw.rect(self.SCREEN, WHITE, rect)
					self.SCREEN.blit(self.rabbit_image, self.rabbit_image.get_rect(center=center_rect))
					pass
				elif cell == FOX:
					# pygame.draw.rect(self.SCREEN, ORANGE, rect)
					self.SCREEN.blit(self.fox_image, self.fox_image.get_rect(center=center_rect))
					pass
				elif cell == WOLF:
					# pygame.draw.rect(self.SCREEN, GREY, rect)
					self.SCREEN.blit(self.wolf_image, self.wolf_image.get_rect(center=center_rect))

	def draw(self, simulation):
		self.draw_simulation(simulation)
		self.draw_panel(simulation)


	def events(self):
		keys_pressed = []
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				keys_pressed.append(event.key)
		return keys_pressed

	def update(self):
		pygame.display.update()
		self.mainClock.tick(90)
