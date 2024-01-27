import pygame
from settings import *

def draw_text(surface, text,  x, y, font=MEDIUM_FONT, color=WHITE, shadow=BLACK):
	text_obj = font.render(text, 1, color)
	if shadow:
		shadow_text_obj = font.render(text, 1, shadow)
		shadow_text_rect = shadow_text_obj.get_rect()
		shadow_text_rect.center = (x+2, y+2)
		surface.blit(shadow_text_obj, shadow_text_rect)
	text_rect = text_obj.get_rect()
	text_rect.center = (x, y)
	surface.blit(text_obj, text_rect)

is_mouse_just_clicked = False
def button(surface, text, x, y, font=BIG_FONT, width=160, height=60, color=LIGHT_WHITE,
			highlight_color=WHITE, text_color=BLACK, text_shadow=False, elevation=6, button_shadow=BLACK):
	global is_mouse_just_clicked
	rect = pygame.Rect(x-width//2, y-height//2, width, height)
	mouse_pos = pygame.mouse.get_pos()
	mouse_clicked = pygame.mouse.get_pressed()[0]
	if mouse_clicked == False:
		is_mouse_just_clicked = False
	draw_shadow = True
	if rect.collidepoint(mouse_pos):
		color = highlight_color
		if mouse_clicked and is_mouse_just_clicked == False:
			is_mouse_just_clicked = True
			return True
		if mouse_clicked:
			rect.x -= elevation
			rect.y -= elevation
			x -= elevation
			y -= elevation
			draw_shadow = False
	if draw_shadow:
		pygame.draw.rect(surface, button_shadow, (rect.x-elevation, rect.y-elevation, rect.w, rect.h), border_radius=16)

	pygame.draw.rect(surface, color, rect, border_radius=16)
	draw_text(surface, text, x, y, font, text_color, text_shadow)
