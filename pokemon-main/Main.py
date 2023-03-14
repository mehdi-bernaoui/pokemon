import sys
import time
import random
sys.path.append('./TypesPokemon')
from TypesPokemon.Eau import *
from TypesPokemon.Feu import *
from TypesPokemon.Plante import *
from TypesPokemon.Sol import *
from TypesPokemon.Pokemon import *
import json

class Combat:

	def __init__(self, poke1, poke2):
		self.joueur = 1
		self.combat = False
		self.poke1 = poke1
		self.poke2 = poke2
		self.pkm1Pv = self.poke1.getVie()
		self.pkm2Pv = self.poke2.getVie()

	def VerifVie(self):
		if self.poke1.getVie() <= 0:
			self.combat = True
			print("Le", self.poke1.getNom(), "n'est plus apte au combat. \nVictoire de", self.poke2.getNom())
			return True
		elif self.poke2.getVie() <= 0:
			self.combat = True
			print("Le", self.poke2.getNom(), "n'est plus apte au combat.\nVictoire de",self.poke1.getNom())
			return True

	def attaque(self, atta, defens):
		alea = random.randint(0,2)
		self.degatType(atta, defens)
		if alea != 0:
			degats = (atta.attaque * self.multiplier) - defens.defense
			defens.moinsPV(degats)
			print ("\033[1;31m", atta.getNom(), "a touché avec son attaque.\033[0m")
			print("\033[1;34mPv restant de", defens.getNom(),":", defens.getVie(),"\033[0m")
		else:
			print ("\033[1;31m",atta.getNom(), "a raté son attaque.\033[0m")
			print("\033[1;34mPv restant de", defens.getNom(),":", defens.getVie(),"\033[0m")

	def combatpoke(self):

		while self.combat != True:
			self.VerifVie()
			self.attaque(self.poke1, self.poke2)
			self.VerifVie()
			#time.sleep(0.65)
			self.attaque(self.poke2, self.poke1)
			time.sleep(0.65)

	def degatType(self, atta, defens):
		self.multiplier = 1
		if atta.TypeNom == "feu":
			if defens.TypeNom == "eau":
				self.multiplier = 0.5
			elif defens.TypeNom == "plante":
				self.multiplier = 2
			elif defens.TypeNom == "sol":
				self.multiplier = 1
			else:
				self.multiplier =1
		elif atta.TypeNom == "eau":
			if defens.TypeNom == "feu":
				self.multiplier = 2
			elif defens.TypeNom == "plante":
				self.multiplier = 0.5
			elif defens.TypeNom == "sol":
				self.multiplier = 1
			else:
				self.multiplier =1
		elif atta.TypeNom == "plante":
				if defens.TypeNom == "eau":
					self.multiplier = 2
				elif defens.TypeNom == "feu":
					self.multiplier = 0.5
				elif defens.TypeNom == "sol":
					self.multiplier = 1
				else:
					self.multiplier =1


Salameche = Feu("Salameche")
Germinion = Plante("Germinion")
Kaiminus = Eau("Kaiminus")
Sabelette = Sol("Sabelette")


Duel1 = Combat(Salameche, Germinion)
Duel1.combatpoke()

Duel2 = Combat(Kaiminus, Sabelette)
Duel2.combatpoke()


# Duel2 = Combat(Kaiminus, Sabelette)
# Duel2.combatpoke()