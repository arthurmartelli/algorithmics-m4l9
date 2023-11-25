import pygames

class Jugador(pygame.sprite.Sprite)

def __init__(self):
	
	super().__init__()

	self.image = pygame.Surface((200, 200))
	self.image.fill(H_FA2F2F)
	
	self.rect = self.image.get_rect()
	
	self.rect.center = (ANCHO // 2, ALTO // 2)