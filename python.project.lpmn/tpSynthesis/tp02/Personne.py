class Personne: 
    def __init__(self, nom, sexe):
        self._nom = nom
        self._sexe = sexe
        self._adresses = []
    
    @property
    def nom(self):
        return self._nom

    @property
    def sexe(self):
        return self._sexe

    @sexe.setter
    def sexe(self, sexe):
        self._sexe = sexe

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    def get_adresses(self):
        return self._adresses

    def add_adresses(self,e):
		if e not in self._adresses:
			self._adresses.append(e)

    def remove_adresses(self,e):
        if e in self._adresses:
			self._adresses.remove(e)

    