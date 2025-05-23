from pygame.time import get_ticks
from typing import Callable

class Timer:
	def __init__(self, duration: int, func: None | Callable = None, repeat: bool = False) -> None:
		self.duration: int = duration
		self.func: Callable | None = func
		self.start_time: int = 0
		self.active: bool = False
		self.repeat: bool = repeat

	def activate(self) -> None:
		self.active = True
		self.start_time = get_ticks()

	def deactivate(self) -> None:
		self.active = False
		self.start_time = 0
		if self.repeat:
			self.activate()

	def update(self) -> None:
		current_time: int = get_ticks()
		if current_time - self.start_time >= self.duration:
			if self.func and self.start_time != 0:
				self.func()
			self.deactivate()

