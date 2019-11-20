#-*- coding: utf8 -*-
import pygame
from pygame.locals import *
import constants
import json

#create labyrinthe
class Laby:
	def __init__(self):
		listing = create_maze()
		for a_letter in listing:# change all character for "o"
			if (a_letter == "_") or (a_letter == "|"):
				listing = listing.replace(a_letter, "o")
		self.lab = listing
		
def create_maze():
	listing = [] #create empty list
	with open("labyjson.json") as f:
		data = json.load(f) #implement data for read json file
		for entry in data: 
			listing.append(entry["lab01"])#add all line

	listing = "".join(listing)# make chain
	return listing

#create class Character

class Character:
	def __init__(self):# character initialization
		self.image = pygame.image.load("macGyver.png").convert_alpha()
		self.position = self.image.get_rect()
		self.position.center = 59, 64
		self.colision = Laby()
		
	def displace(self, direction): # movement method
		if direction == "up": # movement up
			listing_m = list(self.colision.lab)
			if listing_m[self.colision.lab.index("m") - 15] != "o": # no wall at the top
				place_m = self.colision.lab.index("m") - 15 # new place of "m"
				self.colision.lab = self.colision.lab.replace("m", " ") # replace "m"
				place_m = int(place_m)
				listing_m = list(self.colision.lab)
				listing_m[place_m] = "m" #affect "m"
				self.colision.lab = "".join(listing_m)
				self.position = self.position.move(0, -43) #move "m"
				
				

				
		if direction == "down": # movement down
			listing_m = list(self.colision.lab)
			if listing_m[self.colision.lab.index("m") + 15] != "o":# no wall down
				place_m = self.colision.lab.index("m") + 15
				self.colision.lab = self.colision.lab.replace("m", " ")
				place_m = int(place_m)
				listing_m = list(self.colision.lab)
				listing_m[place_m] = "m"
				self.colision.lab = "".join(listing_m)
				self.position = self.position.move(0, 43)

		if direction == "right":# movement right
			listing_m = list(self.colision.lab)
			if listing_m[self.colision.lab.index("m") + 1] != "o":# no wall on the right
				place_m = self.colision.lab.index("m") + 1
				self.colision.lab = self.colision.lab.replace("m", " ")
				place_m = int(place_m)
				listing_m = list(self.colision.lab)
				listing_m[place_m] = "m"
				self.colision.lab = "".join(listing_m)
				self.position = self.position.move(43, 0)
				
		if direction == "left":# movement left
			listing_m = list(self.colision.lab)
			if listing_m[self.colision.lab.index("m") - 1] != "o":# no wall on the left
				place_m = self.colision.lab.index("m") - 1
				self.colision.lab = self.colision.lab.replace("m", " ")
				place_m = int(place_m)
				listing_m = list(self.colision.lab)
				listing_m[place_m] = "m"
				self.colision.lab = "".join(listing_m)
				self.position = self.position.move(-43, 0)	
				
		

		