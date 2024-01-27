from pygame import font
# Screen
WINDOW_NAME = "Nature simulation v1"
VISUALISATION_WIDTH = 888
VISUALISATION_HEIGHT = 888
VISUALISATION_PANEL_WIDTH = 240

# Constants for different entities
TREE = '🌳'
RABBIT = '🐇'
FOX = '🦊'
WOLF = '🐺'
EMPTY = ' '

# Grid dimensions
WIDTH = 60
HEIGHT = 60

# Colors
WHITE = (255, 255, 255)
LIGHT_WHITE = (222, 222, 222)
BLACK = (0, 0, 0)
GREY = (83, 92, 104)
ORANGE = (240, 147, 43)
YELLOW = (249, 202, 36)
GREEN = (106, 176, 76)
LIGHT_GREEN = (186, 220, 88)
LIGHT_BLUE = (126, 214, 223)
DARK_BLUE = (48, 51, 107)

# Fonts
font.init()
SMALL_FONT = font.SysFont("coopbl", 34)
MEDIUM_FONT = font.SysFont("coopbl", 42)
BIG_FONT = font.SysFont("coopbl", 52)

