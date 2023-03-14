class Pokemon:

	def __init__(self, nomPoke):
		self.__nomPoke = nomPoke
		self.__vie = 100
		self.attaque = 10
		self.defense = 0
		self.niveau = 1

	def getVie(self):
		return (self.__vie)

	def setVie(self, pvPlus):
		self.__vie += pvPlus

	def getNom(self):
		return self.__nomPoke

	def moinsPV(self, nPV):
		self.__vie -= nPV