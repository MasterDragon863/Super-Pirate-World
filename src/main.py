from typing import NoReturn
from settings import * 
from level import Level
from pytmx.util_pygame import load_pygame
import pytmx
from os.path import join

class Game:
	def __init__(self) -> None:
		pygame.init()
		self.display_surface: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Super Pirate World')
		self.clock: pygame.Clock = pygame.time.Clock()

		self.tmx_maps: dict[int, pytmx.TiledMap] = {0: load_pygame(join('data', 'levels', 'omni.tmx'))}
		self.current_stage: Level = Level(self.tmx_maps[0])

	def run(self) -> NoReturn:
		while True:
			dt: float = self.clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.current_stage.run(dt)
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()