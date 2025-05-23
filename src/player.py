from settings import * 

class Player(pygame.sprite.Sprite):
	def __init__(self, pos: tuple[int, int], groups: list, collsion_sprites: pygame.sprite.Group) -> None:
		super().__init__(*groups)
		self.image: pygame.Surface = pygame.Surface((48,56))
		self.image.fill('red')
		self.rect: pygame.FRect = self.image.get_frect(topleft = pos)

		# movement 
		self.direction: vector = vector()
		self.speed:int = 200

	def input(self) -> None:
		keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
		input_vector: vector = vector(0,0)
		if keys[pygame.K_RIGHT]:
			input_vector.x += 1
		if keys[pygame.K_LEFT]:
			input_vector.x -= 1
		self.direction = input_vector.normalize() if input_vector else input_vector

	def move(self, dt) -> None:
		self.rect.topleft += self.direction * self.speed * dt

	def update(self, dt) -> None:
		self.input()
		self.move(dt)
