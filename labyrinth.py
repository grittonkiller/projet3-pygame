#-*- utf8 -*-
import json
import pygame
from pygame.locals import *
from constants import *
from classMove import *
import random
from tkinter import *

pygame.init()
#create list from class Laby
laby_un = Laby()
laby_un = laby_un.lab
laby_list = list(laby_un)


# CREATE WALL

list_wall = []
x_wall = []
y_wall = []
for c in range(len(laby_list)):
	if laby_list[c] == "o":
		list_wall.append(c)
		
for d in range(len(list_wall)):
	x_wall.append(list_wall[d] % 15 * 43)
	y_wall.append(int(list_wall[d] / 15) * 43)

#create random place of objects an affect them in list
	
nbr_Gift = 3
i = 0
x_gift = 0
y_gift = 0
while i < nbr_Gift:
	i += 1
	gift_place = random.randint(15, 210)
	if laby_list[gift_place] == " ":
		x_gift = (gift_place % 15 * 43)
		y_gift = (int(gift_place / 15) * 43)
		if i == 1:
			no_gift1 = gift_place
			laby_list[gift_place] = "i"
			x_syr = x_gift
			y_syr = y_gift
		if i == 2:
			no_gift2 = gift_place
			laby_list[gift_place] = "a"
			x_eth = x_gift
			y_eth = y_gift
		if i == 3:
			no_gift3 = gift_place
			laby_list[gift_place] = "b"
			x_pla = x_gift
			y_pla = y_gift	
	else:
		i = 0
	
#Create a window and all the parts that need to be displayed

window = pygame.display.set_mode((640, 640))

fond = pygame.image.load("background.jpg").convert()

guardian = pygame.image.load("guardian.png").convert_alpha()

wall = pygame.image.load("wall.png").convert_alpha()
position_wall = wall.get_rect()
position_wall.center = 43, 43

syringue = pygame.image.load("syringue.png").convert_alpha()
position_syringue = syringue.get_rect()

ether = pygame.image.load("ether.png").convert_alpha()
position_ether = ether.get_rect()

plastic_tube = pygame.image.load("plastic_tube.png").convert_alpha()
position_plastic_tube = plastic_tube.get_rect()
position_plastic_tube.center = 150, 150

#affect perso in class Character

perso = Character()

#assigning object display variables

display_syringue = 0
display_ether = 0
display_pla = 0

#zeroing variables

count = 0
end = 0

#move several times while holding down the key

pygame.key.set_repeat(400, 30)

#start loop for move down, up, right, and left

keep = 1
while keep:
	for event in pygame.event.get():
		if event.type == QUIT:
			keep = 0
		if event.type == KEYDOWN and end == 0:
			if event.key == K_DOWN:
				perso.displace("down")
				if laby_list[laby_list.index("m") + 15] != "o":
					new_place_m = laby_list.index("m") + 15
					laby_list[laby_list.index("m")] = laby_list[laby_list.index("m")].replace("m", " ")
					laby_list[new_place_m] = "m"

			if event.key == K_UP:
				perso.displace("up")
				if laby_list[laby_list.index("m") - 15] != "o":
					new_place_m = laby_list.index("m") - 15
					laby_list[laby_list.index("m")] = laby_list[laby_list.index("m")].replace("m", " ")
					laby_list[new_place_m] = "m"
					
			if event.key == K_RIGHT:
				perso.displace("right")
				if laby_list[laby_list.index("m") + 1] != "o":
					new_place_m = laby_list.index("m") + 1
					laby_list[laby_list.index("m")] = laby_list[laby_list.index("m")].replace("m", " ")
					laby_list[new_place_m] = "m"
					
			if event.key == K_LEFT:
				perso.displace("left")
				if laby_list[laby_list.index("m") - 1] != "o":
					new_place_m = laby_list.index("m") - 1
					laby_list[laby_list.index("m")] = laby_list[laby_list.index("m")].replace("m", " ")
					laby_list[new_place_m] = "m"

#increment the counter

	if laby_list.index("m") == no_gift1 and display_syringue == 0:
		display_syringue = 1
		count += 1
		
	if laby_list.index("m") == no_gift2 and display_ether == 0:
		display_ether = 1
		count += 1
		
	if laby_list.index("m") == no_gift3 and display_pla == 0:
		display_pla = 1
		count += 1

#display part of game	

	window.blit(fond, (0,0))
	window.blit(guardian, (600,560))

#display walls

	index_wall_x = 0
	index_wall_y = 0
	while index_wall_x < len(x_wall):
		for x in x_wall:
			x = x_wall[index_wall_x]
			index_wall_x += 1
			y = y_wall[index_wall_y]
			index_wall_y += 1
			window.blit(wall, (x,y))

#create and display count in game

	YELLOW = (255,255,0)
	RED = (255,0,0)
	GREEN = (0,255,40)
	
	font = pygame.font.SysFont("comicsansms",24,bold=False,italic=False)
	text=font.render("number of object = ",True,RED,YELLOW)
	surfacer = text.get_rect()
	surfacer.center=(310,620)
	window.blit(text, surfacer)

	font = pygame.font.SysFont("comicsansms",24,bold=False,italic=False)
	text=font.render(str(count),True,RED,YELLOW)
	surfacer = text.get_rect()
	surfacer.center=(425,620)
	window.blit(text, surfacer)

# erase the objects when MG passes over

	window.blit(perso.image,(perso.position))
	if display_syringue != 1:
		window.blit(syringue,(x_syr,y_syr))
	if display_ether != 1:
		window.blit(ether,(x_eth,y_eth))
	if display_pla != 1:	
		window.blit(plastic_tube,(x_pla,y_pla))
		
#end of game condition

	if laby_list.index("m") == 209:# place of guardian
		if count == 3:# player wins
			font = pygame.font.SysFont("comicsansms",80,bold=False,italic=False)
			text=font.render("winner",True,RED,GREEN)
			surfacer = text.get_rect()
			surfacer.center=(320,310)
			window.blit(text, surfacer)
			end = 1
		else:# player loses
			font = pygame.font.SysFont("comicsansms",80,bold=False,italic=False)
			text=font.render("you are dead !",True,GREEN,RED)
			surfacer = text.get_rect()
			surfacer.center=(320,310)
			window.blit(text, surfacer)
			end = 1

	pygame.display.flip()