import pygame
from pygame.locals import *
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
 
clock = pygame.time.Clock()
fps = 60
 
screen_width = 1000
screen_height = 1000
 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Get out')

# define font and color
font = pygame.font.SysFont('PressStart2P-Regular', 70)
font_score = pygame.font.SysFont('PressStart2P-Regular', 30)
win_font = pygame.font.Font("PressStart2P-Regular.ttf", 32)
white = (255, 255, 255)
 
# game variables
tile_size = 50
 
# Load Images
bg_img = pygame.image.load('images/bg.png')
restart_img = pygame.image.load('images/restart_btn.png')
start_img = pygame.image.load('images/start_btn.png')
exit_img = pygame.image.load('images/exit_btn.png')
 
# load sounds
pygame.mixer.music.load('sounds/game_music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
pygame.mixer.music.set_volume(0.1)
coin_fx = pygame.mixer.Sound('sounds/coin.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('sounds/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('sounds/game_over.wav')
game_over_fx.set_volume(0.5)


def main():
	game_over = 0
	main_menu = True
	score = 0
	

	#tile map layout for level
	world_data = [
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
		[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 2, 0, 5, 0, 0, 0, 1],
		[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
		[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
		[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]
	

    # create groups
	enemy_group = pygame.sprite.Group()
	platform_group = pygame.sprite.Group()
	lava_group = pygame.sprite.Group()
	coin_group = pygame.sprite.Group()
	exit_group = pygame.sprite.Group()
 
	# create player and world
	player = Player(100, screen_height - 130)
	world = World(world_data, enemy_group, platform_group, lava_group, coin_group, exit_group)
 
	# create buttons
	restart_img = pygame.transform.scale(restart_img, (200, 80))
	restart_button = Button(screen_width // 2 - 100, screen_height // 2 + 100 - 40, restart_img)
	start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
	exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)
	win_restart_button = Button(screen_width // 2 - 100, screen_height // 2 + 80, restart_img)
	

    # game loop
	run = True
	while run:
		clock.tick(fps)
		screen.blit(bg_img, (0, 0))
 
		if main_menu:
			if exit_button.draw():
				run = False
			if start_button.draw():
				main_menu = False
		else:
			world.draw()

			if game_over == 0:
				enemy_group.update()
				platform_group.update()
				game_over = player.update(game_over, world, enemy_group, platform_group, lava_group, coin_group, exit_group)
				if pygame.sprite.spritecollide(player, coin_group, True):
					score += 1
					coin_fx.play()
				draw_text('X ' + str(score), font_score, white, 60, 60)
 
			enemy_group.draw(screen)
			platform_group.draw(screen)
			lava_group.draw(screen)
			coin_group.draw(screen)
			exit_group.draw(screen)
 
			if game_over == -1:
				player.update(game_over, world, enemy_group, platform_group, lava_group, coin_group, exit_group)
				if restart_button.draw():
					world = reset_level(player, enemy_group, platform_group, lava_group, coin_group, exit_group)
					game_over = 0
					score = 0
 
			if game_over == 1:
				text = win_font.render("YOU WON!", True, (255, 255, 255))
				screen.blit(text, (screen_width // 2 - text.get_width() // 2,
								screen_height // 2 - text.get_height() // 2))
				if win_restart_button.draw():
					world = reset_level(player, enemy_group, platform_group, lava_group, coin_group, exit_group)
					game_over = 0
					score = 0
 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
 
		pygame.display.update()
 
	pygame.quit()
	
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))
 
 
def reset_level(player, enemy_group, platform_group, lava_group, coin_group, exit_group):
	player.reset(100, screen_height - 130)
	enemy_group.empty()
	platform_group.empty()
	lava_group.empty()
	coin_group.empty()
	exit_group.empty()
	
	world_data = [
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
		[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 2, 0, 5, 0, 0, 0, 1],
		[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
		[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
		[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]
 
	world = World(world_data, enemy_group, platform_group, lava_group, coin_group, exit_group)
	return world

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False #self.clicked so draw() doesn't crash when called
 
	def draw(self):
		action = False
		pos = pygame.mouse.get_pos() #Get mouse position
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		screen.blit(self.image, self.rect)
		return action
	

class Player():
	def __init__(self, x, y):
		self.reset(x, y)
 
	def update(self, game_over, world, enemy_group, platform_group, lava_group, coin_group, exit_group):
		dx = 0
		dy = 0
		walk_cooldown = 1
		col_thresh = 20

        #Assigning keys
		if game_over == 0:
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
				jump_fx.play()
				self.vel_y = -15
				self.jumped = True
			if key[pygame.K_SPACE] == False:
				self.jumped = False
			if key[pygame.K_LEFT]:
				dx -= 5
				self.counter += 1
				self.direction = -1
			if key[pygame.K_RIGHT]:
				dx += 5
				self.counter += 1
				self.direction = 1
			if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
				self.counter = 0
				self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				elif self.direction == -1:
					self.image = self.images_left[self.index]
 
			# animation
			if self.counter > walk_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images_right):
					self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				elif self.direction == -1:
					self.image = self.images_left[self.index]
 
			# add gravity so the player fall back down after jump
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y
 
			# check for collision with tiles
			self.in_air = True
			for tile in world.tile_list:
				if tile[1].colliderect(self.hitbox.x + dx, self.hitbox.y, self.hitbox.width, self.hitbox.height):
					dx = 0
				if tile[1].colliderect(self.hitbox.x, self.hitbox.y + dy, self.hitbox.width, self.hitbox.height):
					if self.vel_y < 0:
						dy = tile[1].bottom - self.hitbox.top
						self.vel_y = 0
					elif self.vel_y >= 0:
						dy = tile[1].top - self.hitbox.bottom
						self.vel_y = 0
						self.in_air = False
 
			# check for collision with enemies
			if pygame.sprite.spritecollide(self, enemy_group, False):
				game_over = -1
				game_over_fx.play()
 
			# check for collision with lava
			if pygame.sprite.spritecollide(self, lava_group, False):
				game_over = -1
				game_over_fx.play()
 
			# check for collision with exit
			if pygame.sprite.spritecollide(self, exit_group, False):
				game_over = 1
 
			# check for collision with platforms
			for platform in platform_group:
				if platform.rect.colliderect(self.hitbox.x + dx, self.hitbox.y, self.hitbox.width, self.hitbox.height):
					dx = 0
				if platform.rect.colliderect(self.hitbox.x, self.hitbox.y + dy, self.hitbox.width, self.hitbox.height):
					if abs((self.hitbox.top + dy) - platform.rect.bottom) < col_thresh:
						self.vel_y = 0
						dy = platform.rect.bottom - self.hitbox.top
					elif abs((self.hitbox.bottom + dy) - platform.rect.top) < col_thresh:
						self.hitbox.bottom = platform.rect.top - 1
						self.in_air = False
						dy = 0
					if platform.move_x != 0:
						self.hitbox.x += platform.move_direction
					if platform.move_y != 0:
						self.hitbox.y += platform.move_direction
 
			# update player coordinates
			self.hitbox.x += dx
			self.hitbox.y += dy
 
		elif game_over == -1:
			self.image = self.dead_image
			if self.hitbox.y > 200:
				self.hitbox.y -= 5
 
		self.rect.center = self.hitbox.center
		screen.blit(self.image, self.rect)
		return game_over
 
	def reset(self, x, y):
		self.images_right = [] #list of images for character animation
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range(1, 5):
			img_right = pygame.image.load(f'images/player{num}.png')
			img_right = pygame.transform.scale(img_right, (60, 80))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_left.append(img_left)
			self.images_right.append(img_right)
		self.dead_image = pygame.image.load('images/dead.png')
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect(topleft=(x, y))
		self.hitbox = self.rect.inflate(-20, 0)
		self.hitbox.center = self.rect.center
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.in_air = True





if __name__ == '__main__':
	main()