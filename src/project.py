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