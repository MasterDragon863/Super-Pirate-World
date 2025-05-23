from settings import * 

class Sprite(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups) -> None:
		super().__init__(groups)
		self.image: pygame.Surface = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image.fill('white')
		self.rect: pygame.FRect = self.image.get_frect(topleft = pos)