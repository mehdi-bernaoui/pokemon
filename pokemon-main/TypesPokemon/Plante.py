from Pokemon import Pokemon

class Plante(Pokemon):

	def __init__(self, nomPoke):
		Pokemon.__init__(self, nomPoke)
		self.TypeNom = "plante"
		self.nomPoke = nomPoke
		self.Tpvie = 5
		self.Tpatt = 5
		self.Tpdef = 5
		self.setVie(self.Tpvie)
		self.Typepatt = self.Tpatt + self.attaque
		self.Typedeff = self.Tpdef + self.defense