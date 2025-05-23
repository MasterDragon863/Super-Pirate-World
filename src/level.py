from settings import *
from sprites import Sprite
from player import Player
import pytmx

class Level:
	def __init__(self, tmx_map: pytmx.TiledMap) -> None:
		self.display_surface: pygame.Surface = pygame.display.get_surface() # type: ignore

		# groups 
		self.all_sprites: pygame.sprite.Group = pygame.sprite.Group()
		self.collision_sprites: pygame.sprite.Group = pygame.sprite.Group()

		self.setup(tmx_map)

	def setup(self, tmx_map: pytmx.TiledMap) -> None:
		x: int
		y: int
		surf: pygame.Surface
		for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles(): # type: ignore
			Sprite((x * TILE_SIZE,y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

		for obj in tmx_map.get_layer_by_name('Objects'): # type: ignore
			if obj.name == 'player':
				Player((obj.x, obj.y), [self.all_sprites], self.collision_sprites)

	def run(self, dt):
		self.all_sprites.update(dt)
		self.display_surface.fill('black')
		self.all_sprites.draw(self.display_surface)