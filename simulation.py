import random
import time
import os
import copy
from collections import deque
from settings import *

class Simulation:
	def __init__(self):


		# Entity states
		self.rabbits = {}  # Key: position (i, j), Value: hunger level
		self.foxes = {}    # Key: position (i, j), Value: hunger level
		self.wolves = {}   # Key: position (i, j), Value: hunger level

		self.trees = {}  # Key: position (i, j), Value: regrowth timer

		self.grid = self.create_empty_grid(WIDTH, HEIGHT)
		self.populate_grid()

		self.step = 0

	def create_empty_grid(self, width, height):
		return [[EMPTY for _ in range(width)] for _ in range(height)]

	# Function to randomly populate the grid
	def populate_grid(self):
		# Place specific numbers of rabbits first
		placed_rabbits = 0

		while placed_rabbits < 1968:
			i, j = random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1)
			if self.grid[i][j] == EMPTY:
				self.grid[i][j] = RABBIT
				self.rabbits[(i, j)] = 0  # Initial hunger level for rabbits
				placed_rabbits += 1

		# Now populate the rest of the grid randomly, including foxes and wolves
		# Make sure not to overwrite the rabbits you've already placed
		for i in range(HEIGHT):
			for j in range(WIDTH):
				if self.grid[i][j] == EMPTY:
					rand_num = random.random()
					if rand_num < 0.1:
						self.grid[i][j] = TREE
					elif rand_num < 0.12:
						self.grid[i][j] = FOX
						self.foxes[(i, j)] = 0  # Initial hunger level for foxes
					elif rand_num < 0.14:
						self.grid[i][j] = WOLF
						self.wolves[(i, j)] = 0  # Initial hunger level for wolves


	# Function to find nearest entity of a specific type
	def find_nearest(self, start_pos, entity_type):
		visited = set()
		queue = deque([start_pos])

		while queue:
			current_pos = queue.popleft()
			i, j = current_pos

			# Check if the current position is the target entity
			if self.grid[i][j] == entity_type:
				return current_pos

			# Add adjacent positions to the queue
			for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
				if 0 <= x < HEIGHT and 0 <= y < WIDTH and (x, y) not in visited:
					visited.add((x, y))
					queue.append((x, y))

		# Return None if no entity found
		return None

	def reproduce_rabbits(self, position):
		# Check if the rabbit at the given position is not hungry
		if self.rabbits[position] == 0:
			# Find an adjacent empty cell for the new rabbit
			i, j = position
			adjacent_positions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
			random.shuffle(adjacent_positions)
			for new_i, new_j in adjacent_positions:
				if 0 <= new_i < HEIGHT and 0 <= new_j < WIDTH and self.grid[new_i][new_j] == EMPTY:
					self.grid[new_i][new_j] = RABBIT
					self.rabbits[(new_i, new_j)] = 0  # New rabbit is not hungry
					break



	def move_rabbits(self):
		new_rabbits = {}

		for position in list(self.rabbits.keys()):
			i, j = position

			# Check if the rabbit still exists at this position
			if self.grid[i][j] != RABBIT:
				continue

			# Determine the movement of the rabbit
			new_positions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
			random.shuffle(new_positions)  # Randomize potential new positions

			moved = False
			for new_i, new_j in new_positions:
				if 0 <= new_i < HEIGHT and 0 <= new_j < WIDTH:
					if self.grid[new_i][new_j] == TREE:
						# Rabbit eats the tree and resets hunger
						self.rabbits[position] = 0
						self.grid[new_i][new_j] = RABBIT
						self.grid[i][j] = EMPTY
						new_rabbits[(new_i, new_j)] = self.rabbits[position]
						self.trees[(new_i, new_j)] = 3  # Set the regrowth timer for the tree
						moved = True
						break
					elif self.grid[new_i][new_j] == EMPTY:
						# Increase hunger if not eating
						self.rabbits[position] += 1
						self.grid[new_i][new_j] = RABBIT
						self.grid[i][j] = EMPTY
						new_rabbits[(new_i, new_j)] = self.rabbits[position]
						moved = True
						break

			# Reproduce if the rabbit has not moved and is not hungry
			if not moved:
				self.reproduce_rabbits(position)

		self.rabbits = new_rabbits

	def reproduce_rabbits(self, position):
		reproduction_hunger_threshold = 0  # Rabbits can reproduce when not hungry

		if self.rabbits.get(position, 0) <= reproduction_hunger_threshold:
			i, j = position
			adjacent_positions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

			for new_i, new_j in adjacent_positions:
				if 0 <= new_i < HEIGHT and 0 <= new_j < WIDTH and self.grid[new_i][new_j] == EMPTY:
					self.grid[new_i][new_j] = RABBIT
					self.rabbits[(new_i, new_j)] = 0  # New rabbit is not hungry


	def is_closer(self, pos1, pos2, reference):
		""" Check if pos1 is closer to the reference point than pos2. """
		return self.distance(pos1, reference) < self.distance(pos2, reference)

	def distance(self, pos1, pos2):
		""" Calculate exact distance between two points. """
		return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5



	def regrow_trees(self):
		trees_to_regrow = []
		for position, timer in self.trees.items():
			if timer > 0:
				self.trees[position] -= 1
			elif self.trees[position] == 0:
				# only regrow if the cell is empty
				if self.grid[position[0]][position[1]] == EMPTY:
					trees_to_regrow.append(position)

		for position in trees_to_regrow:
			i, j = position
			self.grid[i][j] = TREE
			del self.trees[position]  # Remove the tree from the regrowth tracking


	def move_foxes(self):
		new_foxes = {}
		for position in list(self.foxes.keys()):
			i, j = position

			# Check if the fox still exists at this position
			if self.grid[i][j] != FOX:
				continue

			# Implement smarter hunting behavior
			nearest_rabbit = self.find_nearest(position, RABBIT)

			# Determine the best move for hunting
			if nearest_rabbit:
				best_move = None
				min_distance = float('inf')
				for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
					if 0 <= x < HEIGHT and 0 <= y < WIDTH and self.grid[x][y] in [EMPTY, RABBIT]:
						dist = self.distance((x, y), nearest_rabbit)
						if dist < min_distance:
							min_distance = dist
							best_move = (x, y)

				if best_move:
					new_i, new_j = best_move
					if self.grid[new_i][new_j] == RABBIT:
						self.foxes[position] = 0  # Reset hunger
						# Remove the eaten rabbit
						self.rabbits.pop(nearest_rabbit, None)
					else:
						self.foxes[position] += 1  # Increase hunger

					self.grid[i][j] = EMPTY
					self.grid[new_i][new_j] = FOX
					new_foxes[best_move] = self.foxes[position]
				else:
					# Move randomly if no rabbit is within range
					random_move = random.choice([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
					if 0 <= random_move[0] < HEIGHT and 0 <= random_move[1] < WIDTH and self.grid[random_move[0]][random_move[1]] == EMPTY:
						self.grid[i][j] = EMPTY
						self.grid[random_move[0]][random_move[1]] = FOX
						new_foxes[random_move] = self.foxes[position]
			else:
				# Move randomly if no rabbit is found
				random_move = random.choice([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
				if 0 <= random_move[0] < HEIGHT and 0 <= random_move[1] < WIDTH and self.grid[random_move[0]][random_move[1]] == EMPTY:
					self.grid[i][j] = EMPTY
					self.grid[random_move[0]][random_move[1]] = FOX
					new_foxes[random_move] = self.foxes[position]

		self.foxes = new_foxes

	def move_wolves(self):
		new_wolves = {}
		for position in list(self.wolves.keys()):
			i, j = position

			# Check if the wolf still exists at this position
			if self.grid[i][j] != WOLF:
				continue
			# Find nearest rabbit and fox
			nearest_rabbit = self.find_nearest(position, RABBIT)
			nearest_fox = self.find_nearest(position, FOX)
			# Determine the closest prey
			nearest_prey = None
			if nearest_rabbit and nearest_fox:
				if self.is_closer(nearest_rabbit, nearest_fox, position):
					nearest_prey = nearest_rabbit
				else:
					nearest_prey = nearest_fox
			elif nearest_rabbit:
				nearest_prey = nearest_rabbit
			elif nearest_fox:
				nearest_prey = nearest_fox

			# Move towards the nearest prey
			new_positions = []
			if nearest_prey:
				for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
					if 0 <= x < HEIGHT and 0 <= y < WIDTH and self.grid[x][y] in [EMPTY, RABBIT, FOX]:
						if self.is_closer((x, y), position, nearest_prey):
							new_positions.append((x, y))
			# Move wolf if possible
			if new_positions:
				new_pos = random.choice(new_positions)
				new_i, new_j = new_pos

				# Eat prey if present
				if self.grid[new_i][new_j] in [RABBIT, FOX]:
					self.wolves[position] = 0  # Reset hunger
				else:
					self.wolves[position] += 1  # Increase hunger

				self.grid[i][j] = EMPTY
				self.grid[new_i][new_j] = WOLF
				new_wolves[new_pos] = self.wolves[position]
			else: # the wolf can't move
				new_wolves[position] = self.wolves[position]
		self.wolves = new_wolves

	def display_grid(self):
		os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for each new display
		for row in self.grid:
			print(' '.join(row))
		print("\nSimulation Step Completed. Press Ctrl+C to stop.")

	def run_simulation_one_step(self):

		self.move_rabbits()
		self.move_foxes()
		self.move_wolves()
		self.regrow_trees()
		# self.display_grid()
		self.step += 1


# if __name__ == "__main__":
#     run_simulation()
