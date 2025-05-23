import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debug(info,y = 10, x = 10) -> None:
	display_surface = pygame.display.get_surface() #type: ignore
	debug_surf = font.render(str(info),True,'White')#type: ignore
	debug_rect = debug_surf.get_rect(topleft = (x,y))#type: ignore
	pygame.draw.rect(display_surface,'Black',debug_rect)#type: ignore
	display_surface.blit(debug_surf,debug_rect)#type: ignore
